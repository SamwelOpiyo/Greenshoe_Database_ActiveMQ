import sys  
import os  
import logging  
import stomp  
import json  
import time


import sqlite3

#connects to a sqlite database(file), greenshoe.db, if it exists or creates it
conn = sqlite3.connect('greenshoe.db')
print "Opened database successfully";

#reads the records in the database
cursor = conn.execute("SELECT ROWID, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12 from CSVCG")
#loops through the cursor
for record in cursor:
    #Prints Field and its value for a record
    print "ID = ", record[0]
    print "C1 = ", record[1]
    print "C2 = ", record[2]
    print "C3 = ", record[3]
    print "C4 = ", record[4]
    print "C5 = ", record[5]
    print "C6 = ", record[6]
    print "C7 = ", record[7]
    print "C8 = ", record[8]
    print "C9 = ", record[9]
    print "C10 = ", record[10]
    print "C11 = ", record[11]
    print "C12 = ", record[12], "\n"

#reads the records in the database
cursor = conn.execute("SELECT ROWID, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12 from CSVCG")

#Opens or creates a file, greenshoeCG.csv, for writing only and stores values that were stored in the database
f=open("greenshoeCG.csv","w")


if f:
    #loops though each cursor 
    for record in cursor:
        #loops through each record in the list leaving out the rowid
        for field in range(1,len(record)):
            #write to the file the value of each field followed by a separator, pipe character
            f.write(record[field] + "|")
        #moves to the next record
        f.write("\n")

#closes the file after writing to it
f.close()

print "Operation done successfully";
#close the connection to the database after writing to the table
conn.close()




class MyListener(object):  
    def on_error(self, headers, message):  
        print 'received an error %s' % message  
      
    def on_message(self, headers, message): 
        print headers
        print str(message)
        print type(message)
        print 'received a message ...%s...' % message 
        msg = json.loads(message)  
#       print headers['message-id']  
#       sys.exit(0)  
        conn.ack({'message-id':headers['message-id']}) 
        #Opens or creates a file, greenshoeCG.csv, for writing only and stores values that were stored in the database
        #Opens or creates a file, greenshoeCG.csv, for writing only and stores values that were stored in the database
	f=open("greenshoeCG.csv","w")


	if f:
    	    for key,value in msg:
                #write to the file the value of each field followed by a separator, pipe character
            	f.write(value + "|")
            #moves to the next record
            f.write("\n")

	#closes the file after writing to it
	f.close()

queuename = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
logging.basicConfig(level=logging.DEBUG)  
  
conn = stomp.Connection([('0.0.0.0', 61612)])  
conn.set_listener('', MyListener())  
conn.start()  
conn.connect(wait=True, username=username, passcode=password)  
conn.subscribe(destination='/queue/'+queuename, ack='auto')  
      
while True:  
    try:  
        time.sleep(1)  
    except:  
        break

conn.disconnect()







      
      
      
 

 


