import re
from Neighbour import Neighbour

class WirelessNetworks:
    ADHOC_Mode="ON" # static variable for Ad Hoc mode
    BRAND_NAME="Cisco" # static variable for Brand Name

    def greetMessage(self): # method to greet message
        print("Welcome to the company's IoT-Based Health System")

    def __init__(self):# initializing attributes for class WirelessNetworks
        self.Id=""
        self.oxygenLevel=int
        self.temperature=float
        self.NumNeighs=int
        self.listOfNeighbours=[]
        self.listOfNeighbourId=[]
        self.listOfDistance=[]

    def setId(self): #method to set Id
        self.Id=input("Enter the Sensor Id: ") #taking input from user for Id
        while True:  # error handling to avoid error while running program
            check = re.search("^[A-Z]",self.Id)
            if check:
                   break
            else:
                print("This is an invalid entry for sensor Id!")
                print("_*__*__*__*__*__*__*__*__*__*_ ")
                self.Id=input("Enter the Sensor Id: ")
        


    def getId(self): #method to get Id
        return self.Id 

    def setOxygenLevel(self): #method to set OxygenLevel
        self.oxygenLevel=input("Enter the Oxygen level in %: ")#taking input from user for oxygen Level
        while True:  # error handling to avoid error while running program
            if (self.oxygenLevel.isdigit() and self.oxygenLevel!=str(float) and self.oxygenLevel!="0"):
                break
            else:
                print("This is an invalid entry for the oxygen level!")
                self.oxygenLevel=input("Enter the Oxygen level in %: ")

    def getOxygenLevel(self):#method to get OxygenLevel
        return self.oxygenLevel
                
    def setTemperature(self):#method to set Temperature
        self.temperature=input("Enter the temperature measurement: ")#taking input from user for temperature
        while True: # error handling to avoid error while running program
            if (self.temperature.isdigit()):
                break
            else:
                print("This is an invalid entry for the temperature!")
                self.temperature=input("Enter the temperature measurement: ")
    
    def getTemperature(self):#method to get Temperature
        return self.temperature


    def setNumNeighs(self):#method to set number of Neighbours
        self.NumNeighs=input("Enter the number of neighbours: ")
        while True: # error handling to avoid error while running program
            if (self.NumNeighs.isdigit() and self.NumNeighs!="0" and self.NumNeighs!=float):
                break
            else:
                print("This is an invalid entry for number of neighbours!")
                self.NumNeighs=input("Enter the number of neighbours: ")
    
    def getNumNeighs(self): #method to get Number of Neighbours
        return self.NumNeighs

    def setNeighbours(self,sensorId):#method to set Neighbours using sensorId as parameter
        neighbourId = input("Enter the neighbor for Sensor "+ sensorId +": ")#taking input from user for NeighbourId
        while True:  # error handling to avoid error while running program
            check = re.search("^[A-Z]",neighbourId)
            if (check and neighbourId!=sensorId):
                break
            else:
                print("This is an invalid entry for neighbour of Sensor",sensorId,"! ")
                neighbourId=input("Enter the neighbor for Sensor "+ sensorId +": ")
        self.listOfNeighbourId.append(neighbourId)# appending neighbourId to listOfneighbours
        neighbourDistance = input("Enter the distance to "+ sensorId + ": ") #taking input from user for neighbour Distance
        while True:  # error handling to avoid error while running program
            if (neighbourDistance.isdigit() and neighbourDistance!="0" and neighbourDistance!=float):
                break
            else:
                 print("This is an invalid entry for distance!")
                 neighbourDistance=input("Enter the distance to "+ sensorId + ": ")
        self.listOfDistance.append(neighbourDistance)# appending neighbourDistanceto listOfneighbours
        neighbour = Neighbour(neighbourId, neighbourDistance)# makinfg neighbour object from Neighbour class
        self.listOfNeighbours.append(neighbour)
    
    def getListOfNeighbours(self): #method to get list of Neighbours
        return self.listOfNeighbours

