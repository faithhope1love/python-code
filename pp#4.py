print('Corin')
print('11/14/17')
print('Turkey Day Items and Sale Prices')

count = 0

#Example sale items with original prices
Bread = 4.15
Turkey = 17.00
chocolateMilk = 5.30
Gravy = 2.00
Vegetables = 6.10
#Customer can enter any kind of market item besides these and
#get the discounted price.

while (count < 5): #Max amount of items can be in cart
    count = count + 1

    sale_item = str(input('Enter your sale item: ')) #Enter sale item.
    originalPrice = float(input('Enter your original price: ')) # Enter original price of sale item
    salePrice = originalPrice - 0.10 + 0.05 - 0.01 #discounted price 10%, rounded price, -1 cent
    print ('The sale price is $',format(salePrice, ',.2f')) #total

#    if notDone: #Not having max of 5 items system will ask if you want to continue.
#        input('Do you want to calculate more sale items? ' + ('Enter c to continue.: '))
    
print ('You have 5 items in your cart. Thank you for shopping the annual Turkey Day Sale!')

        
