#!/usr/bin/python3
import sys

options  = ('-n', '--name', '-e', '--email')


def get_author_info(args: list):
    author_info = {}
    step = 3

    for i in range(0, len(args), step):

        # Check if option is supported
        if args[i] not in options:
            print(f"error: unknown option '{args[i]}'", file=sys.stderr)
            exit(1)

        # Retrieve author info from argument
        match args[i]:
            case '-n' | '--name':
                author_info['old_name'] = args[i + 1]
                author_info['new_name'] = args[i + 2]
            case '-e' | '--email':
                author_info['old_email'] = args[i + 1]
                author_info['new_email'] = args[i + 2]

    print('author info is: ', author_info)
    return author_info


# Author info
get_author_info(sys.argv[1:])
