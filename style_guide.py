#Python Styling Guide:
#first rule code layout: indentation,line lenght and blank lines
#First Rule: Code Layout
#1.Indentation:

def function():
    if True:
        print("Indentation True") #Correct

def function():
if True:
print("Indentation False") #Wrong

#2.Line Lenght:

def send_mail(subject,body,to_address):
    print(f"Sending email to {sudekucukoglu@gmail.com}") #Correct

def send_mail(subject,body,address):print(f"Sending email to {sudekucukoglu@gmail.com}") #Wrong

#3.Blank Lines:
def function_one():
    pass
                        #Correct
def function_two():
    pass

def function_three():
    pass
def function_four():    #Wrong
    pass


#Second Rule: Imports
#You have to impoert each library by itself
#And group them by origin(in order)
#Built-in modules first
#External libraries
#Your own modules or codes
import os
import sys
import requests         #Correct
import local_module


import os,sys
import local_module     #Wrong
import requests


#Third Rule: Continuation Lines
#Usage of parntheses for better readability
total = (
    var1
    + var2              #Correct
    + var3
)

total = (
    var1 + \
    var2 + \            #Wrong
    var3 + \
)

#Fourth Rule: Naming Conventions
#Variables and functions use only underscores with lower case
def sum_ages():
    ages_total = 55     #Correct

def SumAges():
    AgesTotal = 55      #Wrong(PascalCase not used for functions or variables)

#Classes use capitalized words
class StudentDetails:
    pass                #Correct              

class student_details:
    pass                #Wrong(Class names should be in PascalCase)


#Fifth Rule: Whitespace
#No spaces before commas, colons, or semicolons
#Always put one space after a comma
x = 5
y = x + 2               #Correct
print(x, y)

x=5
y=x+2
print( x , y )          #Wrong(Too many unnecessary spaces)


#Sixth Rule: Comments
#Use complete sentences
#For Block comments, use them above code blocks, indented to the same level
#For Inline comments, use sparingly, and start with a # and a space
#This function greets the user
def greet():
    print("Hello!")     #Correct

def greet(): #greet
    print("Hello!") #hello  #Wrong


#Seventh Rule: Docstrings
#For Docstrings, use triple quotes """ for module, class, and function documentation
def add(x, y):
    """Returns the sum of x and y."""       #Correct
    return x + y

def add(x, y):
    #Adds two numbers           #Wrong
    return x + y


#Eighth Rule: Comparing to None
#Since is checks the identity, it checks if two variables refer to the exact same object
# == checks for value equality, which can be overrideden with custom logic and also can give unexpected result
if result is None:
    print("No result")      #Correct

if result == None:
    print("No result")      #Wrong


#Nineth Rule: Exception Handling
#It allows us to deal with errors that occur during runtime
#Lİke; Dividing by Zero, Accessing a missing file, Calling a function with invalid input
try:
    value = 10 / 0
except ZeroDivisionError:           #Correct
    print("Cannot divide by zero")

try:
    value = 10 / 0
except:                     
    print("Error")                  #Wrong(Too broad, catches everything)


#Tenth Rule: Lambda Usage
#It is used when you need a simple function for a short period of time, usually as an argument to another function
#It is not suitable for complicated function like mathematical problems
def square(x):              #Correct
    return x * x

square = lambda x: x * x    #Wrong(Avoid for anything more than a simple one-liner)


#Eleventh Rule: Main Function Block(Extra)
#Some Python files can be run directly, or imported into other files
#So it ensures that some code only runs when the file is executed directly, not when it's imported
#It keeps the code clean and modular
#Makes the script safe to import without running everything
def main():
    print("Hello!")
                                #Correct
if __name__ == "__main__":
    main()

print("Hello!")     #Wrong(No main function structure)