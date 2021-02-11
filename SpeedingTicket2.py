#SpeedingTicket.py
#Calculates Speeding Fine
#Scott Mouat, Feb 2021


def speed_legality():
    while True:
        try:
            speed = int(input("What is the speed that you were going?"))
            if speed <= 0 or speed >= 300:
                speed = ValueError
                print("That is not a valid speed")
            else: 
                return speed
        except ValueError:
            print("That is not a valid speed")
            
def conditions(s, name):
    limit = int(input("What is the speed limit?"))
    difference = s - limit
    if difference <= 0:
        print("This person was not speeding")
        
    elif difference > 0 and difference <= 50:
        fine = difference * 6
        print("{} needs to pay ${}".format(name, fine))
        
        
    elif difference > 50 and difference <= 100:
        print("Your licence is gone mate")
        
    else:
        print("Straight to jail, learn how to drive")
       
        
def check_person():
    name = input("What is your name?")
    if name in warrant_people:
        print("This person has a warrant")
    else: 
        print("He is not on the list")
        speed_gone = speed_legality()
        calc_fine = conditions(speed_gone, name)        
        
warrant_people = ["Trisan", "Ravi", "Wilco"]
morepeople = "Y"
while morepeople == "Y":
    check_person()
    morepeople = input("Is there more speeders?(Y/N)")
    