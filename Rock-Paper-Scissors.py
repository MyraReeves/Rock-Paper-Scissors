import random

print('Let\'s play a game of Rock, Paper, Scissors!')
Player_One = input('Please enter your name: ').capitalize()
Player_Two = 'The computer'

def startGame():
    print('')

    def outcomes(Player_One_Choice, Player_Two_Choice):
        if Player_One_Choice == 'rock' and Player_Two_Choice == 'paper':
            return('Paper covers Rock! ' + Player_Two + ' wins this round!')
        elif Player_One_Choice == 'paper' and Player_Two_Choice == 'rock':
            return('Paper covers Rock! ' + Player_One + ' wins this round!')

        elif Player_One_Choice == 'rock' and Player_Two_Choice == 'scissors':
            return('Rock smashes Scissors! ' + Player_One + ' wins this round!')
        elif Player_One_Choice == 'scissors' and Player_Two_Choice == 'rock':
            return('Rock smashes Scissors! ' + Player_Two + ' wins this round!')

        elif Player_One_Choice == 'paper' and Player_Two_Choice == 'scissors':
            return('Scissors cut Paper! ' + Player_Two + ' wins this round!')
        elif Player_One_Choice == 'scissors' and Player_Two_Choice == 'paper':
            return('Scissors cut Paper! ' + Player_One + ' wins this round!')

        elif Player_One_Choice == Player_Two_Choice:
            return('You tied this round!')

        else:
            return('Invalid response. The only valid response choices are: "Rock", "Paper", or "Scissors"')


    Player_One_Chose = input('Do you choose rock, paper, or scissors? ').lower()


    def Player_Two_Chose(number):
        if number == 1:
            return('rock')
        elif number == 2:
            return('paper')
        elif number == 3:
            return('scissors')
        else:
            return('ERROR')
    ComputerChoice = Player_Two_Chose(random.randint(1,3))
    print('The computer randomly chose ' + ComputerChoice)


    print(outcomes(Player_One_Chose, ComputerChoice))
    

    def Play_Again():
        print('')
        RestartAnswer = input('Would you like to play again? ').lower()
        if RestartAnswer == 'no':
            quit()
        if RestartAnswer == 'yes':
            startGame()
        else:
            print('Please answer with either "yes" or "no"')
            Play_Again()



    Play_Again()


startGame()
