from unittest import TestCase
from BookReviewFromScratch.without_database import user
from datetime import datetime


class TestUser(TestCase):

    def test(self):
        registered_user = user.register("foo", "bar", "bar", "30/12/1980")

        self.assertDictEqual(registered_user,  {"username": "foo", "password": "bar", "dateOfBirth": "30/12/1980"})
        
        self.assertEqual(registered_user, user.login("foo", "bar"))


        # test login with invalid password
        self.assertRaises(user.InvalidPassword, user.login, "foo", "wrongPassword")

        # test login with user who does not exist 
        self.assertRaises(user.InvalidUsername, user.login, "bar",  "bar")


        # test register with user name who already exist 
        self.assertRaises(user.UserAlreadyExist, user.register, "foo", "password", "password", "30/12/1980")


        # test register user with password missmatch 
        self.assertRaises(user.PasswordMissmatch, user.register, "favw", "password", "passwOrd", "30/12/1980")

        # test invalid date of birth 
        self.assertRaises(user.InvalidDateOfBirth, user.register, "favw", "password", "password", "invalid_date")


