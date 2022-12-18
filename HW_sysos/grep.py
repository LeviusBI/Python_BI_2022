#!/usr/bin/env 
import argparse
import os, sys
import regex


if __name__ == '__name__':

    parser = argparse.ArgumentParser(
        'grep.py',
        usage='grep [OPTION]... PATTERNS [FILE]...',
        description='Search for PATTERNS in each FILE.' \
                    'Patterns can contain multiple patterns separated by newlines'
    )
    
    parser.add_argument('pattern', type=str,)
    
    parser.add_argument('files', metavar='')