#Corin Price-Howard, BIS 323
#Program's Completion Date: 12/3/17
#Week Number: 5
#Program 7: [Hit-Or-Miss Credit Card Numbers]
# ####################

def main():
    card_nums = ['A53567259_a', 'H93572853.h', 'L23103302_l']

    card_num = input('Enter a card number: ')

    if card_num in card_nums:
        print(card_num, 'was valid.')
    else:
        print(card_num, 'was invalid.')

main()
