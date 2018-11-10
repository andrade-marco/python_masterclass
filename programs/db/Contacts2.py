import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_email = 'brian@update.com'
target_name = 'Brian'

update_sql = 'UPDATE contacts SET email= ? WHERE name= ?'
update_cursor = db.cursor()
update_cursor.execute(update_sql, (new_email, target_name))
print('{} rows updated'.format(update_cursor.rowcount))

update_cursor.connection.commit()
update_cursor.close()

for row in db.execute('SELECT * FROM contacts'):
    print(row)

db.close()
