# write your code here
import os
import sys
import argparse


def sorting_options():
    print('Size sorting options:')
    print('1. Descending')
    print('2. Ascending')
    print()
    print('Enter a sorting option:')
    while True:
        try:
            sorting_type = int(input())
        except TypeError:
            pass
        else:
            if sorting_type in [1, 2]:
                break
        print()
        print('Wrong option')
        print()
        print('Enter a sorting option:')
    return True if sorting_type == 1 else False     # True for sorted(,reverse=True)


def file_dic_construct(file_dir, file_format):
    file_dic = dict()
    for root, dirs, files in os.walk(file_dir, topdown=True):
        for name in files:
            if name.endswith(file_format):
                paths = os.path.join(root, name)
                size = os.path.getsize(paths)
                if size in file_dic.keys():
                    file_dic[size].append(paths)
                else:
                    file_dic[size] = [paths]
        # for name in dirs:
        #     print(os.path.join(root, name))
    return file_dic


try:
    # parser = argparse.ArgumentParser()
    # parser.add_argument("file_dir")
    # args = parser.parse_args()
    # file_directory = args.file_dir
    file_directory = sys.argv[1]
except IndexError:
    print('Directory is not specified')
else:
    # os.chdir(file_directory)
    print('Enter file format:')
    file_format = input()
    print()
    sorting = sorting_options()
    file_dictionary = file_dic_construct(file_directory, file_format)
    for key in sorted(file_dictionary.keys(), reverse=sorting):
        print()
        print(key, 'bytes')
        for path in file_dictionary[key]:
            print(path)
