try:
    age=int(input("Enter the age:"))
    if age<18:
        raise ValueError
except ValueError:
    print("Invalid age")
else:
    print("age is valid")
finally:
    print("Have a nice day")
