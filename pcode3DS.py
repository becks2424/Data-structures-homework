#Rebceca Menda
#Lab3
#I commented out the ones I wasn't really sure about and was trying out

import time
from random import

def main():

waitingRoom = []
triageRoom = []
examRoom = []

examRoomsize = 6
doctors = 6

names = ["Joey", "Bobby", "Sueanne", "Loretta", "Grant", "Jenny", "Billy"\
         "Cletus", "Hunter"]

def callNurse:
    triageRoom.append (waitingRoom.pop(0))
    sort(triageRoom, key = patient.triageNumber)

##class patient:
##    def __init__(name,self,random):
##        self.random = random
##    def triage(self):
##    self.triage = int(triageNumber)
##
##    def getName(self):
##        pass
##    def moveTo(self,location):
##        pass


##
##class patientName:
##        patient(name [random.randInt(0,len(names)-1]\
##                           + " " + names [random.randInt(0,len(names)-1])
        #We'll be able to get names of the patients from the list we made above\
    #*******was trying out something different*******
                      
class patient:
    def __init__(name, location, self):
        self.triageNumber = random.randInt(0, 100)
        self.name = name [random.randInt(0,len(names)-1]\
                           + " " + names [random.randInt(0,len(names)-1]
        self.arrivalTime = time
        self.treatmentTime = random.randInt (15,20)

    def exit (self):
            pass

##class doctor:
##    def __init__(name,self):
##        self.name = name
##        self.random = random (15,20)
##    def examinePatient(self):
##        return self.random


main()
