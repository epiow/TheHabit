import Database

db = Database.Database('./JSON/data.json')

db.register_user('yo', 'yuh')
db.create_activity('yo', 'Jogging', 3700, 1000)
db.create_activity('yo', 'Jogging', 3700, 1000)
db.create_activity('yo', 'Reading', 3700, 1000)
db.create_activity('yo', 'Reading', 3700, 1000)