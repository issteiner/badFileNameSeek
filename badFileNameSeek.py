#! /usr/bin/env python3

# Tool for looking for non UTF-8 filenames
# It can print out the directory of the bad filename 

import argparse
import os
import sys
import codecs

def find_bad_filenames(folders):
    for actual_folder in folders:
        if os.path.exists(actual_folder):
            # Find the same size files and append them to samesize_files dictionary
            file_bad_filename(actual_folder)
        else:
            print('\'{}\' is not a valid path. Please verify.'.format(actual_folder))

def file_bad_filename(folder):
    for dirname, subdirs, filelist in os.walk(folder):
        for filename in filelist:
            fullpath_filename = os.path.join(dirname, filename)
            try:
                u = codecs.encode(filename, 'utf-8')
            except UnicodeEncodeError:
                print('There is a problem with some filenames in folder \'{}\'. Please check and fix it.'.format(os.path.dirname(fullpath_filename)))

def main():
    parser = argparse.ArgumentParser(description='Find non UTF-8 filenames')
    parser.add_argument(
        'folders', metavar='dir', type=str, nargs='+',
        help='A directory to parse for non UTF-8 filenames',
        )
    args = parser.parse_args()
 
    find_bad_filenames(args.folders)

if __name__ == '__main__':
    main()
