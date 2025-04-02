import pytest
from git_author_rewrite.enums import Status 
from git_author_rewrite.message_handler import display_messages


def test_display_messages_exits_with_error_and_prints_to_stderr(capfd):
    """Test that the function prints a message to stderr and exits with status code 2."""
    message = "error"

    print("display messages is correctly imported: ", display_messages)
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

