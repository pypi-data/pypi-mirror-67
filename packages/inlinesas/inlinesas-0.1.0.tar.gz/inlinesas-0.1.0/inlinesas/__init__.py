import os
import tempfile
from sasrunner import SAS

def call_SAS(code_as_str, *flags, **options):
    """ 
    Call SAS from within a Python script. 

    Usage:
    =======================================

    from inlinesas import call_SAS

    sascode = '''your SAS code as a string'''
    result = call_SAS(sascode)
    
    result = call_SAS(sascode)

    # You can also pass in any options you'd pass to SAS
    # on the commandline.
    #
    # Example:
    result = call_SAS(sascode, 'nodms', 'nolog')

    =======================================

    You can access the returncode, stdout, and stderr of your SAS run:

    result.returncode
    result.stdout
    result.stderr
    
    """
    # Write code_as_str to temporary file
    f = tempfile.NamedTemporaryFile(delete=False)
    f.write(code_as_str)
    f.close() 

    sas_call = SAS(*flags, sysin=f.name, **options)
    sas_call.run()

    # Remove the temporary file
    os.unlink(f.name) 
    
    return sas_call
