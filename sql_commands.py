# required library to work with relational databases
import sqlite3

# establish connection to database (.db file) -- in this case our database is created as 'string' 
connection = sqlite3.connect('db_02.db')
# initiate cursor to perform sql commands
cursor = connection.cursor()

# acceptable data types in sqlite3
'''
DATA TYPES

NULL. The value is a NULL value.

INTEGER. The value is a signed integer, stored in 0, 1, 2, 3, 4, 6, or 8 bytes depending on the magnitude of the value.

REAL. The value is a floating point value, stored as an 8-byte IEEE floating point number.

TEXT. The value is a text string, stored using the database encoding (UTF-8, UTF-16BE or UTF-16LE).

BLOB. The value is a blob of data, stored exactly as it was input.
'''

# function used to get name (column) using cursor
def entity_name(cursor):
    cursor.execute("SELECT name FROM ships")
    results = cursor.fetchall()
    if len(results) == 0:
        print("No names in database")
        return None
    for i in range(len(results)):
        print(f"{i+1} - {results[i][0]}")
        choice = 0
    while choice < 1 or choice > len(results):
        choice = int(input("Name ID: "))
    return results[choice-1][0]


def main():
    user_input = None

    # while loop to repeat menu to user until they quit the program
    while user_input != "6":
        print("1. Display Ships")
        print("2. Add Ship")
        print("3. Update Ship Information")
        print("4. Execute Aggregate Queries")
        print("5. Delete Ship")
        print("6. Quit")

        user_input = input(">> ")
        print()

        # runs a standard return all query on ships table
        if user_input == "1":
            cursor.execute("SELECT* FROM ships ORDER BY rowid ASC")
            print("{:>10}  \t\t{:>10}  \t\t{:>10}  \t\t{:>10}  \t\t{:>10} \t\t{:>10}  \t\t{:>10}  \t\t\t{:>10} \t\t{:<10}".format("Name", "Speed (kph)", "Length (m)", "Width (m)", "Diameter (km)", "Hyperdrive", "Weapon Count", "Type", "Manufacturer"))
            
            for record in cursor.fetchall():
                print("{:<10}  \t\t{:<10}  \t\t{:<10}  \t\t{:<10}  \t\t{:<10} \t\t{:<10}  \t\t{:<10}  \t\t\t{:>10} \t\t{:<10}".format(record[0], record[1],record[2], record[3],record[4], record[5], record[8], record[6], record[7]))
        # adds new ship to database
        elif user_input == "2":
            try:
                name = input("Name: ")
                speed = int(input("Speed (kph): "))
                length = float(input("Length (m): "))
                width = float(input("Width (m): "))
                diameter = float(input("Diameter (km): "))
                hyperdrive = input("Hyperdrive: ")
                weapons = int(input("Weapon Count: "))
                type = input("Type: ")
                manufacturer = input("Manufacturer: ")
                values = (name, speed, length, width, diameter, hyperdrive, weapons, type, manufacturer)
                cursor.execute("INSERT INTO ships VALUES(?,?,?,?,?,?,?,?,?)", values)
                # commit changes in order to save to database
                connection.commit()
            except ValueError:
                print("Invalid speed")
        # performs update operation to specified row of database
        elif user_input == "3":
            # print("1. Update Ship speed")
            # print("2. Update Ship model")
            # print("3. Update Ship hyperdrive")
            try:
                name = input("Name: ")
                type = input("Type: ")
                values = (type, name)
                cursor.execute("UPDATE ships SET type = ? WHERE name = ?", values)
                # commit changes in order to save to database
                connection.commit()
                if cursor.rowcount == 0:
                    print("Invalid name")
            except ValueError:
                print("Invalid type")
        # performs constructed aggregate queries
        elif user_input == "4":
            # aggregate function queries
            # AVG and SUM
            cursor.execute("SELECT AVG(DISTINCT speed_kph) 'Sum of speeds' FROM ships")

            query = cursor.fetchall()

            for i in query:
                print("Average ship speed: {:<10} kph".format(i[0]))

            cursor.execute("SELECT SUM(weapon_count) FROM ships")

            agg_one = cursor.fetchall()

            for i in agg_one:
                    print("Total weapon count: {:>10}".format(i[0]))
        # performs delete function to remove a row of data from table
        elif user_input == "5":
            name = entity_name(cursor)
            if name == None:
                continue
            values = (name, )
            cursor.execute("DELETE FROM ships WHERE name = ?", values)
            # commit changes in order to save to database
            connection.commit()
        print()

    # closes our connection to database safely
    connection.close()

if __name__ =="__main__":
    main()




