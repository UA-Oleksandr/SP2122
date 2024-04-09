from logging import *
'''
debug("DEBUG")
info("DEBUG")
warning("DEBUG")
error("DEBUG")
critical("DEBUG")
'''
from logger import Logger
customLogger = Logger(__name__, level=ERROR)
try:
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    print(digit1/digit2)
except TypeError as te:
    print(f'TE: {te}')
except ZeroDivisionError as zde:
    print(f'ZDE: {zde}')
except Exception as ex:
    print(f'EX: {ex}')
print("End")