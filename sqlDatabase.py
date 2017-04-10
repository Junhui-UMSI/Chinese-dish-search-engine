# -*- coding: utf-8 -*-

import sqlite3 as sql

def getFileID():
    totalID = []
    f = open('boRecipeTII\\validID.txt')
    lines = f.readlines()
    for line in lines:
        line = line.rstrip()
        fID = line
        totalID.append(fID)
    return totalID

IDlist = getFileID()

f = open('masterInstructions.txt')
lines = f.readlines()
f.close()

sqlite_file = 'sqlDB\\recipe_db.sqlite'
table_name1 = 'instructions'
new_field = 'Title'

conn = sql.connect(sqlite_file)
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS Instruction")
c.execute('CREATE TABLE Instruction (Title CHAR, rID INTEGER NOT NULL, Instructions CHAR)')

for id in IDlist[:10]:
    c.execute("INSERT INTO Instruction (rID, Instructions) VALUES (?, ?)", (id, lines[int(id)]))

conn.commit()
conn.close()
