import random

moves = ['r', 'p', 's']
num = int(input("number of games:"))
score = {'user':0, 'computer':0,}
def main(num):
    for i in range(num):
        user_input = input("Make your move(rock(r), paper(p) or scissors(s): ")
        if user_input not in moves:
            print('wrong input!!!')
        computer_move = random.choice(moves)
        winner(user_input, computer_move)
    for player in score:
        print(str(player)+':'+str(score[player]))
def winner(user_input, computer_move):
    if user_input == computer_move:
        print("Both of the parties have chosen the same move:"+ user_input+ 'so it is a tie')
    elif user_input == 'p':
        if computer_move == 's':
            print("sciccors cut paper:  Computer wins")
            score['computer'] +=1
        else:
            print('Paper covers rock, User wins')

            score['user'] +=1
    elif user_input == 'r':
        if computer_move == 'p':
            print("Paper covers rock Computer wins")
            score['computer'] +=1
        else:
            print('Rock smasshes scissors, User wins')
            score['user'] +=1
    else:
        if computer_move == 'r':
            print("Rock smasshes scissors:  Computer wins")
            score['computer'] +=1
        else:
            print('scissors cut paper, User wins')
            score['user'] +=1
main(num)
