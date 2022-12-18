#!/usr/bin/env python3

# import os
# import sys
# import argparse

#option -a - show all files, including hidden


import os
import sys
import argparse





if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        usage='./ls.py [OPTION]... [FILE]...',
        description='''List the FILEs (the current directory by default). Sort entries alphabetically''')

    parser.add_argument('-a', '--all', 
                        action='store_true', 
                        help='do not ignore entries starting with .',
                        required=False)
    parser.add_argument('directory', type=str, default='.', nargs='?',
                        help='directory which content to display ("." by default)')
    
    args = parser.parse_args()
    
    directory = args.directory

    try:
        dir_content = list(sorted(os.listdir(directory)))
        if args.all:
            dir_content.extend(['.', '..'])
        else:
            dir_content = list(sorted(os.listdir(directory)))
        sys.stdout.write('  '.join(dir_content) + '\n')
    except FileNotFoundError:
        sys.stderr.write(f'ls: cannot access \'{directory}\': No such file or directory\n')


# def ls_args():
    # parser = argparse.ArgumentParser(
    #     usage = 'ls.py [OPTION]... [FILE]...',
    #     description = ''' List information about the FILEs (the current directory by default).\n
    #     Exit status:
    #     0  if OK,\n
    #     1  if minor problems (e.g., cannot access subdirectory),\n
    #     2  if serious trouble (e.g., cannot access command-line argument).\n
    #     ''',
    # )
    # parser.add_argument('-a', '--all', 
    #                     help = 'do not ignore entries starting with .',
    #                     required= False, 
    #                     action = 'store_true',)
    # parser.add_argument('path_to_file', type = str, default = '.', nargs = '?')

# if __name__ == '__main__':
    # args = ls_args()
    # path_to_file = args.path_to_file
    
    # try:
    #     files_in_directory = list(sorted(os.listdir(dir)))
    #     if args.all:
    #         files_in_directory.extend()
    #     else:
    #         files_in_directory = os.listdir(dir)
    #     sys.stdout(*files_in_directory + '\n')
    # except FileNotFoundError:
    #     sys.stderr(f'ls: cannot access {path_to_file}: No such file or directory')