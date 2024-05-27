import urllib.request, urllib.error
import re
import sqlite3

connection = sqlite3.connect("../databases/count_org.sqlite")
cursor = connection.cursor()

def input_file(max_attempts = 3):
    '''Limiting the number of failed urls to 3 to break out of app if can't enter
    '''
    fail_count = 0
    while fail_count < max_attempts:
        try:
            file = open(input('Enter file name:'))
            return file
        except:
            print("Can't open the file")
            fail_count +=1
    return None


file = input_file()

def clear_db():
    cursor.execute('DELETE FROM Counts')
    connection.commit()

def parse_file(file):
    global cursor
    count = 0
    clear_db()
    if file is not None:
        for line in file:
            if line.startswith("From:") and "@" in line:
                line_parts = line.split()
                for part in line_parts:
                    if "@" in part:
                        email_parts = part.split("@")
                        domain = email_parts[1]
                        cursor.execute('SELECT Org FROM Counts WHERE Org = ?', (domain,))
                        domain_is_present = cursor.fetchone()
                        if domain_is_present is None:
                            cursor.execute('''
                            INSERT INTO Counts (org, count) VALUES (?, 1)
                            ''', (domain,))
                        else:
                            cursor.execute('''UPDATE Counts SET Count = Count + 1 
                                           WHERE Org = ? ''', (domain,))

        # Commit the transaction       
        connection.commit()
parse_file(file)

# Close the cursor and connection
cursor.close()
connection.close()