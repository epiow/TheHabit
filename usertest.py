import Database
from DataIO import DataIO
io = DataIO('./JSON/data.json')
db = Database.Database(io)

db.registerUser('yo', 'yuh')
db.registerUser('Nhi', 'Gyro')
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
db.registerUser('John Doe', 'johnnyboy')
db.create_activity('John Doe', 'Jogging', 6969, 420)

