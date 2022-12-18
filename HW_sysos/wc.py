#!/usr/bin/env python3

import os
import sys
import argparse

# option -l - show number of lines in file
# option -c - show quantity of bytes in file
# option -w - show number of words in file
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            usage='./wc.py [OPTION]... [FILE]...',
            description='''Print newline, word, and byte counts for each FILE, and a total line 
                            if more than one FILE is specified. A word is a non-zero-length sequence
                            of characters delimited by white space. With no FILE. or when FILE is -
                            , read standert input.''')

    parser.add_argument('filename', 
                        type=argparse.FileType('r'), 
                        default=sys.stdin, 
                        nargs='?')
        
    parser.add_argument('-l', '--lines',
                        action='store_true',
                        help='print the newline counts',
                        required=False)
        
    parser.add_argument('-w', '--words', 
                        action='store_true', 
                        help='print the character counts', 
                        required=False)
        
    parser.add_argument('-c', '--bytes',
                        action='store_true',
                        help='print the byte counts',
                        required=False)
        
    args = parser.parse_args()
        
    filename = args.filename
    
    file_content = args.filename.read()
        
    def lines_counter(data):
        return len(open(data).readlines())


    def words_counter(data):
        return len(data.split())


    def byte_syze(data):
        return os.path.getsize(data)
        

    functions = {'lines': lines_counter,
                'words': words_counter,
                'bytes': byte_syze
                }
    
