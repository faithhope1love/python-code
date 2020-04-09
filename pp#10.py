#Corin Price-Howard, BIS 323
#Program's Completion Date: 12/10/17
#Week Number: 6
#Program 8: [Employee Search]
# ####################

def main():
    #Create empyty dictionary
    employee_file = {}
    #Open employeesAQYX.txt file
    employee_file = open('employeesAQYX.txt', 'r')
    #If file is being read, will continue to process file
    while employee_file != '':
        #Read the first file line
        last = employee_file.readline()
        #Read first name
        first = employee_file.readline()
        #Read phone extension
        phone_etn = employee_file.readline()
        #Read department
        dept = employee_file.readline()
        #Strip new lines will separate the file into sections
        first = first.rstrip('\n')
        phone_etn = phone_etn.rstrip('\n')
        dept = dept.rstrip('\n')
        #User input for employee search. Enter employee's last name.
        #After function, read next employees first name.
        print('Employee\'s first name is: ', first)
        last = (input('Enter employee\'s last name: '))
        if last != employee_file:
            print('Last name found.')
            #Print last name and list consisting of first name, phone extension and department code
            print ('Last name:', last)
            print(['First name:', first,'Phone Extension:', phone_etn,'Department Code:', dept])
    #Read last name in file after input
    last = employee_file.readline()
    #Close file
    employee_file.close()
#Retunr to beginning of file    
main()
