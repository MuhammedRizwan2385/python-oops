class first:
    def accept2(self):
        self.mark1=int(input("Enter the mark1: "))
        self.mark2=int(input("Enter the mark2: "))
        self.mark3=int(input("Enter the mark3: "))
    def find1(self):
        self.total_marks1=self.mark1+self.mark2+self.mark3
        return(self.total_marks1)

    def display2(self):
        print(f"Mark1: {self.mark1}")
        print(f"Mark2: {self.mark2}")
        print(f"Mark3: {self.mark3}")
class second(first):
    def accept1(self):
        self.regno=int(input("Enter the regno: "))
        self.name=input("Enter the name: ")
    def display1(self):
        print(f"Regno: {self.regno}")
        print(f"Name: {self.name}")
class third(first):
    def accept3(self):
        self.mark4=int(input("Enter the mark4: "))
        self.mark5=int(input("Enter the mark5: "))
        self.mark6=int(input("Enter the mark6: "))
    def find2(self):
        self.total_from_first=self.find1()
        self.total_marks=self.total_from_first+self.mark4+self.mark5+self.mark6
        self.avg_marks=self.total_marks/6
    def display3(self):
        print(f"Mark4: {self.mark4}")
        print(f"Mark5: {self.mark5}")
        print(f"Mark6: {self.mark6}")
        print(f"total Mark: {self.total_marks}")
        print(f"avg mark: {self.avg_marks}")
n=int(input("Enter the no of students: "))
list1=[]
for i in range(n):
    studentB=second()
    studentC=third()
    list1.append((studentB,studentC))

    print(f"Enter the details of  student {i+1}")
    studentB.accept1()
    studentC.accept2()
    studentC.accept3()
    studentC.find2()

for i in range(n):
    print(f"Details of student {i+1}\n")
    studentB,studentC=list1[i]
    studentB.display1()
    studentC.display2()
    studentC.display3()
    

