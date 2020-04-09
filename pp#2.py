#Corin
#Program's Completion Date: 12/17/17
#[Part 1, Part 2 and Part 3: Individual Class]
# #####################

#PART 1
#Create a class with first name, last name and mail address
class Individuals:
    
    #instantiate function with first, last, and mail address
    def __init__(self, first, last, street, city, zip_code):
        self.first = first
        self.last = last
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.address = self.street + self.city + self.zip_code

indiv_1 = Individuals('Robert', 'King', '\n317 E.Street ', 'Philadelphia, ', '19171' )
indiv_2 = Individuals('Corin', 'Queen', '\n277 E.Street ', 'Philadelphia, ', '19147')
indiv_3 = Individuals('Faith', 'Heaven', '\n937 W.Street ', 'Los Angeles, ', '90013' )
indiv_4 = Individuals('Aiden', 'Hell', '\n192 W.Street ', 'Los Angeles, ', '90005')

#Get individuals first and last name
def get_first(self):
    return self.first
def get_last(self):
    return self.last

#Set individuals first and last name, and mail address
def set_first(self, first):
    self.first = first
def set_last(self, last):
    self.last = last
def set_street(self, street):
    self.street = street
def set_city(self, city):
    self.city = city
def set_state(self,state):
    self.state = state
def set_zipCode(self, zip_code):
    self.zip_code = zip_code

def __str__(self): #__Str__() value with first and last name and address
    return '[] [] []'.format(self.first, self.last, self.address)

#Display all current information and attributes
indiv_1 = print('First Name:', indiv_1.first), print('Last Name:', indiv_1. last), print('Mail Address:', indiv_1.address)
indiv_2 = print('\nFirst Name:', indiv_2.first), print('Last Name:', indiv_2.last), print('Mail Address:', indiv_2.address)
indiv_3 = print('\nFirst Name:', indiv_3.first), print('Last Name:', indiv_3.last), print('Mail Address:', indiv_3.address)
indiv_4 = print('\nFirst Name:', indiv_4.first), print('Last Name:', indiv_4.last), print('Mail Address:', indiv_4.address)

#################################

print('-----------End of Class Definition-------------')

#PART 2

#Create main function
def main():
    
    #Instantiate an object of the class with no values
   def __init__():
        self.first = first
        self.last = last
        self.street = street
        self.city = city
        self.zip_code = zip_code
        self.address = self.street + self.city + self.zip_code
        
#Display current status of an instantiated object
print('This is the name and mail address entered for the first individual: \n')
print(['Robert', 'King', '317 E.Street ', 'Philadelphia, ', '19171'] )
          
#Empty list for objects
first = []
last = []
street = []
city = []
zip_code = []
   
#Request from the user all data from each individual and print in a list 
indiv_2 = print(['Corin', 'Queen', '277 E.Street ', 'Philadelphia, ', '19147'])
indiv_3 = print(['Faith', 'Heaven', '937 W.Street ', 'Los Angeles, ', '90013'])
indiv_4 = print(['Aiden', 'Hell', '192 W.Street ', 'Los Angeles, ', '90005'])

#Allow user to make changes to the address of indiv_1
print('\nChange the mail address of the individual Robert King.')
indiv_1 = [print('\nFirst Name:','Robert'), print('Last Name:', 'King'), input('Mail Address:')]

#Print changes
print('\nThese are the changes made to the name and address of the first individual: ')
print('Robert King', indiv_1)

#Return to main function
main()

#################################

print('----------End of Main Definition-------------')

#PART 3

#Create a class definition
class Patients(Individuals):
    def __init__(self, first, last, street, city, zip_code, temperature, blood_pressure, respiration_rate, pain_level):

        #Get function
        def get_temperature(self):
            return self.temperature
        def get_blood_pressure(self):
            return self.blood_pressure
        def get_respiration_rate(self):
            return self.respiration_rate
        def get_pain_level(self):
            return self.pain_level

        #Set function
        def set_get_temperature(self, get_temperature):
            self.get_temperature = get_temperature
        def set_blood_pressure(self, blood_pressure):
            self.blood_pressure = blood_pressure
        def set_respiration_rate(self, respiration_rate):
            self.respiration_rate = respiration_rate
        def set_pain_level(self, pain_level):
            self.pain_level = pain_level

#Indidivuals
indiv_1 = ('Robert', 'King', indiv_1)
indiv_2 = ('Corin', 'Queen', '277 E.Street ', 'Philadelphia, ', '19147') 
indiv_3 = ('Faith', 'Heaven', '937 W.Street ', 'Los Angeles, ', '90013') 
indiv_4 = ('Aiden', 'Hell', '192 W.Street ', 'Los Angeles, ', '90005')

#Patients objects
temperature = int(92.1)
blood_pressure = int(99.9)
respiration_rate = int(120/60)
pain_level = int(0) 

#Display all information
print(indiv_1 + (temperature, blood_pressure, respiration_rate, pain_level))
print(indiv_2 + (temperature, blood_pressure, respiration_rate, pain_level))
print(indiv_3 + (temperature, blood_pressure, respiration_rate, pain_level))
print(indiv_4 + (temperature, blood_pressure, respiration_rate, pain_level))

print('-----------End of Class Definition-------------')
