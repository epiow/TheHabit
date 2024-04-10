import Database

db = Database.Database('./JSON/data.json')


db.register_user('yo', 'yuh')
db.register_user('Nhi', 'Gyro')
db.create_activity('yo', 'Jogging', 3700, 1000)
db.create_activity('yo', 'Skating', 3700, 1000)
db.create_activity('yo', 'Parkouring', 3700, 1000)
db.create_activity('yo', 'Reading', 3700, 1000)
db.create_activity('Nhi', 'Parkouring', 3700, 1000)
db.create_activity('yo', 'Jogging', 3700, 1000)
db.create_activity('yo', 'Jogging', 3700, 1000)
db.create_activity('Nhi', 'Reading', 3700, 1000)
db.create_activity('Nhi', 'Reading', 3700, 1000)
db.create_activity('Nhi', 'Parkouring', 3700, 1000)
db.register_user('John Doe', 'johnnyboy')
db.create_activity('John Doe', 'Jogging', 6969, 420)

