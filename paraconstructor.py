class ABC:
    def __init__(self,name,branch,age):
        self.name=name
        self.branch=branch
        self.age=age
    def print_details(self):
        print("Name: ",self.name)
        print("Branch: ",self.branch)
        print("Age: ",self.age)
n=int(input("Enter the number of persons:"))
list1=[]
for i in range(n):
    print(f"Enter the details of the {i+1}person")
    name=input("Enter the name: ")
    age=int(input("Enter the age: "))
    branch=input("Enter the branch: ")
    person=ABC(name,branch,age)
    list1.append(person)
for i in range(n):
     print(f" The details of the {i+1}person\n") 
     list1[i].print_details()



