import random
#Empty list that will hold the generated Characters
generated_characters=[]
#loop through 100 to generate 100 rows
for each in range(100):
    #Generate characters for each row
    generated_characters.append(" ".join(random.choice("AGCT") for each in range(12)))

#Opens or creates a file, greenshoe.csv, for writing only
f=open("greenshoe.csv","w")


if f:
    #loops though each item of the list 
    for each in generated_characters:
        #splits the string that has characters that should be inserted into the file above as rows
        for eac in each.split(" "):
            #write to the file the value of each column followed by a separator, pipe character
            f.write(eac + "|")
        #moves to the next row
        f.write("\n")
 
#closes the file after writing to it
f.close()
