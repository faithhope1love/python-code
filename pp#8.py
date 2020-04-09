#Corin
#Program's Completion Date: 12/3/17
#[Hit-Or-Miss Credit Card Numbers]
# ####################

def main():
    card_nums = []

    card_num = str(input('Enter a card number: '))
    card_nums.append(card_num)

    if card_num.upper():
        print(card_num, 'was valid.')
    else:
        print(card_num, 'was invalid.')
    if card_num.lower():
        print(card_num, 'was valid.')
    else:
        print(card_num, 'was invalid.')
    if card_num.digits():
        print(card_num, 'was valid.')
    else:
        print(card_num, 'was invalid.')

main()
