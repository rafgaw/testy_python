import sqlite3
sql_connection = None
try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    insert = '''
    INSERT INTO software (id, name, price) VALUES(1,'PYTHON', 200)
    '''
    select = '''
    SELECT * FROM software
    '''
    cursor = sql_connection.cursor()
    print("Baza danych podłączona")
    # cursor.execute(insert)
    # sql_connection.commit()
    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 200.0)
except sqlite3.Error as e:
    print("Błąd podczas otwierania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")
