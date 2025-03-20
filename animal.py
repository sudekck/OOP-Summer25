print("Animals of the Zoo:")
animals={ "name": ["Elephant", "Giraffe", "Crocodile", "Snake"],
    "group":["Mammals", "Mammals", "Reptiles", "Reptiles"],
    "number_of_legs":[4,4,4,0],
    "skills":["Heavy", "Tall", "Amfibia", "Poisonous"]}

print(animals["name"])
print(animals["group"])
print(animals["number_of_legs"])
print(animals["skills"])

animal1={"name":"Elephant,", "group":"Mammals,", "number_of_legs": "4,", "skills": "Heavy"}
animal2={"name":"Giraffe,", "group": "Mammals,", "number_of_legs": "4", "skills": "Tall"}
animal3={"name":"Crocodile,", "group":"Reptiles,", "number_of_legs": "4", "skills": "Amfibia"}
animal4={"name":"Snake,", "group": "Reptiles,", "number_of_legs": "0,", "skills": "Poisonous"}
animal5={"name":"Tiger,", "group":"Mammals,", "number_of_legs":"4,", "skills": "Strong"}
print("Animals of the Zoo")
print(animal1["name"],animal1["group"],animal1["number_of_legs"],animal1["skills"])
print(animal2["name"],animal2["group"],animal2["number_of_legs"],animal2["skills"])
print(animal3["name"],animal3["group"],animal3["number_of_legs"],animal3["skills"])
print(animal4["name"],animal4["group"],animal4["number_of_legs"],animal4["skills"])
print(animal5["name"],animal5["group"],animal5["number_of_legs"],animal5["skills"])