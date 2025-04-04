 #-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#
# HIGA_IO.v2.py shows how to do various kinds of input and output operations in python.
# Demonstrates persistence, which means that the data collected in the program can exist after the program stops running
#
# Created by Scott Higa, 2025-03-02
# Last edit: 2025-03-04
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

var1 = input("what year were you born in? ")
### The prompt "What year were you born in?" will appear on the console and ask the user for an input.  We are setting this input to the variable, var1.
### print (type(var1))

var2 = str(2025 - int(var1))
### The input response from the user (var1) will be saved as a string by default.  But in order to calculate age, we must subtract the input from an int value, 2025 (the current year).  Therefore, we need to convert the input to an int for the subtraction step.  Since int/floats cannot be written to .txt, we must convert the difference back to a string before appending or writing it to a .txt.

print ("you must be",(var2),"years old!")
### This will print the users estimated age to the console based on the subtraction operation in the previous step.

outfile = open("outfile.txt", "w")
### Opening outfile.txt in write mode, "w".  This will overwrite any existing text in outfile.txt and replace it.

outfile.write("born in " + var1 + ", " )
### Write var1 (string) into outfile.txt
### Adding in some other text strings to make data easier to read

outfile.close()
### Close outfile.txt. We need to close the file after each "w" or "a"

outfile = open("outfile.txt","a")
### Opening outfile.txt in append mode

outfile.write("age: "+ var2 + ", ")
### Write var2 (string) into outfile.txt.  This time, since outfile.txt has been opened in append mode, the text from var 1 will not be erased and text from var2 will be added after the text from var1 into outfile.txt
### Adding in some other text strings to make data easier to read

outfile.close()
### Close outfile.txt

var3 = input("what is your favorite color? ")
### After the user gives first answer, var1, a second prompt "What is your favorite color? " will appear on the console.  Since the input that we are expecting is a string, there is no need to change variables.  We are setting this input to the variable, var 3.

outfile = open("outfile.txt","a")
### Opening outfile.txt in append mode

outfile.write("favorite color: " + var3)
### Write var3 into outfile.txt
### Adding in some other text strings to make data easier to read

outfile.close()  ### Close outfile.txt

print ("")
print ("Thanks!")

### .csv is like a .txt but it can be used to store data as (comma seperated varriables), useful with .exe.