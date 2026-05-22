##initiate a class
class Employee:
    ##Special functions / magic methods/ dunder methods --constructor
    def __init__(self):
        print("Started Executing attributes/data")
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
        print("attributes/data initiated")

    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is travelling to {destination}")

##Creating an object or instance of the class
sam = Employee()

##Printing the Attributes
print(sam.salary)
print(sam.id)

##Calling the methods
sam.travel("Paris")