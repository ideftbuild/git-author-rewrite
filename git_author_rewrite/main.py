#!/usr/bin/python3
import sys
import re
import git
import argparse
from git_author_rewrite.enums import Status
from git_author_rewrite.installer import ensure_pip_packages
from git_author_rewrite.message_handler import display_messages


BRANCH_NAME = 'author-rewrite'


def is_email_format_valid(email: str) -> bool:
    """Validate whether an email is in a proper format.

    Args:
        email (str): The email address to validate.

    Returns:
        bool: True if the email format is valid, False otherwise.
    """

    pattern = r'.+@.+.com'
    return False if re.match(pattern, email) is None else True


def create_parser() -> argparse.ArgumentParser:
    """Create and return a command-line argument parser.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """

    parser = argparse.ArgumentParser(
        prog='git-author-rewrite',
        description='git-author-rewrite is a command-line tool that allows developers to update the author name and/or email in Git commit history. It offers flexible options to either interactively modify specific commits or perform a full history rewrite, ensuring accurate attribution while minimizing disruption to collaborators.',
        epilog='Checkout out https://github.com/ideftbuild/git-author-rewrite')

    parser.add_argument('-n', '--name', nargs=2, metavar=('old_name', 'new_name'), help='Provide the old name to update and the new name')
    parser.add_argument('-e', '--email', nargs=2, metavar=('old_email', 'new_email'), help='Provide the old email to update and the new email')
    parser.add_argument('-l', '--local-path', help='Provide the path to the local repository')
    parser.add_argument('-r', '--reset', help='Reset for a fresh start')
    
    return parser


def create_working_branch(repo: git.Repo) -> git.HEAD:
    """Create working branch for which the changes will be applied too

    Args:
        repo (git.Repo): the repo

    Returns:
        git.HEAD: the working branch
    """

    rewrite_branch = repo.create_head(BRANCH_NAME)
    display_messages(f'Created new branch: ' + BRANCH_NAME)

    rewrite_branch.checkout()
    display_messages(f'Switched to new branch: {BRANCH_NAME}')
    return rewrite_branch


def sync_working_branch(repo: git.Repo, default_branch: git.HEAD) -> git.HEAD:
    """Sync the working branch with the default branch.

    Args:
        repo (git.Repo): The Git repository.  
        default_branch (git.HEAD): The default branch to sync with.  

    Returns:
        git.HEAD: The updated working branch.  
    """

    if repo.active_branch.name != BRANCH_NAME:
        rewrite_branch = repo.heads[BRANCH_NAME]
        rewrite_branch.checkout()
        display_messages(f"Switched to '{BRANCH_NAME}'")

    repo.git.merge(default_branch)  # Update the branch 
    display_messages(f"Merged '{default_branch.name}' to '{BRANCH_NAME}'")
    return rewrite_branch


def main(args: list = sys.argv[1:]):
    """main entry point for the script.

    Args:
        args (list, optional): command-line arguments. defaults to sys.argv[1:].
    """
    ensure_pip_packages()

    parser = create_parser()

    args = parser.parse_args()

    repo = git.Repo(args.local_path if args.local_path else '.')  # Connect to repo

    print('Repository:', repo)

    if 'origin' not in repo.remotes:
        display_messages("No remote named 'origin' found", status=Status.ERROR)
    
    default_branch = repo.heads.main if 'main' in repo.heads else repo.heads.master;

    repo.git.checkout(default_branch.name)
    display_messages(f"Switched to '{default_branch.name}'")
    
    repo.remotes.origin.pull(refspec=default_branch.name)
    display_messages('Pulled latest changes from remote')

    # Delete working branch if --reset is passed  
    if args.reset:
        repo.git.branch('-D', BRANCH_NAME)

    rewrite_branch = None
    try:
        if BRANCH_NAME in repo.heads:
            rewrite_branch = sync_working_branch(repo, default_branch)
        else:
            # Create branch if --reset is passed or it doesn't exist  
            rewrite_branch = create_working_branch(repo)
    except Exception as e:
        display_messages(f"Error: Failed to rewrite branch '{BRANCH_NAME}': {e}",
                         'To proceed, you can:',
                         '  - Fix the errors and retry.',
                         "  - Use the '-r' or '--reset' option to delete this branch and start fresh.",
                         status=Status.ERROR)


if __name__ == '__main__':
    main()
    
