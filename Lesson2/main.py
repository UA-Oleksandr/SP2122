from student import Student
yaroslav = Student("Yaroslav", age=12.8, group="SP2122")
oleksandr = Student(name="Olekdandr", age=14.2, group="SP2122")
denys = Student(name="Denys", age=12.8, group="SP2122")
kyrylo = Student(name="Kyrylo", age=14.1, group="SP2122")
#students = [yaroslav, oleksandr, denys, kyrylo]
students = list()
students.append(yaroslav)
students.append(oleksandr)
students.append(denys)
students.append(kyrylo)
for student in students:
    print(f"Name: {student.Name}\n"
          f"Age: {student.Age}\n"
          f"Group: {student.Group}\n")
print("Hello World!\nEnd:)")