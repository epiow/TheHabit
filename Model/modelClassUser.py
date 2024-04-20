from modelClassActivity import Activity
class User():
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.currentActivity = None
        self.activities = []
    def createActivity(self, activity_name):
        if self.findActivity(activity_name) == None:
            new_activity = Activity(activity_name) 
            self.activities.append(new_activity)
            return True
        return False
    def findActivity(self, activity_name):
        for activity in self.activities:
            if activity.activity_name == activity_name:
                return self.activities.index(activity)
        return None
    def setCurrentActivity(self, activity_name):
        activityToSet = self.findActivity(activity_name)
        if activityToSet != None:
            self.currentActivity = activityToSet
            return self.activities[self.currentActivity]
        return None
    def editActivity(self, activity_name=None):
        nameSet = False
        if self.findActivity(activity_name) == None:
            if activity_name != None:
                nameSet = True
                self.activities[self.currentActivity].name = activity_name
        return nameSet
    def deleteCurrentActivity(self):
        del self.activities[self.currentActivity]
        self.currentActivity = None
        
