from auto import *

humans = list()
yaroslav = Human("Yaroslav", HumanRole.PASSENGER)
oleksandr = Human("Oleksandr", HumanRole.PASSENGER)
denys = Human("Denys", HumanRole.PASSENGER)
dmytro = Human("Dmytro", HumanRole.PASSENGER)
kyrylo = Human("Kyrylo", HumanRole.PASSENGER)
for human in yaroslav, oleksandr, denys, dmytro, kyrylo:
    humans.append(human)

bmw = Auto("X7", Autotype.CAR)
for Human in humans:
    bmw.AddDriver(human)
    bmw.AddPassenger(human)

print(bmw)
