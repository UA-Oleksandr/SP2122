result = []
def divider(a, b):
   if a < b:
       raise ValueError(f"{a}<{b}")
   if b > 100:
       raise IndexError(f"{b}>{100}")
   return a/b
data = {10: 2, 2: 5, "123": 4, 18: 0, 30:15, 8 : 4, 102:101}
for key in data:
   try:
       res=divider(key, data[key])
       result.append(res)
   except ValueError as ve:
       print(f"[ValueError]: {ve}")
   except IndexError as ie:
       print(f"[IndexError]: {ie}")
   except ZeroDivisionError as zde:
       print(f"[ZeroDivisionError]: {zde}")
   except Exception as ex:
       print(f"[Exception]: {ex}")
print(result)