#!/usr/bin/env python3

import pytest
from git_author_rewrite.main import get_author_info


def test_get_author_info_name():
    old_name = 'akan'
    new_name = 'john'
    result = get_author_info(['-n', old_name, new_name])
    assert isinstance(result, dict), "Expected a tuple"
    assert result == { 'old_name': old_name, 'new_name': new_name }, 'Expected to retrieve a names'


	
def test_get_author_info_email():
    old_email = 'example@gmail.com'
    new_email = 'example@yahoo.com'
    result = get_author_info(['-e', old_email, new_email ])
    assert isinstance(result, dict), "Expected a tuple"
    assert result == { 'old_email': old_email, 'new_email': new_email }, 'Expected to retrieve emails'


def test_get_author_info_name_and_email():
    old_name = 'akan'
    new_name = 'john'
    old_email = 'example@gmail.com'
    new_email = 'example@yahoo.com'

    result = get_author_info(['-n', old_name, new_name, '-e', old_email, new_email ])
    assert isinstance(result, dict), "Expected a tuple"
    assert result == { 'old_name': old_name, 'new_name': new_name, 'old_email': old_email, 'new_email': new_email}, 'Expected to retrieve names and emails'


def test_get_author_info_unknown_option(capfd):
    new_email = 'example@yahoo.com'

    with pytest.raises(SystemExit) as excinfo:
        get_author_info(['--invalid'])

    # Capture stdout and stderr
    out, err = capfd.readouterr()

    assert excinfo.value.code == 1, 'Ensure it exists with 1'
    assert "error: unknown option '--invalid'" in err, 'Ensure correct error message'
