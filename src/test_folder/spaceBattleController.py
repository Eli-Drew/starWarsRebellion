"""
Author:     Drew Rinker
Date:       12/10/2022

Space Battle Driver.
"""

import json
import sys
from Combat_Card_Space import CombatCard


def importCombatCards(cardList, faction, theater):
    """Takes in .json file and reads a json segment representing a space tactic card."""
    spaceBattleCardList = []
    for x in cardList:
        name = x["name"]
        descriptionTop = x["descriptionTop"]
        descriptionBottom = x["descriptionBottom"]
        vehicleBonus = x["vehicleBonus"]
        newCombatCard = CombatCard(
            faction, name, theater, descriptionTop, descriptionBottom, vehicleBonus)
        spaceBattleCardList.append(newCombatCard)
    return spaceBattleCardList


def readJsonCardInfo(fileName):
    with open(fileName, "r") as readFile:
        data = json.load(readFile)
        return data


def printCardSet(cardSet):
    """Functions that prints cards to the console. Assumes __str__ method is defined for the class."""
    for card in cardSet:
        print(card)


def main():

    # open rebel space card json file and create Rebel Space card objects.
    data = readJsonCardInfo("rebelsSpaceBattleCards.json")
    faction = data["faction"]
    theater = data["theater"]
    cardSet = data["cards"]
    rebelSpaceBattleCardList = importCombatCards(cardSet, faction, theater)
    printCardSet(rebelSpaceBattleCardList)

    # open empire space cards json file and create Empire Space tactic cards.


main()
