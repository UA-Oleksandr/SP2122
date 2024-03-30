#1 help()
from Lesson4.student import Student
from Lesson4.teacher import Teacher
from Lesson4.human import Human
#help(requests)
'''

r = requests.get('https://www.python.org')
print(r.status_code)#200
print(b'Python is a programming language' in r.content)

payload = dict(key1='value1', key2='value2')
r = requests.post('https://httpbin.org/post', data=payload)
print(r.text)
'''

# __name__, type(), dir()
'''
print(requests.__name__)
print(type(requests.Response()))
print(dir(requests.Response))
print(dir(requests.Response))
'''

#hasattr getattr
'''
print(hasattr(requests.Response, 'content'))
print(getattr(requests.Response, 'content', 'object has no attribute "content"'))
print(getattr(requests.Response, 'content1', 'object has no attribute "content1"'))
'''

#callable()
'''
def show(name:str):
    print(name)
name = "Andrii"
showFn = show(name)
print(callable(show))
print(callable(name))
print(callable(showFn))
'''
#5 issubssclass
class Human:
    pass

class Student(Human):
    pass
student = Student()
student = Student("name", 12.0, "SP2122", "student")
print(issubclass(Student, Human))
print(issubclass(Teacher, Human))
print(issubclass(student, Student))
print(issubclass(student, Teacher))

