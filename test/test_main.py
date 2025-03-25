#!/usr/bin/env python3

import pytest
from git_author_rewrite.main import (
    git,
    display_messages,
    main,
    is_email_format_valid,
    create_working_branch,
    sync_working_branch,
)
from unittest.mock import MagicMock
from git_author_rewrite.enums import Status

TEST_BRANCH_NAME = 'author-rewrite'

@pytest.fixture
def mock_repo():
    """Mock the git.Repo object to avoid real repo modifications."""
    repo = MagicMock(spec=git.Repo)
    rewrite_branch = MagicMock()
    default_branch = MagicMock()

    repo.create_head.return_value = rewrite_branch
    repo.git.merge.return_value = None
    repo.active_branch.name = 'main'
    repo.heads = { 'main': default_branch, 'author-rewrite': rewrite_branch }

    return repo


def test_create_working_branch(mock_repo):
    """Test that the function correctly creates and checks out a branch."""
    branch = create_working_branch(mock_repo)

    # Check if create_head was called with the correct branch name
    mock_repo.create_head.assert_called_once_with(TEST_BRANCH_NAME)

    # Check if checkout() was called once
    branch.checkout.assert_called_once()


def test_sync_working_branch_not_on_active_branch(mock_repo):
    """Test syncing the working branch with the default branch."""  
    default_branch = mock_repo.heads['main']

    rewrite_branch = sync_working_branch(mock_repo, default_branch)

    # Check if merge was called with the correct branch name
    mock_repo.git.merge.assert_called_once_with(default_branch)

    # Check if checkout() was called once 
    rewrite_branch.checkout.assert_called_once()

def test_sync_working_branch_on_active_branch(mock_repo):
    """Test syncing the working branch with the default branch."""  
    default_branch = mock_repo.heads['main']
    mock_repo.active_branch.name = 'main'

    rewrite_branch = sync_working_branch(mock_repo, default_branch)

    # Check if merge was called with the correct branch name
    mock_repo.git.merge.assert_called_once_with(default_branch)

    # Check if checkout() was called once 
    rewrite_branch.checkout.assert_called_once()


def test_display_messages_exits_with_error_and_prints_to_stderr(capfd):
    """Test that the function prints a message to stderr and exits with status code 2."""
    message = "error"

    with pytest.raises(SystemExit) as excinfo:
        display_messages(message, status=Status.ERROR)

    # Capture stdout and stderr
    out, err = capfd.readouterr()

    assert excinfo.value.code == 2, 'Expected an exit code of 2 (stderr)'
    assert message in err, 'Expected a message'


def test_display_messages_prints_to_stdout(capfd):
    """Test that the function prints a message to stdout"""
    message = "message"

    display_messages(message)

    out, err = capfd.readouterr()

    assert message in out, 'Expected a message'


def test_display_messages_exits_and_prints_multiple_messages_to_stderr(capfd):
    """Test that the function prints multiple messages to stderr and exits."""

    messages = ["error 1", "error 2"]
    with pytest.raises(SystemExit) as excinfo:
        display_messages(*messages, status=Status.ERROR)

    out, err = capfd.readouterr()

    assert excinfo.value.code == 2, 'Expected an exit code of 2 (stderr)'
    assert "\n".join(messages) in err, 'Expected two messages';


def test_display_messages_prints_multiple_mesages_to_stdout(capfd):
    """Test that the function prints multiple messages to stdout."""  

    messages = ["message 1", "message 2"]

    display_messages(*messages)

    out, err = capfd.readouterr()
    assert "\n".join(messages) in out, 'Expected two messages';


def test_is_email_format_valid_invalid_email():
    """Test that it detects an invalid email"""
    email = 'example.com'
    assert is_email_format_valid(email) == False


def test_is_email_format_valid_valid_email():
    """Test that it detects a valid email"""
    email = 'example@gmail.com'
    assert is_email_format_valid(email) == True
