import users
import json
import pathlib

def test_import_users():
    path = pathlib.Path().cwd().joinpath("test").joinpath("users").with_suffix(".json")
    _users = users.Users()
    user_op = users.UserOperations(path).import_users(_users)
    assert _users.users == ["phil.bambridge@ons.gov.uk", "bob@bob.com", "bill@bill.com"]