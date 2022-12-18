#!/usr/bin/env python3

import os
import sys
import argparse

# option -l - show number of lines in file
# option -c - show quantity of bytes in file
# option -w - show number of words in file
def main():
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
        
    def extract_actions_list(args):
        del args['filename']
        if not any(args.values()):
            return list(args.keys())
        else:
            return [action for action, is_needed in args.items() if is_needed]


    def lines_counter(data):
        return len(open(data).readlines())


    def count_words(data):
        return len(data.split())


    def count_bytes(data):
        return os.path.getsize(data)
        
    file_content = args.filename.read()
    actions = extract_actions_list(vars(args))

    functions = {'lines': lines_counter,
                'words': count_words,
                'bytes': count_bytes
                }

    results = []
    for action in actions:
        results.append(functions[action](file_content))

    sys.stdout.write('\t' + '\t'.join(map(str, results)) + '\n')







if __name__ == '__main__':
    try:
       main()
    except SystemExit:
       sys.exit(1)
    else:
        sys.exit(0)