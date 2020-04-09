#Corin Price-Howard, BIS 323
#Program's Completion Date: 11/26/17
#Week Number: 4
#Program 5: Business Expenses
# #####################

#lodging-1.txt file
print ('This is your lodging-1.txt file!')
infile = open ('lodging-1.txt', 'rt')
text = infile.read()
print (text)

lodging_sum = 135.33 + 89.17 + 186.84 + 112.56
print ('\nThe sum of your expenses are:', (format(lodging_sum, ',.2f')))

lodging_average = lodging_sum/4
print ('Your avaerage expenses are:', (format(lodging_average, ',.2f')))

infile.close()

#dining-1.txt file
print ('\nThis is your dining-1.txt file!\n')

infile = open ('dining-1.txt', 'rt')
text = infile.read()
print (text)

dining1_sum = 9.45 + 14.32 + 28.26 + 12.93 + 16.21 + 32.76 + 11.22 + 8.26 + 27.45 + 10.02 + 14.42 + 38.23
print ('\nThe sum of your expenses are:', (format(dining1_sum, ',.2f')))

dining1_average = dining1_sum/12
print ('Your avaerage expenses are:', (format(dining1_average, ',.2f')))

infile.close()

#gas.txt file
print ('\nThis is your gas.txt file!\n')
infile = open ('gas.txt', 'rt')
text = infile.read()
print (text)

gas_sum = 35.23+ 42.67+ 32.65+ 43.12+ 34.67
print ('\nThe sum of your expenses are:', (format(gas_sum, ',.2f')))

gas_average = gas_sum/5
print ('Your avaerage expenses are:', (format(gas_average, ',.2f')))

infile.close()

#total of all the files
total = lodging_sum + dining1_sum + gas_sum
print ('\nThe total expenses from the following files lodging-1.txt, dining-1.txt, and gas.txt are:', (format(total, ',.2f')))
