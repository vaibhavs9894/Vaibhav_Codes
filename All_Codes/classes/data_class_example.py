# when no using data classes
class Student:
   
    def __init__(self,name,age,college,cls,section,gender):
        self.name = name
        self.age = age
        self.college = college
        self.cls = cls
        self.section = section
        self.gender = gender

from dataclasses import dataclass

@dataclass
class StudentV2:
    name: str
    age: int
    college: str
    cls:str
    section:str
    gender:str

@dataclass
class Marks:
    student: StudentV2
    total : int


if __name__ == "__main__":
    s1 = Student('ajay',12,'AKPMDS','7th','B','male')
    s2 = Student('rani',12,'JDASJ','7th','A','female')
    s3 = StudentV2('raju',16,'AKP','11th','D',"male")
    print(s1.name)
    print(s2.name)
    print(s1.cls)
    print(s2.cls)
    print(s3.name)
    print(s3.cls)
    print(s3)

    m = Marks(s3,77)
    print(m)