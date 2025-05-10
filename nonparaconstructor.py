class ABC:
    def __init__(self):
        print("This is non parameterised constructor")
    def print_details(self,name,age,branch):
        self.name=name
        self.branch=branch
        self.age=age
        print("Name: ",self.name)
        print("Branch: ",self.branch)
        print("Age: ",self.age)
s1=ABC()
s1.print_details("Arun",40,"CSE")
