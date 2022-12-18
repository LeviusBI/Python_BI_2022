#!/usr/bin/env python3

#option -a - show all files, including hidden

import os
import sys
import argparse



if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='./ls.py [OPTION]... [FILE]...',
        description='''List the FILEs (the current directory by default). Sort entries alphabetically''')

    parser.add_argument('path_to_directory', type=str, default='.', nargs='?')
    
    parser.add_argument('-a', '--all', 
                        action='store_true', 
                        help='do not ignore entries starting with .',
                        required=False)
    
    args = parser.parse_args()
    
    path = args.path_to_directory

    try:
        if args.all:
            files_in_directory = ['.', '..']
            files_in_directory += list(sorted(os.listdir(path)))
        else:
            files_in_directory = sorted(os.listdir(path))
        sys.stdout.write(' '.join(files_in_directory) + '\n')
    except FileNotFoundError:
        sys.stderr.write(f'ls: cannot access \'{path}\': No such file or directory\n')

