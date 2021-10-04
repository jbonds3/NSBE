from __future__ import print_function
from random import choice
import re, json, random

class Player:
    def __init__(self, name):
        self.playerNum = 0
        self.name = name
        self.character = ''
        self.barList = []
        self.jsonIndex = 0

class Players:
    def __init__(self, players):
        self.players = players

def skip(str):
    if isinstance(str, Player):
        if str.playerNum == 1:
            player = nameList()
    elif isinstance(str, str):


def game(player1, player2, charactersUsed):
    charJSON = json.load(open("characters.json"))

    if len(range(0,len(charJSON) - 1)) - len(charactersUsed) != 0:
        print('\nplayer1 is % s' % player1.name)
        print('player2 is % s\n\n' % player2.name)

        characterInUse = list(set(range(0,len(charJSON) - 1)) - set(charactersUsed))

        randNum = random.sample(characterInUse, 2)

        player1.jsonIndex, player2.jsonIndex = randNum[0], randNum[1]

        # print("character total: %s" % range(0,len(charJSON) - 1))
        # print("charactersUsed: %s" % charactersUsed)
        # print("characterInUse: %s" % characterInUse)
        # print("randNum: %s" % randNum)
        # print("randNum1: %s" % player1.jsonIndex)
        # print("randNum2: %s" % player2.jsonIndex)


        player1.character = charJSON["charName"][player1.jsonIndex]

        # print("p1: %s" % player1.character)

        player2.character = charJSON["charName"][player2.jsonIndex]

        # print("p2: %s" % player2.character)

        player1.barList = charJSON[player1.character]

        player2.barList = charJSON[player2.character]

        print(player1.name + ': ' + player1.character)
        print(player1.barList)

        print('\n\n')
        print(player2.name + ': ' + player2.character)
        print(player2.barList)

        charactersUsed.append(player1.jsonIndex)
        charactersUsed.append(player2.jsonIndex)
    else:
        print('Out of character :(')
        print('Add more characters for $4.99')
        exit()

def main():
    inputTxt = ''
    charactersUsed = []
    nameList = Players([])

    #players input phone numbers
    with open ("playerList.txt", "r") as myfile:
        nameList.players = list(myfile.readlines())

    while inputTxt != 'd':
        for index, pNum in enumerate(nameList):
            if index % 2 == 0:
                player1, player2 = Player(nameList[index]), Player(nameList[index+1])
                player1.playerNum = 1
                player2.playerNum = 1
                game(player1, player2, charactersUsed)
                print('\nEnter d for done else hit enter for next round')
                inputTxt = input()

if __name__ == "__main__":
    main()
