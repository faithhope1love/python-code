print('Corin')
print('11/14/17')
print('Peirce Rocks Theater Admission')

#This program will display the age then charge price for a ticket
#Age will qualify depending on ticket charge

AGE_OVER = +64 #If over 64 customer will have to pay $12.00.
AGE_BETWEEN = 21 - 64 #If between age 21-64 customer will have to pay $16.00.
AGE_BETWEENTWO = 13 - 20 #If between 13-20 customer will have to pay $8.00.
AGE_BETWEENTHREE = 3 - 12 #If between 3-12 customer will have to pay $4.00.
AGE_UNDER = -3 #If under 3 customer will be FREE.

age1 = float(input('Enter your age: ')) #Charge of ticket
if age1 >= AGE_OVER: #Charge of ticket
    print ('You owe $12.00.')
    
age2 = float(input('Enter your age: ')) #''
if age2 >= AGE_BETWEEN: #''
    print ('You owe $16.00')

age3 = float(input('Enter your age: ')) #''   
if age3 >= AGE_BETWEENTWO: #''
    print ('You owe $8.00')
    
age4 = float(input('Enter your age: ')) #''
if age4 >= AGE_BETWEENTHREE:#''
    print ('You owe $4.00')

age5 = float(input('Enter your age: ')) #''
if age5 >= AGE_UNDER: #''
    print ('You owe $0.00')
