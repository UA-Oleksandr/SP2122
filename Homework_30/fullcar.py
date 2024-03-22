from carspace import CarSpace
from carcompleset import CarCompleSet

class FullCar(CarSpace, CarCompleSet):
    def __init__(self, sits:int, trunk:int, brand:str, engine:float, format:str):
        CarSpace.__init__(self, sits, trunk)
        CarCompleSet.__init__(self, brand, engine, format)


    def __str__(self):
        return (f"Sits: {self.Sits}\n"
                f"Trunk: {self.Trunk}\n"
                f"Brand: {self.Brand}\n"
                f"Engine: {self.Engine}\n"
                f"Format: {self.Format}")