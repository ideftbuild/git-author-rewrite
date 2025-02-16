#!/usr/bin/python3
import sys
import re
# import gitpython

options  = ('-n', '--name', '-e', '--email')


def display_err_message(message: str):
    print(message, file=sys.stderr)
    exit(1)


def is_email_format_valid(email: str) -> bool:
    pattern = r'.+@.+.com'
    return False if re.match(pattern, email) is None else True


def get_author_info(args: list, step: int) -> dict: 
    author_info = {}

    for i in range(0, len(args), step):

        # Check if option is supported
        if args[i] not in options:
            display_err_message(f"error: unknown option '{args[i]}'")

        # Retrieve author info from argument
        match args[i]:
            case '-n' | '--name':
                author_info['old_name'] = args[i + 1]
                author_info['new_name'] = args[i + 2]
            case '-e' | '--email':
                old_email = args[i + 1]
                new_email = args[i + 2]

                if not is_email_format_valid(new_email):
                    display_err_message(f"error: invalid email format '{new_email}'")
                author_info['old_email'] = old_email
                author_info['new_email'] = new_email

    print('author info is: ', author_info)
    return author_info


def check_usage(args: list):
    usage_message = "USAGE: git-author-rewrite [option] [old] [new]. See 'git-author-rewrite --help."
    step = 3

    if len(args) % step != 0:
        display_err_message(usage_message)


def main(args: list = sys.argv[1:]):
    # Author info
    # help(gitpython)
    check_usage(args)

    step = 3
    get_author_info(args, step)

if __name__ == '__main__':
    main()
    
