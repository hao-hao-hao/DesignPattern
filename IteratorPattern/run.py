from models import Student
from models import Teacher

class Helper():
    def __init__(self):
        pass
    @staticmethod
    def PrintAllNames(iterators):
        while iterators.HasNext():
            item = iterators.Next()
            print("The name is "+item.Name)

student_ids = [3,5,1,9,8]
teachers = [Teacher("teacher a"),Teacher("teacher b"),Teacher("teacher c"),Teacher("teacher d"),Teacher("teacher e")]

#This is the student iterator to iterate the database
studentsIterator = Student.GetIterator(student_ids)
#This is the teach iterator to iterate the teachers object itself
teachersIterator = Teacher.GetIterator(teachers)


Helper.PrintAllNames(studentsIterator)
#outputs:
#The name is Students 5
#The name is Students 3
#The name is Students 1
#The name is Students 9
#The name is Students 8

Helper.PrintAllNames(teachersIterator)
#outputs:
#The name is teacher a
#The name is teacher b
#The name is teacher c
#The name is teacher d
#The name is teacher e