import csv
import cx_Oracle

username = 'viktoriya'
password = 'viktoriya'
database = 'localhost:1521/xe'
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

csvfile = open('diamonds.csv', errors='ignore')
readCSV = csv.reader(csvfile, delimiter=',')
row_num = 1

color_unique = []
cut_unique = []
clarity_unique = []

tables = ['Diamond', 'Description', 'Category', 'Clarity']
for table in tables:
    cursor.execute("DELETE FROM " + table)

try:
    for row in readCSV:
        diamond_index = row[0]
        color = row[3]
        cut = row[2]
        clarity = row[4]
        carat_weight = row[1]

        if color not in color_unique:
            color_unique.append(color)
            query = '''INSERT INTO Description(color) VALUES(:color)'''
            cursor.execute(query, color=color)

        if cut not in cut_unique:
            cut_unique.append(cut)
            query = '''INSERT INTO Category(cut) VALUES(:cut)'''
            cursor.execute(query, cut=cut)

        if clarity not in clarity_unique:
            clarity_unique.append(clarity)
            query = '''INSERT INTO Clarity(clarity) VALUES(:clarity)'''
            cursor.execute(query, clarity=clarity)

        query = '''
        INSERT INTO Diamond(diamond_index, color, cut, clarity, carat_weight) 
            VALUES(:diamond_index, :color, :cut, :clarity, :carat_weight)'''
        cursor.execute(query, diamond_index=diamond_index, color=color, cut=cut,
                    clarity=clarity, carat_weight=carat_weight)

    row_num += 1

except:
    print(f'Error of the row {row_num}')
    raise

finally:
    csvfile.close()
    connection.commit()
    cursor.close()
    connection.close()


