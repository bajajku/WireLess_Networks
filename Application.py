from WirelessNetworks import WirelessNetworks 

class Application:
    def __init__(self):#initializing attributes for class Application
        self.listOfSensors=[]
        self.listOfSensorId=[]
        self.listOfNeighbours=[]
        self.listOfNeighbourId=[]
        self.listOfDistance=[]

    def createSensors(self): #method to create sensors
        wireless=WirelessNetworks() # creating wireless object form WirelessNetworks Class
        wireless.greetMessage() # accessing greetmessage from wireless object
        print("These are sensors of ",wireless.BRAND_NAME," brand , and their Ad Hoc Mode is ",wireless.ADHOC_Mode) # using static variables from wireless objects
        noOfSensors=(input("Enter the number of sensors: ")) # taking input of no of sensors
        while True:# error handling to avoid error while running program
            if (noOfSensors.isdigit() and noOfSensors!="0"):
                break
            else:
                print("This is an invalid entry for the number of sensors!")
                noOfSensors=input("Enter the number of sensors: ")
        for i in range(int(noOfSensors)): #using for loop to create sensors
            wirelessNetworks=WirelessNetworks()
            wirelessNetworks.setId() 
            sensorId=wirelessNetworks.getId()
            wirelessNetworks.setNumNeighs()
            numNeighs=wirelessNetworks.getNumNeighs() 
            for x in range (int(numNeighs)): #using for loop to set oxygenlevel and temperature 
                wirelessNetworks.setNeighbours(sensorId)                
            wirelessNetworks.setOxygenLevel()
            wirelessNetworks.setTemperature()
            print("_*__*__*__*__*__*__*__*__*__*_")
            self.listOfSensors.append(wirelessNetworks) #appending wirelessNetwoks to listOfSensors
            self.listOfSensorId.append(wirelessNetworks.getId()) #appending sensorId to listOfSensorsId
            self.listOfNeighbours.append(wirelessNetworks.getListOfNeighbours())#appendingl istOfNeighbours to listOfNeighbours
    
    def convrtToDictionary(self): # method to create dictionary from listOfsensorId and listOfNeighbours
       self.sensorDict= dict(zip(self.listOfSensorId, self.listOfNeighbours)) # [neghbour1: {id: B, distance: 10}, neighbour2]
       return self.sensorDict
    
    def findPath(self, path, source, destination): # method to create path using a recursive function and by using path source and destination as parameter
        
        if(source==destination):
            path.append(destination)
            return path
        elif(source==""):
            return []
        

        path.append(source) #[A]
        # find out new source
        longestDistance = 0
        neighbourList = self.sensorDict.get(source)
        for neighbour in neighbourList:
            if(int(neighbour.getNeighbourDistance()) > longestDistance):
                if(path.count(neighbour.getNeighbourId()) <= 0):
                    longestDistance = int(neighbour.getNeighbourDistance())
                    source = neighbour.getNeighbourId()
                else:
                    source = ""
        
        finalPath = self.findPath(path, source, destination) #
        return finalPath

application = Application() #creating application object form Application class
application.createSensors() # callling createSensors method
application.convrtToDictionary() # callling convrtToDictionary method
source = input("Enter the source sensor: ") #taking source input
destination = input("Enter the destination sensor: ") # taking destination input
path = []

finalPath = application.findPath(path, source, destination)# checking if path is correct or not and giving the valid output
if(finalPath):
    print("PATH= ",finalPath)
else:
    print("Destination not found")
