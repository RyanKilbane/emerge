import os
class MissingToken(Exception):
    def __init__(self, message):
        super().__init__(message)
    
    @staticmethod
    def add_token():
        token_name = input("Enter token name: ")
        token_value = input("Enter token value: ")
        os.environ[token_name] = token_value
