#Global Variables
#Variables that are created outside of a function are known as global variables. 
#Global variables can be used by everyone, both inside of functions and outside. 
#And those can be accessed from anywhere in your code-including inside functions. 
#Why to use? -> you can share data between functions
#Useful for configiration settings, flags, or constants used throughout the program. 
#Example:

x = 10

def show(): #global variable
    print(x)

show()

#If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
#The global variable with the same name will remain as it was, global and with the original value. 

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)