

import sqlite3

# creating database
conn = sqlite3.connect('assignment.db')

# open connection, create table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT,\
                txt_files TEXT)")
    conn.commit()

# list
fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg')

# identify .txt suffix with loop
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # insert 1 .txt suffix into one row
            cur.execute("INSERT INTO tbl_files (txt_files) VALUES (?)", (x,))
            print(x)
conn.close()
