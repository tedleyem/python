###### ASCII ART FILE IMPORTS ######
import default
import unix_placeholder
import windows_8
import windows
import arch_big
import swastika
import swastika_no_unicode
import ubuntu
import gentoo
import macosx
import apple
######/ASCII ART FILE IMPORTS ######

import re
import pyFetch.Debug

lineno = 0 # current line number for line()
maxwidth = 0 # maximum width
artlist = [] # loaded ascii art

def setMaxWidth(width):
    """\
    Set the maximum terminal width. All text drawn by `line()` will be truncated
    at this length.

    Defaults to 0, meaning no truncation will be performed.

    :param width: int
    """

    assert isinstance(width, int), "Maximum width should be an integer"
    global maxwidth
    maxwidth = width

def line(ascii, text = "", fill = False):
    """\
    Print a line of ASCII art followed by text. Used by the draw() function.
    If `fill` is `True`, this function will print all remaining lines of ASCII art.
    Expects ascii[0] to be a line of spaces with the same length as the rest of the lines.

    :param ascii: list
    :param text: string
    :param fill: bool
    """

    global lineno

    class Mark:
        pass

    mark = Mark()
    mark.skip = mark.len = 0
    mark.out = mark.input = ""

    if not ascii:
        mark.input = text
        return None
    elif fill:
        if lineno < len(ascii.ascii_art):
            print '\n'.join(ascii.ascii_art[lineno:])
            return None
    else:
        if lineno < len(ascii.ascii_art):
            mark.input = "%s %s" % (ascii.ascii_art[lineno], text)
        else:
            mark.input = "%s %s" % (ascii.ascii_art[0], text)

    if maxwidth == 0:
        print mark.input
        lineno += 1
        return None

    for character in mark.input:
        if character == "\x1b":
            # start of color character
            mark.skip += 4
        elif mark.skip != 0:
            mark.skip -= 1
        else:
            mark.len += 1
        
        mark.out += character

        if mark.len == maxwidth:
            print mark.out
            lineno += 1
            return None

    print mark.out
    lineno += 1

def system(sys, warn=True):
    """\
    Get the ASCII art for the given system.

    :param sys: string
    :rtype: list
    """

    if str(type(sys)) == "<type 'module'>" and sys.ascii_art:
        return sys
    elif isinstance(sys, str):
        if sys in artlist:
            return eval("%s" % sys)
        else:
            if warn:
                print "WARNING: selected ASCII art not found, returning the default one"
            return default
    else:
        pyFetch.Debug.debug("pyFetch.ascii.system: expected sys to be <type 'str'> or <type 'module'>, got %s" % type(sys))
        return default

def list():
    """\
    Print all available ASCII art images to the screen.

    :rtype: None
    """

    global lineno
    from colorama import Fore, Back, Style

    for module in artlist:
        lineno = 0
        b = system(module)
        print
        print "%s%s" % (Fore.RESET, '-' * 80 if maxwidth is 0 else maxwidth)
        print "--%s %s" % (Fore.RESET, module)
        line(b, fill=True)
        print Style.RESET_ALL

excludes = [
    '__.*__',
    're',
    'pyFetch',
    'excludes',
    'line',
    'list',
    'system',
    'maxwidth',
    'setMaxWidth',
    'lineno',
    'artlist',
]

for x in dir():
    try:
        for item in excludes:
            if re.match(item, x):
                raise Exception
        artlist.append(x)
    except:
        pass
