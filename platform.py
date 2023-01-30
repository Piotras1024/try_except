'''keypress - A module for detecting a single keypress.
msvcrt is working only for windows
alternative (in except) getkey() is for linux/apple
'''

try:
    import msvcrt

    def getkey():
        '''Wait for keypress and return a single character string.'''
        return msvcrt.getch()

## alternative way to get key for linx and OS (apple)
except ImportError:
    import sys
    import tty
    import termios

    def getkey():
        '''Wait for a keypress and return a single character string.'''
        fd = sys.stdin.fileno()
        orginal_attributes = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, orginal_attributes)
        return ch

# if either of the Unix-specific tty or termios are not found,
# we allow the importError to propagate from here

