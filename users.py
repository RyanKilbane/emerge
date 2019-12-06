class Users:
    def __init__(self):
        self.users = ["phil.bambridge@ons.gov.uk"]

    def __add__(self, email):
        self.users.append(email.lower())

    def __getitem__(self, index):
        return self.users[index]

class UserOperations:
    def __init__(self, file):
        self.file = file
    
    def export_users(self, users: Users):
        # will write to disk for persistent storage
        pass

    def import_users(self, users: Users):
        # will import yaml of users
        pass