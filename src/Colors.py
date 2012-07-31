'''=======================================================================

    Colors.py
    =====================================
    description 
        Contains terminal colors for printing stuff
    =====================================
    ====================================================================== '''
class Colors(object):
    '''Colors
    -----------
    Outputs terminal codes for background / foreground colors.  Use
    by calling Colors.color or Colors.bg_color
    '''
    #Reset
    reset = '\033[0m'
    bold = '\033[1m'

    #Foreground Colors
    black = '\033[30m'
    red = '\033[31m'
    green = '\033[32m'
    yellow = '\033[33m'
    blue = '\033[34m'
    magenta = '\033[35m'
    cyan = '\033[36m'
    white = '\033[37m'

    #Background Colors
    bg_black = '\033[40m'
    bg_red = '\033[41m'
    bg_green = '\033[42m'
    bg_yellow = '\033[43m'
    bg_blue = '\033[44m'
    bg_magenta = '\033[45m'
    bg_cyan = '\033[46m'
    bg_white = '\033[47m'

    #Extra characters
    smiley = '\xE2\x98\xBA'
