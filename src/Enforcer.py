'''=======================================================================

    enforcer.py
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
        This the main the script for the commentator commenting 
        anslysis system
    =====================================
    ====================================================================== '''
#Standard library imports
import os
#regex module for rule set parsing
import re

#Commentator imports
import Errors
#TODO: FileRules class
import FileRules

import JavascriptRules

'''=======================================================================

    CLASS

    ======================================================================= '''
class Enforcer(object):
    '''Enforcer
    -----------
    The main (and only, for now) class which handes taking in a file and
    running code analysis on it.  

    TODO: Split up this class'''

    def __init__(self, 
        file_name='',
        prepend_relative_file_name=True,
        file_type=''):
        '''__init__
        -----------
        description
            Called when object is instantiated.
        parameters
            file_name: Specifies the filename to run analysis on
            prepend_relative_file_name=True: specifies wheter '../' should be
                added to the filename or not.  Because this will usually be
                called from this file's parent directory
            file_type: Overrides the file type.  If nothing is passed in
                it is parsed from the file_name
        '''
        #--------------------------------
        #Get filename
        #--------------------------------
        #Make sure file_name is passed in by caller
        if file_name == '':
            #File name must not be empty.  We won't do any other checks 
            #   (yet at least)
            raise Errors.MissingParameter('No file name provided')

        #--------------------------------
        #Get the absolute file name
        #--------------------------------
        #Assume it's an absolute location (if not, we'll overwrite it)
        self.file_name = file_name

        #If the file name does not have a '/' as the first character,
        #   assume it's relative to the current directory
        if file_name[0] != '/' and file_name[0] != '~':
            #File name should be relative to current directory, 
            #   using os.path.dirname

            #If prepend_relative_file_name is True, prepend '../' to 
            #   the file_name (__init__ will usually be called by the 
            #   parent directory)
            if(prepend_relative_file_name is True):
                file_name = '../' + file_name

            self.file_name = os.path.join(os.path.dirname(__file__), 
                file_name)

        #--------------------------------
        #Get the file type
        #--------------------------------
        #Figure out the file type
        if file_type != '':
            #Don't parse the file type from the file name since they passed 
            #   it in
            self.file_type = file_type
        else:
            #file_type is not passed in
            #Split on '.' and get the last index (in case there are
            #   multiple periods in the passed in file name)
            file_name_split = self.file_name.split('.')
            self.file_type = file_name_split[len(file_name_split)-1]

        #--------------------------------
        #Get the rules for the file type
        #--------------------------------
        #TODO: Make this extensible, use a class so it isn't coupled
        #   to one rule set
        self.rule_set = FileRules.FileRules(self.file_type).get_rule_set()
        
        #--------------------------------
        #
        #Statistic data structure
        #
        #--------------------------------
        #--------------------------------
        #Comments
        #--------------------------------
        #Line and characters found (dumb heuristic)
        self.comment_lines_found = 0
        self.comment_characters_found = 0
        #Comment words (any alphanumeric text separated by space)
        self.comment_words_found = 0
        #Comment points (little more smarter measure)
        self.comment_points = 0

        #--------------------------------
        #Code
        #--------------------------------
        #(Same structure as above, FOR NOW)
        self.code_lines_found = 0
        self.code_characters_found = 0
        self.code_words_found = 0
        self.code_points = 0 



        #--------------------------------
        #Call process_file
        #--------------------------------
        self.process_file()

        print self

    #------------------------------------
    #Process file
    #------------------------------------
    def process_file(self):
        '''process_file
        --------------
        description: 
            Open and analyze the file using the self.file_name using
            the rules for self.file_type
        '''
        #--------------------------------
        #Open and process the file
        #--------------------------------
        with open(self.file_name) as target_file:
            #Get the current line
            content = target_file.read()
            #Process the file
            self.analyze_file(content)

    #------------------------------------
    #Analyze file
    #------------------------------------
    def analyze_file(self, content):
        '''analyze_file
        ---------------
        parameters:
            content: content to process
        description:
            Analyze the passed in content (file) based on the file format
            Update this object's properties based on comment and
            code statistics
        '''
        #Build a regex that contains words followed by a space (This regex
        #   will be the same for each iteration in the loop)
        comment_regex = re.compile(r'[a-zA-Z\']* ')

        #Do a regex match for each key in the Ruleset
        for key in self.rule_set:
            #Build a regular expression using the current key in rule_set
            regex = re.compile(r'%s' % (key))
            #Match the regular expression with the string passed in from line
            results = regex.findall(content)

            #Handle results
            if len(results) > 0:
                #We found something, so process it
                
                #TODO: DONT COUNT COMMENTED OUT CODE
                #   Use a regex to make sure there are at least a few words in a
                #   comment
                #TODO: Make comments that are less than N words worth less. 
                #   IN GENERAL (At least until 7 or 8 words)
                #   MORE WORDS = MORE POINTS.  Less words = less points
                #See if it's a comment
                if self.rule_set[key]['type'] == 'comment':
                    #Comment was found, so now we need to do someparsing on it
                    #   to determine its value

                    comment_points = 0
                    for comment in results:
                        #TODO: Write function to test if a comment is just
                        #   commented out code
                        #Things we want:
                        #   1. Don't count commented code as much
                        #   2. Up until 8 words, the length affects the worth

                        #Get the number of words in the comment
                        num_words = comment_regex.findall(comment)
                        num_words_len = len(num_words)

                        #TODO: This should be a scale function
                        #There should be at least 4 words in a comment.
                        #   Anything less isn't counted
                        #LESS THAN CHECKS
                        if num_words_len < 3:
                            #Do nothing
                            comment_points += 0
                        elif num_words_len < 5:
                            #Less then six words, so give some points
                            comment_points += .3
                        elif num_words_len < 7:
                            comment_points += .6
                        elif num_words_len < 8:
                            comment_points += .8

                        #GREAT THAN CHECKS
                        elif num_words_len > 12:
                            comment_points += 1.6

                        #Everything else
                        else:
                            #If the comment length is decent, add some extra 
                            #   points
                            comment_points += 1.3

                    #Add to the amount of comments found
                    self.comment_points += comment_points
                else:
                    #It's code
                    #Add to the code_points the amount of times this match is
                    #   found multiplied by the point value
                    self.code_points += (
                        len(results) * self.rule_set[key]['points']
                    )


    #------------------------------------
    #String represetion
    #------------------------------------
    def __repr__(self):
        '''__repr__
        ----------
        description:
            overrides the built in __str__ method - so when self is printed,
            it will display something custom'''
        return '''
        Commentator Object
        ---------------------------------
        
        file_name: %(file_name)s
        file_type: %(file_type)s
        
        ---------------------------------
        Statistics
        ---------------------------------
        Comments
        --------
        Comment Points: %(comment_points)s

        Code
        --------
        Code Points: %(code_points)s

        Breakdown
        ---------------------------------
        Percentage of comments to code: %(point_percentage)s %%

        ''' % ({
            'file_name': self.file_name,
            'file_type': self.file_type,
            'comment_points': self.comment_points,
            'code_points': self.code_points,
            #Divide comments by code_points and grab the integer of it
            'point_percentage': str(
                int((self.comment_points / (self.code_points * 1.0)) * 100)),
        })

