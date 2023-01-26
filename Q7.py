class Student:
    pass
class Marks:
    pass
a = Marks()
b = Student()

print(isinstance(b, Student))
print(isinstance(a, Student))
print(isinstance(a, Marks)) 
print(isinstance(b, Marks))
print("\nCheck whether the said classes are subclasses of the built-in object class or not.")
print(issubclass(Student, object))
print(issubclass(Marks, object))