#A simple python program to read and print details of 2 persons
class ABC:
    def fill_details(self,name,branch,age):
        self.name=name
        self.branch=branch
        self.age=age
    def print_details(self):
        print("Name: ",self.name)
        print("Branch: ",self.branch)
        print("Age: ",self.age)
s1=ABC()
s2=ABC()
s1.fill_details("Arun","CSE",40)
s1.print_details()
s2.fill_details("Chinnu ravi","CSE",36)
s2.print_details()
