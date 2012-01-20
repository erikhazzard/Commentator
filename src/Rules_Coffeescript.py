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
    #------------------------------------
    '\/\/': {
        'type': 'comment',
    },
    '\/\*': {
        'type': 'comment',
    },
    '\*\/': {
        'type': 'comment',
    },
    '#': {
        'type': 'comment',
    },

    #------------------------------------
    #Code
    #------------------------------------
    'function': {
        'type': 'code',
    },
    '\-\>': {
        'type': 'code',
    },
    '\=\>': {
        'type': 'code',
    },
    'class': {
        'type': 'code',
    },
    'when': {
        'type': 'code',
    },
    'switch': {
        'type': 'code',
    },
    'for': {
        'type': 'code',
    },
    'if': {
        'type': 'code',
    },
}
