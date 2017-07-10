# Greenshoe_Database_ActiveMQ

Ensure you have python 2 and pip installed.

Delete greenshoe.csv, greenshoe.db, greenshoeCG.csv and greenshoenotCG.csv before starting.

### File 1

generatecsv.py generates letters randomly from "A","C","G" or "T" randomly and writes them to a CSV file containing 12 columns and 100 rows

To run it, open the terminal, navigate to the folder containing the project files and run "**python generatecsv.py**". 
A file greenshoe.csv will be created in the working directory. If the file did not exist before, it will be created and if it existed before it will be recreated with the updated information.


### File 2

create_database.py creates the database used to save rows with 5th column as either "C" or "G"

To run it, open the terminal, navigate to the folder containing the project files and run "**python create_database.py**". 
A file "greenshoe.db" will be created in the working directory if it did not exist before or else an error will be raised - sqlite3.OperationalError: table CSVCG already exists.


### File 3

differentiate.py opens and reads a CSV file - greenshoe.csv -. The program processes each line and if the value column 5 in the file has the value “C”or “G” the entire row is inserted into an sqlite database - greenshoe.db - created by File 2.
If the value in column 5 is anything other than “C” or “G” then the entire row is inserted as a JSON object into an Apache ActiveMQ queue. 
The program reads the csv file name , queue name, ActiveMQ Username and password as a command line parameter. 

To run it, open the terminal, navigate to the folder containing the project files and run "**pip install stomp.py**" followed by "**python differentiate.py greenshoe.csv --queue name-- --username-- --password--**". 


### File 4

write_differentiated.py connects to the database created by File 2 and updated by File 3 above and then reads the rows stored there and writes them to a CSV file - greenshoeCG.csv.
It also connects to the ActiveMQ queue and read the data contained therein and write them to a separate CSV file.

To run it, open the terminal, navigate to the folder containing the project files and run "**pip install stomp.py**" followed by "**python write_differentiated.py --queue name-- --username-- --password--**".

File "greenshoeCG.csv" and "greenshoenotCG.csv" will be created in the working directory. If the files did not exist before, they will be created and if they existed before they will be recreated with the updated information.






