#F Strings
#To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets as placeholders for variables and other operations. 
age = 22
txt = f"My name is Sude, I am {age}"
print(txt)

#Placeholders and Modifiers
#A placeholder can contain variables, operations, functions, and modifiers to format the value. 
price = 59
txt = f"The price is {price} dollars"
print(txt)

#A placeholder can include a modifier to format the value. 
#A modifier is included by adding a colon(:) followed by a legal formatting type, like .2f which means fixed point number with 2 decimals. 
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)