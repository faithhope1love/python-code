#Corin

#This program displays gross pay and to allow the user to enter as many
#gross pay's as they choose.

print ('Batch Program B: Gross Pay')

while (100):

#Number of hours worked.

	hours = int(input('How many hours have you worked?: '))

#Hourly pay rate.

	pay_rate = float(input('What is your hourly pay rate?: '))

	print ('Hourly pay: ', hours)

	print ('Pay rate: ', pay_rate)

#Work 40 hours or less than 40 hours.

	if (hours <= 40):
		print ('Hours: ', hours)
	else:
		print ('Too many hours.')

#Pay rate is 20 or less than 20.

	if (pay_rate <= 20):
		print ('Pay rate: ', pay_rate)
	else:
		print ('Rate is incorrect.')


	print ('Gross Pay: ', hours * pay_rate)

	print ('_______________________________')

print ('End of Batch Program B: Gross Pay')
