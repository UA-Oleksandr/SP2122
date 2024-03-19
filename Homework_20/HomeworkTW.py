import time
from student2 import Student
from validator import Validator
import random

georgiy = Student(name="Georgiy", age=16.9, money=5000, rest=1)
andrew = Student(name="Andrew", age=16.9, money=2500, rest=2)
maxim = Student(name="Maxim", age=14.6, money=1500, rest=1)
egor = Student(name="Egor", age=14.8, money=1200, rest=3)
oleksandr = Student(name="Oleksandr", age=14.2, money=2500, rest=1)
students = [georgiy, andrew, maxim, egor, oleksandr]
students_with_high_rest = []
students_with_normal_rest = []



#days = 366
#              0   1    2    3
#vacations = [14, 182, 244, 350]
#if  student2.Money < 2000
#     and ((x>=vacations[1] and x>=vacations[2]) or (x<=vacations[0] and x>=vacations[3])):
#while(day > 0):
#   day-=1
validator = Validator("")
for student2 in students:
    print(f"Name: {student2.Name}\n"
          f"Age: {student2.Age}\n"
          f"Money: {student2.Money}\n"
          f"Rest: {student2.Rest}\n")
    if student2.Money < 2000:
        print(f"{student2.Name} needs to go to the work.")
        print(f"Send {student2.Name} to the work?")
        validator.validation()
        if validator.Yes.lower() == 'y':
            print(f"{student2.Name} went to his work. {student2.Name} will claim his day sallary after his work.")
            print(f"{student2.Name} claims his sallary.", end="")
            time.sleep(2)
            print(".", end="")
            time.sleep(2)
            print(".", end="")
            time.sleep(2)
            print(".", end="")
            print(f"{student2.Name} claimed his sallary, 900 $.")
            student2.Money += 900
        else:
            print(f"{student2.Name} didn't go to his work. He won't claim his day sallary.")

    if student2.Rest > 3:
        print(f"{student2.Name} won't rest.")
        students_with_high_rest.append(student2)

    if student2.Rest < 3:
        students_with_normal_rest.append(student2)

print(f"Boys want to play rulette.")
for student2 in students_with_normal_rest:
    r = random.randint(1, 2)
    if r == 2:
        print(f"{student2.Name} won 100 $")
        student2.Money += 100
    if r == 1:
        print(f"{student2.Name} lost 100 $.")
        student2.Money -= 100