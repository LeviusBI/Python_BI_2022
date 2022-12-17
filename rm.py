#!/usr/bin/env python3

import os
import sys
import argparse

# option -r - recursive deletion

def rm_args():
    parser = argparse.ArgumentParser(
        prog = 'rm.py [OPTION].. [FILE]...',
        description = ''' Remove (unlink) the FILE(s).\n
        
        By default, rm does not remove directories.  Use the --recursive (-r or -R)\n
        option to remove each listed directory, too, along with all of its contents.\n
        To remove a file whose name starts with a '-', for example '-foo',\n
        use one of these commands:\n
        rm -- -foo\n

        rm ./-foo\n
        ''' 
    )
    parser.add_argument('-r', '-R', '--recursive')