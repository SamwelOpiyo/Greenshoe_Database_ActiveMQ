import sqlite3

#connect to a sqlite database(file)
conn = sqlite3.connect('greenshoe.db')
print "Opened database successfully";

#creating table CSVCG with 12 columns that will hold the 12 columns of the csv file
#Each column will hold an integer value and cannot be null
#rowid is autogenerated for us
conn.execute('''CREATE TABLE CSVCG
         (C1       CHAR(1)    NOT NULL,
         C2       CHAR(1)    NOT NULL,
         C3       CHAR(1)    NOT NULL,
         C4       CHAR(1)    NOT NULL,
         C5       CHAR(1)    NOT NULL,
         C6       CHAR(1)    NOT NULL,
         C7       CHAR(1)    NOT NULL,
         C8       CHAR(1)    NOT NULL,
         C9       CHAR(1)    NOT NULL,
	 C10      CHAR(1)    NOT NULL,
         C11      CHAR(1)    NOT NULL,
         C12      CHAR(1)    NOT NULL);''')

print "Table created successfully";

#close the connection to the database after creating the table
conn.close()