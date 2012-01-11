'''=======================================================================

    JavascriptRules.py
    =====================================

    =====================================
    description 
        This file describes a rules object for Javascript files.

        TODO: These rules should all be extensible.  Should follow the basic
        format of the key being the Code string to match,
        and the key being a dict of various attributes related to that key
    =====================================
    ====================================================================== '''
'''RuleSet
----------
This is a dictionary containing keys which map to some regex that will get run
    whose value is a dictionary containing various properties that describe
    what to do when the match is found.  

The following describes the data structure:

'regex key': {
    'type': 'code' OR 'comment',
}

    TODO:
        Code and Comments each have 'points', so for instance a function in code
        has more 'code points' than a regular code expression does
'''

RuleSet = {
    #------------------------------------
    #Comments
    #   Don't count comment blocks for JS.
    #------------------------------------
    '\/\/.*\n': {
        'type': 'comment',
        'points': 1,
    },
    '#.*\n': {
        'type': 'comment',
        'points': 1,
    },

    ## NOTE: If you wanted to count comment blocks, example:
    ##JS
    #'\/\*.*\*\/': {
    #    'type': 'comment',
    #}, 
    ##COFFEE
    #'\"\"\".*\"\"\"':{
    #    'type': 'comment',
    #}, 
    #'""".*"""':{
    #    'type': 'comment',
    #}, 

    #------------------------------------
    #Code
    #------------------------------------
    'function': {
        'type': 'code',
        'points': 4,
    },
    'class': {
        'type': 'code',
        'points': 4,
    },
    'switch': {
        'type': 'code',
        'points': 4,
    },
    'for': {
        'type': 'code',
        'points': 2,
    },
    'if': {
        'type': 'code',
        'points': 2,
    },

    #------------------------------------
    #Coffee Script
    #------------------------------------
    '\-\>': {
        'type': 'code',
        'points': 4,
    },
    '\=\>': {
        'type': 'code',
        'points': 4,
    },
    'when': {
        'type': 'code',
        'points': 2,
    },
}
