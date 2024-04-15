from backendController import *

db: Data = Data('./JSON/data.json')
print(db.createUser('yo', 'yuh'))
print(db.createUser('Nhi', 'Gyro'))
print(db.loginUser('yo', 'yuh'))
print(db.deleteCurrentUser())
print(db.loginUser('yo', 'yuh'))
print(db.createUser('yo', 'yuh'))
user: User = db.loginUser('yo', 'yuh')
user.createActivity('Jogging')
activity: Activity = user.setCurrentActivity('Jogging')
activity.createEntry('2022/04/18', 3600, 1700, 1)
activity.createEntry('2022/04/18', 3600, 1700, 1)
activity.createEntry('2022/04/18', 3600, 1700, 1)
print(activity.entries[activity.findEntry('2022/04/18')].count)

'''
db.createActivity('yo', 'Skating', 3700, 1000)
db.createActivity('yo', 'Parkouring', 3700, 1000)
db.createActivity('yo', 'Reading', 3700, 1000)
db.createActivity('Nhi', 'Parkouring', 3700, 1000)
db.createActivity('yo', 'Jogging', 3700, 1000)
db.createActivity('yo', 'Jogging', 3700, 1000)
db.createActivity('Nhi', 'Reading', 3700, 1000)
db.createActivity('Nhi', 'Reading', 3700, 1000)
db.createActivity('Nhi', 'Parkouring', 3700, 1000)
db.createUser('John Doe', 'johnnyboy')
db.createActivity('John Doe', 'Jogging', 6969, 420)

'''