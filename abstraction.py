from abc import ABC,abstractmethod
class A(ABC):
    def print(self):
        print("This is print() of parent class...")
    @abstractmethod
    def hello(self):
        None
class B(A):
    
    def hello(self):
        print("this is abstract method from child class B")
class C(A):
    
    def hello(self):
        print("This is abstract method from child class C")
obj1=B()
obj2=C()
obj1.print()
obj1.hello()
obj2.print()
obj2.hello()
