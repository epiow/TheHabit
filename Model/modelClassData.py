from Model.modelClassUser import *
from Model.modelClassActivity import *
from Model.modelClassCalendar import *
from pyrebase import pyrebase
from datetime import datetime
from config import config_keys as keys

class Database:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()

class Data:
    def __init__(self):
        self.firebase = pyrebase.initialize_app(keys)
        self.auth = self.firebase.auth()
        self.db = self.firebase.database()
        self.currentUser = None
        self.users = []
        self.is_authenticated = False

    def createUser(self, username, password):
        try:
            self.auth.create_user_with_email_and_password(username, password)
            return True
        except Exception as e:
            print(f"Error creating user: {e}")
            return False
    
    def findUser(self, username):
        for user in self.users:
            if user.username == username:
                return self.users.index(user)
        return None
    
    def loginUser(self, username, password):
        userToLogin = self.findUser(username)
        if userToLogin != None:
            if self.users[userToLogin].password == password:
                self.currentUser = userToLogin
                return self.users[self.currentUser]
        return None
    
    def editUser(self, username=None, password=None):
        if self.currentUser is not None:
            if username is not None:
                self.currentUser.username = username
                self.db.set_name(username)
            if password is not None:
                self.currentUser.password = password
            return [username is not None, password is not None]
        return [False, False]

    def deleteCurrentUser(self):
        if self.currentUser is not None:
            self.db.delete_user(self.currentUser.username)
            del self.users[self.users.index(self.currentUser)]
            self.currentUser = None
            return True
        return False

    
