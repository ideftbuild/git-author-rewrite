#!/usr/bin/env python3

import pytest
from git_author_rewrite.main import display_err_message, main, is_email_format_valid, check_usage, get_author_info 

STEP = 3


def test_display_err_message(capfd):
    message = "error"

    with pytest.raises(SystemExit) as excinfo:
        display_err_message(message)

    # Capture stdout and stderr
    out, err = capfd.readouterr()

    assert excinfo.value.code == 1, 'Expected exit code of 1'
    assert message in err, 'Expected a message'


def test_is_email_format_valid_invalid_email():
    """Test that it detects an invalid email"""
    email = 'example.com'
    assert is_email_format_valid(email) == False


def test_is_email_format_valid_valid_email():
    """Test that it detects a valid email"""
    email = 'example@gmail.com'
    assert is_email_format_valid(email) == True

def test_get_author_info_name():
    """Verify that it returns an object containing the author name"""
    old_name = 'akan'
    new_name = 'john'
    result = get_author_info(['-n', old_name, new_name], STEP)
    assert isinstance(result, dict), "Expected a tuple"
    assert result == { 'old_name': old_name, 'new_name': new_name }, 'Expected to retrieve a names'


def test_get_author_info_email():
    """Verify that it returns an object containing the author email"""
    old_email = 'example@gmail.com'
    new_email = 'example@yahoo.com'
    result = get_author_info(['-e', old_email, new_email ], STEP)
    assert isinstance(result, dict), "Expected a tuple"
    assert result == { 'old_email': old_email, 'new_email': new_email }, 'Expected to retrieve emails'


def test_get_author_info_name_and_email():
    """Verify that it returns an object containing the author info"""
    old_name = 'akan'
    new_name = 'john'
    old_email = 'example@gmail.com'
    new_email = 'example@yahoo.com'

    result = get_author_info(['-n', old_name, new_name, '-e', old_email, new_email ], STEP)
    assert isinstance(result, dict), "Expected a tuple"
    assert result == { 'old_name': old_name, 'new_name': new_name, 'old_email': old_email, 'new_email': new_email}, 'Expected to retrieve names and emails'


def test_get_author_info_unknown_option(capfd):
    """Test that it detects an unkown option"""
    new_email = 'example@yahoo.com'
    option = '--invalid'

    with pytest.raises(SystemExit) as excinfo:
        get_author_info([option], STEP)

    # Capture stdout and stderr
    out, err = capfd.readouterr()

    assert excinfo.value.code == 1, 'Expected exit code of 1'
    assert f"error: unknown option '{option}'" in err, 'Expected the correct message'


def test_get_author_info_invalid_email_format(capfd):
    """Verify that the email is in the right format"""
    new_email = 'example@.com'

    with pytest.raises(SystemExit) as excinfo:
        get_author_info(['-e', 'example@gmail.com', new_email], STEP)

    # Capture stdout and stderr
    out, err = capfd.readouterr()

    assert excinfo.value.code == 1, 'Expected exit code of 1'
    assert f"error: invalid email format '{new_email}'" in err, 'Expected the correct message'


def test_check_usage(capfd):
    """Test that usage is shown when an invalid number of argument is passed"""
    message = "USAGE: git-author-rewrite [option] [old] [new]. See 'git-author-rewrite --help." 

    with pytest.raises(SystemExit) as excinfo:
        check_usage(['-n', 'new name'])

    # Capture stdout and stderr
    out, err = capfd.readouterr()

    assert excinfo.value.code == 1, 'Expected exit code of 1'
    assert message in err, 'Expected the correct message'


