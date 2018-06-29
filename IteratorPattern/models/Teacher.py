from models import Iterator

class Teacher():
    def __init__(self,name):
        self._name=name
    
    @property
    def Name(self):
        return self._name
    
    @staticmethod
    def GetIterator(teachers):
        #teachers is the teacher array
        return TeacherIterator(teachers)


class TeacherIterator(Iterator):
    #teachers are the teacher dict
    def __init__(self,teachers):
        self._teachers=teachers
        self._position=-1
        
    def HasNext(self):
        if len(self._teachers)<=self._position+1:
            return False
        else:
            return True
    
    def Next(self):
        self._position+=1
        return self._teachers[self._position]
        