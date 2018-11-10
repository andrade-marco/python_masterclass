import sqlite3

db = sqlite3.connect('contacts.sqlite')
cursor = db.cursor()

# Creating table and adding data
db.execute('CREATE TABLE IF NOT EXISTS contacts(name TEXT, phone INTEGER, email TEXT)')
db.execute('INSERT INTO contacts(name, phone, email) VALUES("Tim", 4168479898, "tim@test.com")')
db.execute('INSERT INTO contacts VALUES("Brian", 6473348976, "brian@test.com")')

# Queries
cursor.execute('SELECT * FROM contacts')
print(cursor.fetchall())

for row in cursor:
    print(row)

print('-' * 40)

cursor.execute('SELECT * FROM contacts')
for name, phone, email in cursor:
    print('{:6} | {:10} | {}'.format(name, phone, email))

cursor.close()
db.commit()
db.close()
