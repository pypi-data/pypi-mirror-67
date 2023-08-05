# inlinesas #

Call SAS from within a Python script. Pass your SAS code as a string to the call_SAS function. 

Usage:
=======================================

    from inlinesas import call_SAS

    sascode = 'your SAS code as a string'
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


You can access the returncode, stdout, and stderr of your SAS run:

`result.returncode`

`result.stdout`

`result.stderr`

