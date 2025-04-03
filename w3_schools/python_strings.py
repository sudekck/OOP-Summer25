#Strings in python are surrounded by either single quotation marks, or double quotation marks. 
#Strings are Arrays:
#This means you can access individual characters in a string using indexing. 
text = "hello"
print(text[0]) #output: h
print(text[1]) #output: e

#Looping Through a String
#Since strings are arrays, we can loop through the characters in a string, with a for loop. 
for x in "banana":
    print(x)
#String Lenght
#To get the lenght of a string, use the len() function. 
a = "Hello, world!"
print(len(a))

#Check String
#To check if a certain phrase or character is present in a string, we can use the keyword in. 
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

#Check if NOT
#To check if a certain phrase or character is not present in a string, we can use the keyword not in. 
txt = "The best things in life are free!"
print("expensive" not in txt)
