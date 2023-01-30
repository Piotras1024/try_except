"""
try:
    #try-block
finally:
    #executed no matter how the try-block terminates
"""

import os
import sys


def make_at(path, dir_name):
    orginal_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)          #if os.mkdir fail you would loose the orginal_path
                                    #That's the reason why try and finally are HERE :)
    finally:
        os.chdir(orginal_path)


def make_at(path, dir_name):
    orginal_path = os.getcwd()
    os.chdir(path)
    try:
        os.mkdir(dir_name)  # if os.mkdir fail you would loose the orginal_path
        # That's the reason why try and finally are HERE :)

    except OSError as error:            #this give you more information what error is interrupting
        print(error, file=sys.stderr)   #your job.
        raise
    finally:
        os.chdir(orginal_path)          #save the orginal_path no matter what !!!
