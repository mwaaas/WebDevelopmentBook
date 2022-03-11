from typing import List

# This will act as our store for a start we will later convert it to something that can be persisted. 
# the structure of this should end up with something like this 
# {"john": {"password": "mypassword", "dateOfBirth": "30/12/1980"}}
users = {}




# exception throw when username does not exist 
class InvalidUsername(Exception):
    pass 

# exception throw when password is invalid
class InvalidPassword(Exception):
    pass 

# exception throw when registering a user who already exist
class UserAlreadyExist(Exception):
    pass 


# exception thrown when registering a user with password missmatch i.e password 1 and 2 are not same 
class PasswordMissmatch(Exception):
    pass 


class InvalidDateOfBirth(Exception):
    pass 


def login(username: string, password: string) -> {}:
    """ 
    Returns user details if user exist else returns None
    """
    pass


def register(username: string, password: string, password2: string, dateOfBirth: string):
    """
    if user exist return error saying user already exist 

    if password1 and password2 are equal and username does not exist it will create 
    a new user on our user dictionary and return user. 

    if password1 and password2 is not equal raise an error.  
    """
    pass


def list_users() -> List:
    pass 

if __name__ == '__main__':
    login("foo", "mysecret_password")