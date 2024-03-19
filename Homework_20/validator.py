class Validator:
    def __init__(self, yes: str):
        self.Yes = yes
    def validation(self):
        self.Yes = input(f"- y or n - ")
        while (True):
            if (self.Yes.lower() == "y" or self.Yes.lower() == "n"):
                break
            self.Yes = input("Your input is not correct. Please write a correct  one. - ")