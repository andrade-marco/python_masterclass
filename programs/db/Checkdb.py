import sqlite3

db = sqlite3.connect('contacts.sqlite')
cursor = db.cursor()

# Getting user input
print('----- SEARCH CONTACTS -----')
contact_name = input('Please enter the name of your contact: ')
query = 'SELECT * FROM contacts WHERE name LIKE ?'
query_tuple = tuple([contact_name])

cursor.execute(query, query_tuple)
print(cursor.fetchone())

db.close()
