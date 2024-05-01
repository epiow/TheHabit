from Model.modelClassUser import User
class Data():
    def __init__(self, file_path):
        self.file_path = file_path
        self.currentUser = None
        self.users: list[User] = []
    def createUser(self, username, password):
        if self.findUser(username) == None:
            new_user = User(username, password)
            self.users.append(new_user)
            return True
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
        usernameSet = False
        passwordSet = False
        if self.findUser(username) == None:
            if username != None:
                usernameSet = True
                self.users[self.currentUser].username = username
            if password != None:
                passwordSet = True
                self.users[self.currentUser].password = password
        return [usernameSet, passwordSet]
    def deleteCurrentUser(self):
        del self.users[self.currentUser]
        self.currentUser = None
        return True
    

