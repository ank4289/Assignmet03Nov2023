# Create a Car class and Create 2 Objects of the class with attributes 5 and 5 methods


# Hondaobj.Name
class Car:
    Name = None
    Model = None
    Year = None
    Type = None
    Transmission = None
    Running = None
    company = None
    average = None

    def CarDetails(self):
        print("Name of the  car:>", self.Name)
        print("Name of the model :>", self.Model)
        print("Year of manufacturer is ", self.Year)
        print("Type of fuel car:  ", self.Type)
        print("Transmission of car is ", self.Transmission)

    def Running(self):
        print("Running of car is ", self.Running)

    def Carcodition(self):
        if self.Running <= 70:
            print("New Car")
        else:
            print("used car")

    def manufacturer(self):
        print("Company of the car:", self.company)

    def kmpl(self):
        if self.average >= 10:
            print("Average is good")
        else:
            print("Average is bad")

    def delivery(self):
        if self.Running <= 100:
            print("New car delivered")
        else:
            print("Test drive vechile")






Honda = Car()
Honda.Name= input("the name of the car")
Honda.Model=input("Enter the name of the model")
Honda.Year= int(input("Enter year of manufacture"))
Honda.Type =input("Enter type of fuel of the car")
Honda.Transmission = input("Enter the transmission of the car")
Honda.Running= int(input("Enter the kilometer of the car"))
Honda.company= input("Enter the company of the car")
Honda.average= int(input("Enter the average of the car"))

Honda.CarDetails()
Honda.Carcodition()
Honda.manufacturer()
Honda.kmpl()
Honda.delivery()

Suzuki = Car()
Suzuki.Name= input("the name of the car")
Suzuki.Model=input("Enter the name of the model")
Suzuki.Year= int(input("Enter year of manufacture"))
Suzuki.Type =input("Enter type of fuel of the car")
Suzuki.Transmission = input("Enter the transmission of the car")
Suzuki.Running= int(input("Enter the kilometer of the car"))
Suzuki.company= input("Enter the company of the car")
Suzuki.average= int(input("Enter the average of the car"))
Suzuki.CarDetails()
Suzuki.Carcodition()
Suzuki.manufacturer()
Suzuki.kmpl()
Suzuki.delivery()
