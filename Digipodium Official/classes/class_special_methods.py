class Student:

    def __init__(self, name, cls, marks):
        self.name = name
        self.cls = cls
        self.marks = marks

    def show(self):
        print("name  =>",self.name)
        print(" cls  =>",self.cls)
        print("marks =>",self.marks)

    # convert object to string when printed
    def __str__(self):
        return f"{self.name} in {self.cls}"

    def __gt__(self,other):
        return self.marks > other.marks

    def __repr__(self):
        return self.name

    def __add__(self,other):
        return self.marks + other.marks

if __name__ == "__main__":        
    s1 = Student('Vaishali',12,78)
    s2 = Student('Divya',11,98)
    s3 = Student('Smita',12,88)
    s4 = Student('Anjali',11,78)
    s5 = Student('Nidhi',10,98)

    print(s1)
    print(s2)

    if s3 > s1:
        print(f'{s3} got more marks')

    students = [s1,s2,s3,s4,s5]
    students.sort()
    print(students)

    print(s1 + s2 )