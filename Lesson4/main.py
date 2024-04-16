from teacher import Teacher
from student import Student
import logging


logging.basicConfig(filename='errors.log', level=logging.ERROR)

try:
    logging.debug("debug")
    logging.info("info")
    logging.warning("warning")
    logging.error("error")
    logging.critical("critical")
except Exception as e:
    logging.error(f"Помилка при логуванні: {e}")

try:
    andrii = Teacher("Andrii", 37, "PythonOOP", "teacher")
except Exception as e:
    logging.error(f"Помилка при створенні об'єкта Teacher: {e}")

try:
    yaroslav = Student("Yaroslav", 12.8, "SP2122", "student")
    oleksandr = Student("Oleksandr", 14.2, "SP2122", "student")
    denys = Student("Denys", 12.6, "SP2122", "student")
    dmytro = Student("Dmytro", 12.3, "SP2122", "student")
    kyrylo = Student("Kyrylo", 14.1, "SP2122", "student")
except Exception as e:
    logging.error(f"Помилка при створенні об'єктів Student: {e}")


humans = [yaroslav, oleksandr, denys, dmytro, kyrylo]

for human in humans:
    print(human)