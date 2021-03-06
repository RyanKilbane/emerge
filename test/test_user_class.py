import users
import workspace
import pytest
from exceptions import missing_token, get_users_exception
def test_add_with_string():
    x = users.Users()
    x + "abc@efg.com"
    assert x.users ==  ["phil.bambridge@ons.gov.uk", "abc@efg.com"]

def test_add_with_list():
    x = users.Users()
    x + ["abc@efg.com", "hig@klm.com"]
    assert x.users == ["phil.bambridge@ons.gov.uk", "abc@efg.com", "hig@klm.com"]
