class Person:

    def persondetails(self,name,age,address):
        print("The following are person details" ,name,age,address)


Person_ref_obj= Person()
Person_ref_obj.persondetails(name=input("Please enter your name"),age=int(input("Enter age")),address=input("Enter your address"))
