#!/usr/bin/env python3

import os
import sys
import argparse

#option -a - show all files, including hidden

def ls_args():
    parser = argparse.ArgumentParser(
        usage = 'ls.py [OPTION]... [FILE]...',
        description = ''' List information about the FILEs (the current directory by default).\n
        Exit status:
        0  if OK,\n
        1  if minor problems (e.g., cannot access subdirectory),\n
        2  if serious trouble (e.g., cannot access command-line argument).\n
        '''
    )
    parser.add_argument('-a', '--all')

if __name__ == '__main__':
    args = ls_args()
    
    try:
        files_in_directory = list(sorted(os.listdir(dir)))