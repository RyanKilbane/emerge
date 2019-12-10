import pytest
import workspace
from exceptions import missing_token, get_users_exception

def test_raises_missing_token():
    with pytest.raises(missing_token.MissingToken) as e:
        workspace.SlackWorkspace(None)
    assert str(e.value) == "Slack token not found in environment variables"

def test_raises_empty_token():
    with pytest.raises(missing_token.MissingToken) as e:
        workspace.SlackWorkspace("")
    assert str(e.value) == "Slack token found, but seems to be empty"