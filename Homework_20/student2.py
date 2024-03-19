class Student(object):

    def __init__(self, name:str, age:float, money:int, rest:float):
        self.Name:str = name
        self.Age:float = age
        self.Money:int = money
        self.Rest:float = rest

    def __str__(self):
        return (f"Name: {self.Name}\n"
                f"Age: {self.Age}\n"
                f"Money: {self.Money}\n"
                f"Rest: {self.Rest}\n")