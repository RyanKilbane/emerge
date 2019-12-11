import json
class Users:
    def __init__(self):
        self.users = ["phil.bambridge@ons.gov.uk"]

    def __add__(self, email: (str, list)):
        if isinstance(email, str):
            self.users.append(email.lower())
        elif isinstance(email, list):
            for i in email:
                self.users.append(i.lower())

    def __getitem__(self, index):
        return self.users[index]

    def __len__(self):
        return len(self.users)
# Structure of data:
# {
#   "users": [EMAIL ADDRESSES]
# }
class UserOperations:
    def __init__(self, file: str):
        self.file = file
    
    def export_users(self, users: Users):
        # will write to disk for persistent storage
        with open(self.file, "w") as f:
            f.write(json.dumps({"users": Users.users}))

    def import_users(self, users: Users):
        # will import yaml of users
        with open(self.file, "r") as f:
            emails = json.loads(f.read())
        Users + emails["users"]
