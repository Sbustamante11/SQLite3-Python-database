import sqlite3
# initialize connection to database
connection = sqlite3.connect('db_02.db')
# initialize cursor to perform operations
cursor = connection.cursor()

# valid data types
'''
DATA TYPES

NULL. The value is a NULL value.

INTEGER. The value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.

REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.

TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).

BLOB. The value is a blob of data, stored exactly as it was input.
'''
# BEGIN database creation
# create table if it does not already exist, only columns headings
cursor.execute("""CREATE TABLE IF NOT EXISTS ships( 
                name TEXT, 
                speed_kph INTEGER,
                length_m REAL, 
                width_m REAL, 
                diameter_km REAL, 
                hyperdrive TEXT,
                type TEXT,
                manufacturer TEXT,
                weapon_count INT
                )""")
# First method used to import data simultaneously
# list comprised of tuples used to insert multiple rows of data into db
# raw data entered manually
# many_ships = [
#                 ('TIE Fighter', 1200, 7.2, 'NULL', 'NULL', 'None'),
#                 ('TIE Bomber', 850, 11.1, 'NULL', 'NULL', 'None'),
#                 ('TIE Advanced V1', 1600, 3.6, 'NULL', 'NULL', 'Class 4.5'),
#                 ('Special Forces TIE Fighter', 'NULL', 6.7, 'NULL', 'NULL', 'Class 2'),
#                 ('T-65 X-wing', 1050, 13.4, 'NULL', 'NULL', 'Class 1'),
#                 ('Delta-class T-3C Shuttle', 1000, 14.4, 'NULL', 'NULL', 'Class 1'),
#                 ('Slave 1', 1000, 21.5, 'NULL', 'NULL', 'Class 1'),
#                 ('Death Star', 'NULL', 'NULL', 'NULL', 160, 'Class 4'),
#                 ('Finalizer', 'NULL', 2916, 'NULL', 'NULL', 'Equipped'),
#                 ('Supremacy', 'NULL','NULL', 60542.68, 'NULL', 'Equipeed')
#              ]   

# insert statements -- row by row, specifying table
cursor.execute("INSERT INTO ships VALUES('TIE Fighter', 1200, 7.2, 'NULL', 'NULL', 'None','Starfighter', 'Sienar Fleet Systems',2)")
cursor.execute("INSERT INTO SHIPS VALUES('TIE Bomber', 850, 11.1, 'NULL', 'NULL', 'None','Bomber', 'Sienar Fleet Systems', 5)")
cursor.execute("INSERT INTO ships VALUES('Executor', 100, 19000, 'NULL', 'NULL', 'Class 1', 'Super Star Destroyer', 'Kuat Driver Yards', 5000 )")
cursor.execute("INSERT INTO ships VALUES('Libertine', 'NULL', 52.92, 'NULL', 'NULL', 'Equipped', 'Starship','Guild d Lanseaux', 'None')")
cursor.execute("INSERT INTO ships VALUES('T-65 X-wing', 1050, 13.4, 'NULL', 'NULL', 'Class 1', 'Starfighter', 'Income Corporation', 5)")
cursor.execute("INSERT INTO ships VALUES('Scimitar', 1180, 26.5, 'NULL', 'NULL', 'Class 2', 'Starship', 'Republic Sienar Systems', 7)")
cursor.execute("INSERT INTO ships VALUES('Slave 1', 1000, 21.5, 'NULL', 'NULL', 'Class 1','Pursuit Vessel', 'Kuat Systems Engineering', 5)")
cursor.execute("INSERT INTO ships VALUES('Death Star', 'NULL', 'NULL', 'NULL', 160, 'Class 4', 'Battle Station', 'Advanced Weapons Research', 20769)")
cursor.execute("INSERT INTO ships VALUES('Finalizer', 'NULL', 2916, 'NULL', 'NULL', 'Equipped','Star Destroyer', 'Kuat-Entralla Engineering', 6)")
cursor.execute("INSERT INTO ships VALUES('Supremacy', 'NULL','NULL', 60542.68, 'NULL', 'Equipeed','Star Dreadnought', 'Kuat-Entralla Engineering', 8000)")

# must use execute many in order to insert multiple rows of data into existing table
# cursor.executemany("INSERT INTO ships VALUES(?,?,?,?,?,?)", many_ships)

# cursor.execute("""CREATE TABLE IF NOT EXISTS builds(
#                   type TEXT,
#                   manufacturer TEXT,
#                   weapon_count INT,
#                   FOREIGN KEY(ship_id) REFERENCES ships(ship_id)
#                   )""")

# # raw data entered manually
# many_builds = [
#                 ('Starfighter', 'Sienar Fleet Systems', 2,1),
#                ('Bomber', 'Sienar Fleet Systems', 5, 2),
#                ('Starfighter', 'Sienar Fleet Systems', 3, 3),
#                ('Starfighter', 'Sienar-Jaemus Fleet Systems', 2, 4),
#                ('Starfighter', 'Income Corporation', 5,5),
#                ('Shuttle', 'Sienar Fleet Systems', 5,6),
#                ('Pursuit Vessel', 'Kuat Systems Engineering', 5,7),
#                ('Battle Station', 'Advanced Weapons Research', 20769,8),
#                ('Star Destroyer', 'Kuat-Entralla Engineering', 6,9),
#                ('Star Dreadnought', 'Kuat-Entralla Engineering', 8000,10)
#                ]

#cursor.execute("INSERT INTO builds VALUES('Starfighter', 'Sienar Fleet Systems', 2)")

#cursor.executemany("INSERT INTO builds VALUES(?,?,?,?)", many_builds)

connection.commit()

connection.close()

#END of database creation