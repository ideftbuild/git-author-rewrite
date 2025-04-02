#!/usr/bin/env python3
import sys
from git_author_rewrite.enums import Status


def display_messages(*messages: str, status: Status = Status.SUCCESS):
    """Print messages to stdout or stderr based on status.

    Args:
        messages (str): One or more messages to print.
        status (Status, optional): The message status. Defaults to Status.SUCCESS.

    Raises:
        SystemExit: If status is Status.ERROR, the function exits with an error code.
    """

    if status == Status.ERROR:
        print(*messages, sep='\n', file=sys.stderr)
        sys.exit(status.value)
    else:
        print(*messages, sep='\n')

