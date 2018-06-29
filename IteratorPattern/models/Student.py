from models import Iterator

class Student():
    def __init__(self,name):
        self._name=name
    
    @property
    def Name(self):
        return self._name
    
    @staticmethod
    def GetIterator(student_ids):
        return StudentIterator(student_ids)
    
    @staticmethod
    def GetStudentById(id):
        #this is a mock of getting student from database
        return DBMock.GetStudent("Students",id)

class DBMock():
    """This is the mock database"""
    def __init__(self):
        self._db = ""
    
    @staticmethod
    def GetStudent(collection,id):
        return Student(collection+" "+str(id))

class StudentIterator(Iterator):
    #student_ids are the student ids array
    def __init__(self,student_ids):
        self._student_ids=student_ids
        self._position=-1
        
    def HasNext(self):
        if len(self._student_ids)<=self._position+1:
            return False
        else:
            return True
    
    def Next(self):
        self._position+=1
        return Student.GetStudentById(self._student_ids[self._position])


        