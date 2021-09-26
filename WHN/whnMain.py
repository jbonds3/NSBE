import re, json, random
from random import choice
class Player:
    def __init__(self, phoneNum):
        self.phoneNum = phoneNum
        self.character = ''
        self.barList = []




def game(player1, player2):
    print()
    print('player1 is % s' % player1.phoneNum)
    print('player2 is % s' % player2.phoneNum)

    charJSON = json.load(open("characters.json"))

    randNum = random.sample(range(0,len(charJSON) - 1), 2)

    player1.character = charJSON["charName"][randNum[0]]

    player2.character = charJSON["charName"][randNum[1]]

    player1.barList = charJSON[player1.character]

    player2.barList = charJSON[player2.character]

    print(player1.barList)

    print(player2.barList)

    while True:
        print('stop')
        x = input()

def main():
    inputTxt = ''

    phoneNumList = []

    print('Enter phone numbers on players: ')
    print('Hit Enter start (s) when done\n')

    print('Player {}'.format(len(phoneNumList) + 1))
    print('Phone #: ', end='')

    #players input phone numbers
    while inputTxt != 's':
        inputTxt = input()

        if inputTxt in phoneNumList:
            print('Number already registered\n')
            print('Player {}'.format(len(phoneNumList) + 1))
            print('Phone #: ', end='')

        elif inputTxt != 's':
            if bool(re.match("[0-9]{10}", inputTxt)):
                phoneNumList.append(inputTxt)
                print('Entered.....\n\n')
            else :
                print('Input was not a phone number\n')

            print('Player {}'.format(len(phoneNumList) + 1))
            print('Phone #: ', end='')

    for index, pNum in enumerate(phoneNumList):
        if index % 2 == 0:
            player1, player2 = Player(phoneNumList[index]), Player(phoneNumList[index+1])
            game(player1, player2)

if __name__ == "__main__":
    main()
