# Demonstrates iterating over a list of dict objects
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

def search(name):
    for student in students:
        for key in student:
            if student[key] == name:
                print(f'{name} has been Founded')
                return
    print(f'{name} has not been founded' )

search('Harry')
