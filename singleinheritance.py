class ABC:
    def accept1(self):
        self.regno=int(input("Enter the regno: "))
        self.name=input("Enter the name: ")
    def display1(self):
        print(f"Regno: {self.regno}")
        print(f"Name: {self.name}")
class DEB(ABC):
    def accept2(self):
        self.mark1=int(input("Enter the mark1: "))
        self.mark2=int(input("Enter the mark2: "))
        self.mark3=int(input("Enter the mark3: "))
    def find(self):
        self.total_marks=self.mark1+self.mark2+self.mark3
        self.avg_marks=self.total_marks/3
    def display2(self):
        print(f"Mark1: {self.mark1}")
        print(f"Mark2: {self.mark2}")
        print(f"Mark3: {self.mark3}")
        print(f"total Mark: {self.total_marks}")
        print(f"avg mark: {self.avg_marks}")

n=int(input("Enter the no of students: "))
list1=[]
for i in range(n):
    student=DEB()
    list1.append(student)
    print(f"Enter the details of  student {i+1}")
    student.accept1()
    student.accept2()
    student.find()
for i in range(n):
    print(f"Details of student {i+1}\n")
    list1[i].display1()
    list1[i].display2()
    

