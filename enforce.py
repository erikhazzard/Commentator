'''=======================================================================

    enforce.py
    =====================================
    parameters
        target_file: the target file to run the comment analysis on
    =====================================
    
    =====================================
    sample call
       -When calling this script, pass in the name of the file you want to
        analyze. example:

       $ enforcer.py my_script.js
    =====================================

    =====================================
    description 
        This script takes in a file name and sets up the Enforcer class,
        running comment analysis on it
    =====================================

    ====================================================================== '''
'''=======================================================================

    IMPORTS

    ======================================================================= '''
#Standard library imports
import sys

#Enforcer imports
import src.Enforcer as Enforcer
'''=======================================================================

    INIT

    ======================================================================= '''
if __name__ == '__main__':
    '''If this script is called from the command line, the __name__ property
    is given the value '-__name__', so this if statement will get executed
    when calling this script from the command line'''
    #Get the file name, will be the second item (first is the script 
    #   name itself)
    #Make sure a file name is passed in
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        #Filename was not passed in, so raise the MissingParameter error
        raise Enforcer.Errors.MissingParameter('''
No filename provided.  
Please provide a filename - either relative or absolute, e.g.,
    python enforcer.py filename.py''')

    #------------------------------------
    #Create a new Enforcer object with the passed in file
    #------------------------------------
    #Pass in the file name.  If we wanted to, we could override the file 
    #   extension
    enforce_object = Enforcer.Enforcer(
            file_name=file_name
    )
