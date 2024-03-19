from humanrole import HumanRole
from human import Human
from autotype import Autotype

class Auto:
    def __init__(self, model:str, type:Autotype):
        self.Model:str = model
        self.Type:Autotype = type
        self.Passengers:list = list()
        self.Drivers:list = list()
    def AddPassenger(self, human:Human):
        if(isinstance(self.Drivers, list) and human.Role == HumanRole.PASSENGER):
            self.Passengers.append(human)
    def AddDriver(self, human:Human):
        if(isinstance(self.Drivers, list) and human.Role == HumanRole.DRIVER):
            self.Drivers.append(human)
    def __str__(self):
        drivers:str = ''
        passengers:str = ''
        for driver in self.Drivers:
            drivers += str(driver)
        for passenger in self.Passengers:
            passengers += str(passenger)
        return (f"Drivers:\n{drivers}\n"
                f"Passengers:\n{passengers}")
