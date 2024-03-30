'''
digit1 = int(input("Enter digit1: "))
digit2 = int(input("Enter digit2: "))
print(digit1/digit2)#ZeroDivisionError: division by zero
#1 BaseException
'''
'''
try:
    code
except:
    code
finally:
    code
'''
'''
try:
    digit1 = int(input("Enter digit1: "))
    digit2 = int(input("Enter digit2: "))
    print(digit1/digit2)#ZeroDivisionError: division by zero
except Exception as ex:
    print(ex)
finally:
    print("finally")
print("End")
#1 BaseException
'''
'''
try:
    code
except:
    code
finally:
    code
'''
'''
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
'''
from builderror import BuildError
from validator import Validator
limit = 7
amount = ''
try:
    amountStr = input("Enter amount: ")
    while(True):
        if(amountStr.isdigit()):
            amount = int(amountStr)
            break
        amountStr = input("Enter integer value for amount: ")
    Validator.Check(amount, limit)
except BuildError as be:
    print(be)
except Exception as ex:
    print(ex)
print("End")
