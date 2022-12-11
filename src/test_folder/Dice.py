"""
=================================================
Author:     Drew Rinker
Date:       12/11/22

Defines Dice Objects
=================================================
"""
# import random
from random import randint,shuffle

class Dice(object):

    def __init__(self, numOfSides, color, numOfHits, numOfDirectHits, numOfSpecial, numOfBlank):
        self.numOfSides = numOfSides
        self.color = color
        self.numOfHits = numOfHits
        self.numOfDirectHits = numOfDirectHits
        self.numOfSpecial = numOfSpecial
        self.numOfBlank = numOfBlank

    def getNumOfSides(self):
        return self.numOfSides

    def setNumOfSides(self, newNumOfSides):
        self.numOfSides = newNumOfSides

    def getColor(self):
        return self.color
    
    def setColor(self, newColor):
        self.color = newColor

    def getNumOfHits(self):
        return self.numOfHits

    def setNumOfHits(self, newNumOfHits):
        self.numOfHits = newNumOfHits

    def getNumOfDirectHits(self):
        return self.numOfDirectHits

    def setNumOfDirectHits(self, newNumOfDirectHits):
        self.numOfDirectHits = newNumOfDirectHits

    def getNumOfSpecial(self):
        return self.numOfSpecial

    def setNumOfSpecial(self, newNumOfSpecial):
        self.numOfSpecial = newNumOfSpecial

    def getNumOfBlank(self):
        return self.numOfBlank

    def setNumOfBlank(self, newNumOfBlank):
        self.numOfBlank = newNumOfBlank

    def rollDice(self):
        # could split this up. 'makeDice()' 'rollDice()'
        diceLegend = {"H", "DH", "SP", "BLNK"}
        dice = []
        for x in range(self.getNumOfHits()):
            dice.append("H")
        for x in range(self.getNumOfDirectHits()):
            dice.append("DH")
        for x in range(self.getNumOfSpecial()):
            dice.append("SP")
        for x in range(self.getNumOfBlank()):
            dice.append("BLNK")

        print(dice)
        shuffle(dice)
        print(dice)
        diceIndex = randint(0, self.getNumOfSides() - 1)
        print(diceIndex)
        diceSideLandedOn = dice[diceIndex]
        print("Dice roll is: " + str(diceSideLandedOn))

    def validateDice(self):
        # TODO
        pass

