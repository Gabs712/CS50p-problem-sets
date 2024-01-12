students = []
  #comment
#comment
with open("students0.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {'name': name, 'house': house}
        students.append(student)


for student in sorted(students, key=lambda x: x['name']):
    print(f"{student['name']} is in {student['house']}")