'''=======================================================================

    FileRules.py
    =====================================

    =====================================
    description 
        This file contains the FileRules class 
    TODO: Make this more automatic
    =====================================

    ====================================================================== '''
from Rules_Javascript import RuleSet as Rules_Javascript
from Rules_Coffeescript import RuleSet as Rules_Coffeescript
'''=======================================================================

    CLASS

    ======================================================================= '''
class FileRules(object):
    def __init__(self, file_type):
        '''__init__(self, file_type)
        ----------------------------
        Takes in a file_type (e.g., .js or .coffee) and sets the rule
        set for that file.  It does this by getting the file name and opening
        the file and returning the object
        TODO: Could do more stuff here'''

        self.rule_set = self.rule_set_lookup()[file_type]
        
    def rule_set_lookup(self):
        '''rule_lookup
        --------------
        Returns a dict of file names to file types.  This is just a dictionary
        of file extensions to file type names - __ini__ will call this function
        to determine what file to open.  Files in the directory should be named
            Rules_Filetype.py
        '''

        return {
            'js': Rules_Javascript,
            'coffee': Rules_Coffeescript,
            'py': 'Python',
        }

    def get_rule_set(self):
        '''returns the rule set object'''
        return self.rule_set

