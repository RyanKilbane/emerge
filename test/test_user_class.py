import users

def test_add_with_string():
    x = users.Users()
    x + "abc@efg.com"
    assert x.users ==  ["phil.bambridge@ons.gov.uk", "abc@efg.com"]

def test_add_with_list():
    x = users.Users()
    x + ["abc@efg.com", "hig@klm.com"]
    assert x.users == ["phil.bambridge@ons.gov.uk", "abc@efg.com", "hig@klm.com"]