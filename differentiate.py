import sys  
import os  
import logging 
# run "pip install stomp.py" to successfully import it 
import stomp  
import time  
import json 

filename = sys.argv[1]
#Opens or creates a file, greenshoe.csv, for reading only
f = open(filename,"r").readlines()
#creates a nested list of the contents gotten from the database with each row as a sub-list in the list 
k=[list(each) for each in f]
#Eliminates the separator, piped character in the sub-lists 
k=[each[0::2] for each in k]
#Eliminates "\n" in the sub-lists
k=[each[0:-1] for each in k]
#Checks if a the fifth character in every sub-list(row) is a C or G. If it is, a new list, Database, is created to hold these sub-lists.
Database = [each for each in k if each[4]=="C" or each[4]=="G"]
#Checks if a the fifth character in every sub-list(row) is not a C or G. If it is not, a new list, ActiveMQ, is created to hold these sub-lists.
ActiveMQ = [each for each in k if each[4]=="A" or each[4]=="T"]

import sqlite3


#connects to a sqlite database(file), greenshoe.db, if it exists or creates it
conn = sqlite3.connect('greenshoe.db')
print "Opened database successfully";

#Loops through the list and for each value in the sub-list, it is inserted to the database in a column. Each sub-list is the same as each record
for each in Database:
    conn.execute("INSERT INTO CSVCG (C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12) \
    VALUES ('" + each[0] + "', '" + each[1] + "', '" + each[2] + "', '" + each[3] + "', '" + each[4] + "', '" + each[5] + "', '" + each[6] + "', '" + each[7] + "', '" + each[8] + "', '" + each[9] + "', '" + each[10] + "', '" + each[11] + "')");

#Make the changes requested
conn.commit()
print "Records created successfully";
#close the connection to the database after creating the table
conn.close()


queuename = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
logging.basicConfig(level=logging.DEBUG)  
start = time.time()  
  
conn = stomp.Connection([('0.0.0.0', 61613)])  
conn.start()  
conn.connect(wait=True, username=username, passcode=password)  
  
for i in ActiveMQ: 
    msg = {'cv1':i[0],'cv2':i[1],'cv3':i[2],'cv4':i[3],'cv5':i[4],'cv6':i[5],'cv7':i[6],'cv8':i[7],'cv9':i[8],'cv10':i[9],'cv11':i[10],'cv12':i[11]}  
    conn.send(body=json.dumps(msg), destination='/queue/'+queuename)  
    print "send one"  
  
conn.disconnect()  
print "OK Finished msgs time %f" % ((time.time()-start)) 



 
