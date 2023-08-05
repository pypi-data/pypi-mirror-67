import os
import subprocess
import pipes


class SAS(object):
    """
    Scaffolding to accept arbitrary SAS commandline options.

    All options defined here for 9.3: 
        https://support.sas.com/documentation/cdl/en/hostunx/63053/HTML/default/viewer.htm#n0nnsvhnt2jwevn1fha4dz2n4g0y.htm

    Example:
    =======

    # You'd like to call SAS with -nolog and -sysin
    sas = SAS('nolog', sysin='/wrds/some/sas/path.sas')

    All flag options (-nolog, -nodms, etc.) must be passed in
    before keyword args are provided.
    """
    def __init__(self, *flags, **options):
        flag_options = []
        for flag in flags:
            if flag.startswith('-'):
                flag_options.append(flag)
            else:
                flag_options.append('-{}'.format(flag))

        # Enforced default
        sas_version = 'sas'

        options_with_args = []
        for key, value in options.items():
            # If you need to pass in the path
            # to the SAS execuable directly
            if key == 'path_to_sas':
                sas_version = value
                continue

            if key == 'utf8':
                if value == True:
                    sas_version = 'sas_u8'
                elif value == False:
                    sas_version = 'sas'
                else:
                    raise Exception("Please pass utf8=True or utf8=False. I received utf={}".format(value))
                continue

            options_with_args.append('-{}'.format(key))
            options_with_args.append(pipes.quote(value))
                 
        self.invocation = [sas_version] + flag_options + options_with_args
        self.log = self._logfile()

    def _get_cmdline_arg(self, arg):
        for idx, item in enumerate(self.invocation):
            if item == arg:
                return self.invocation[idx+1]
        return False

    def _logfile(self):
        if ('-nolog' in self.invocation) or ('nolog' in self.invocation):
            return 'SAS was run with -nolog, so no log is available.'
        elif '-log' in self.invocation:
            return self._get_cmdline_arg('-log')
        else:
            sasfile = self._get_cmdline_arg('-sysin')
            saslog = os.path.split(sasfile)[1].replace('.sas', '.log')
            return os.path.join(os.getcwd(), saslog)
    
    def __str__(self):
        return 'SAS call: {}'.format(' '.join(self.invocation))

    def run(self):
        r = subprocess.Popen(
            self.invocation, 
            stdout=subprocess.PIPE, 
            stderr=subprocess.PIPE
        )
        stdout, stderr = r.communicate()

        self.stdout = stdout.decode()
        self.stderr = stderr.decode()

        self.returncode = r.returncode
