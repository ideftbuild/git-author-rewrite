#!/usr/bin/env python3

import pytest
from git_author_rewrite.main import display_messages, main, is_email_format_valid
from git_author_rewrite.enums import Status


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
