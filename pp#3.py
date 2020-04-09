#Corin Price-Howard, BIS 323
#Program's Completion Date: 12/17/17
#Week Number: 7
#Program 9: [Individual Class]
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

indiv_1 = Individuals(input, input, '\n317 E.Street ', 'Philadelphia, ', '19171' )
indiv_2 = Individuals(input, input, '\n277 E.Street ', 'Philadelphia, ', '19147')
indiv_3 = Individuals(input, input, '\n937 W.Street ', 'Los Angeles, ', '90013' )
indiv_4 = Individuals(input, input, '\n192 W.Street ', 'Los Angeles, ', '90005')

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
indiv_1 = input('First Name:'), input('Last Name:'), print('Mail Address:', indiv_1.address)
indiv_2 = input('\nFirst Name:'), input('Last Name:'), print('Mail Address:', indiv_2.address)
indiv_3 = input('\nFirst Name:'), input('Last Name:'), print('Mail Address:', indiv_3.address)
indiv_4 = input('\nFirst Name:'), input('Last Name:'), print('Mail Address:', indiv_4.address)

#################################

print('--------------------')

#PART 2
def main():
    
    #Instantiate an object of the class with no values
    class Individuval:
        def __init__():
            indiv_1 = [first, last, street, city, zip_code]
        
    #Display current status of instantiated object <--Fix! Add mail address 
    print('This is the name and mail address entered: ', print(indiv_1))
          
    #Empty list for objects <-- Fix!
    first = []
    last = []
    street = []
    city = []
    zip_code = []
   
    #Request from the user all data from each individual and print in a list <--Fix! add previous entered inputs
#    print[indiv_1, '\n317 E.Street ', 'Philadelphia, ', '19171']
#   print[indiv_2, '\n277 E.Street ', 'Philadelphia, ', '19147']
#   print[indiv_3, '\n937 W.Street ', 'Los Angeles, ', '90013' ]
#   print[indiv_4, '\n192 W.Street ', 'Los Angeles, ', '90005']

    #Allow user to make changes to the address of indiv_1
indiv_1 = print[input('First Name:'), input('Last Name:'), input('Mail Address:')]

    #Print changes
print('These are the changes made to the name and address of indiv_1: ')
main()

