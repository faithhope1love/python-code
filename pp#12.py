#Corin
#Program's Completion Date: 12/3/17
#[Olympic Scoring]
# ####################

#Number of Judges
num_of_judges = 9
def main():
    #Score List
    scores = []
    #Judge List
    judges = ['USA', 'RUS', 'JPN', 'GBR', 'FRA', 'CAN', 'DEU', 'ITA', 'CHN']
    #Variable starting with number one
    index = 0
    #Enter each Judges score
    for i in range(len(judges)):
        judge = judges[i]
        print('Enter score for ',judge,': ', sep='', end='')
        scores.append(int(input()))
    #Determine average score
    average = sum(scores)/len(scores)
    #Display high score
    print('The average score is: ', '{0:.2f}'.format(average))      
    #Determine high score
    max_score = max(scores)
    #Display high score
    print('The high score is:', max_score)
    #Determine low score
    min_score = min(scores)
    #Display low score
    print('The low score is:', min_score)
main()

