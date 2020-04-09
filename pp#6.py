print ('Corin')
print ('11/19/17')
print ('Annual Inflation Rate')

currentPrice = 11.00
previousPrice = 7.00
annualinflationRate = 17.00
priceChange = 17.50
expectedPrice = 19.00
regularPrice = 9.00
Weeks = 27

def main():

    #User can enter an name of an object and receive the outcome of it
    object = input ('Enter name of object.')
    print ('There have been multiple changes to this product.')
    
    message()

def message(): 
    
    print ('The price of object has changed.')
    #Display Price Change of Item
    priceChange = (11.00 - 7.00)/17*52 #PriceChange=(CurrentPrice-PreviousPrice)/Weeks*52
    print ('The price change is $', format(priceChange, ',.2f'))

    #Display Annual Inflation Rate of Item
    print ('The annual inflation rate of the object has gone up.')
    annualinflationRate = 17.50/9.00 #AnnualInflationRate=PriceChange/RegularPrice
    print ('The annual inflation rate is',format(annualinflationRate, ',.2f'), '%') #Object appear as %

    #Display the Expected Price of the Item
    print ('This is the expected price of the object.')
    expectedPrice = 11.00 + 17.00 * 11.00 #ExpectedPrice=CurrentPrice+AnnualIflationRate*CurrentPrice
    print ('The expected price is $',format(expectedPrice, ',.2f')) 


main()
