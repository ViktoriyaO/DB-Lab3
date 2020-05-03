import csv
import cx_Oracle

username = 'viktoriya'
password = 'viktoriya'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

tables = ['Diamond', 'Description', 'Category', 'Clarity']
for table in tables:
    with open(table + '.csv', 'w', newline = '') as csvfile:
        cursor.execute('SELECT * FROM ' + table)
        row = cursor.fetchone()
        writeCSV = csv.writer(csvfile, delimiter=',')

        while row:
            writeCSV.writerow(row)
            row = cursor.fetchone()

cursor.close()
connection.close()