import random

class Chisl(object):
    def __init__(self, chisll: list):
        self.Chislll = chisll


m_chisl = Chisl(chisll=[10, 20, 30, 40, 50])

asciiP = ""


for number in m_chisl.Chislll:
    r = random.randint(0, 9)
    asciiP += chr(r)

print("Шифр:", asciiP)
