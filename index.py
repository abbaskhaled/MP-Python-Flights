#creat three classes 

class Person:
    def __init__(self , name , age ,passport_number):
        self.name = name 
        self.age = age 
        self.passport_number= passport_number

    
class Passenger(Person):
    def __init__(self , name , age , number_of_bags,passport_number ,destination):
        super().__init__(name , age, passport_number)
        self.destination = destination
        self.number_of_bags = number_of_bags
        self.passport_number = passport_number 
        
        

    def get_bag_weight(self):
        return self.number_of_bags  * 23

    def __str__(self):
        return f"Person name is {self.name}his age {self.age}his passport_number{self.passport_number} bags {self.number_of_bags} destination {self.destination} "


Passenger_one = Passenger("Laila",23,854534,2,"Japan")
Passenger_two = Passenger("Shereen",25,9876542,3,"Germany")
print (Passenger_one)
print (Passenger_two)

class Captin (Person):
    def __init__(self , name ,age , passport_number ,experience_years,salary):
        super().__init__(name , age,passport_number)
        self.experience_years = experience_years
        self.salary = salary
    
    def get_bonus(self):
        return (self.experience_years /100) * self.salary 

    def __str__(self):
        return f"Captin name is {self.name} his age {self.age} his passport_number{self.passport_number} his experience_years {self.experience_years} Salary {self.salary} "


Passenger_one = Passenger("Laila",23,854534,2,"Japan")
Passenger_two = Passenger("Shereen",25,9876542,3,"Germany")
print (Passenger_one)
print (Passenger_two)


captin_one = Captin("khaled",26,99999,5,3000)
captin_two = Captin("yousef",23,88888,4,2500)
print (captin_one)
print (captin_two)


def show_option ():
    options = ["show persons " , "show captains " ,"Add person" , "Add captain" ]
    for index, option in enumerate(option,1):
        print (index , option )

def get_user_option():
    user_option = int(input(" plese choose ? " ))


    if user_option == 1 :
        print (Person)

    elif user_option == 2 :
        print (Captin)

    elif user_option == 3 :
       add_person = Person(input("Enter a name \n"),input("Enter a age \n"),input("Enter passport_number \n "))
       print (Person)

    elif user_option == 4 :
       add_captin = Captin(input("Enter a name \n "), input ("Enter a age \n  "), input("Enter passport number\n ", ), input("experience_years\n"),input ("salary\n "))
       print (Captin)

    else :
        print ("choose a number 1 to 4 please ")


get_user_option()
       
