student1 ={
    "first_name": "Sude",
    "last_name": "Kucukoglu",
    "index_number": "34783",
    "nationality": "Turkish",
    "starting_date": "13/09/2024",
    "courses": ["Basics of Cs"]
}
print(student1["first_name"])
print(student1["last_name"])
print(student1["index_number"])
print(student1["nationality"])
print(student1["starting_date"])
print(student1["courses"])

student2 ={
    "first_name": "Ali",
    "last_name" : "Cankar",
    "index_number": "34657",
    "nationality": "Turkish",
    "starting_date": "13/09/2025",
    "courses": ["Economics", "Mathematics"]
}
print(student2["first_name"])
print(student2["last_name"])
print(student2["index_number"])
print(student2["nationality"])
print(student2["starting_date"])
print(student2["courses"])


student3 ={
    "first_name": "Janny",
    "last_name" : "Christina",
    "index_number": "67489",
    "nationality": "American",
    "starting_date": "13/09/2023",
    "courses": ["Basics of Digital Marketing"]
}
print(student3["first_name"])
print(student3["last_name"])
print(student3["index_number"])
print(student3["nationality"])
print(student3["starting_date"])
print(student3["courses"])

def add_new_students(first_name, last_name, index_number, nationality, starting_date, courses):
    student = {'first_name': first_name, 'last_name': last_name, 'index_number':index_number, 'nationality':nationality, 'starting_date':starting_date,'courses':courses}
    students.append(student)
    print(first_name + " " + last_name + " " + index_number + " " + nationality + " " + starting_date + " " + courses)