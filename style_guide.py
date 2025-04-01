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

