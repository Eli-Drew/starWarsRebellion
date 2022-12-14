"""
Author:     Drew Rinker
Date:       12/10/2022

Space Battle Driver.

Short term: Console based
Long Term: This version is interactive gui. 
        - also want an automated version
"""

# TODO 
"""
* add 'amountInBox' to units.json
* how to factor in the action cards...? 
1. Ask user for input through GUI.
    - Who is attacking (who goes first?)
    - Can attacker move here?
        - Are they moving from an area that already has a leader?
        - Are they trying to traverse a single edge to to get to this system?
    - How many of each reinforcement is is the system.
        - Ground, space
        - Build those objects in memory
    - Leaders in the system
        - take highest value for space and ground (can be separate leaders)
            - do by faction
    - Ask about troops in each neighboring area. (determining if can retreat)
        - graph theory involved here.
        - edges and nodes. 
            - there will be 4 edges and 5 nodes for each system graph. 
            - presense of enemies (or by rules) on neighboring nodes won't allow to retreat there.

    *** Actual Battle ***
    - are there space units? 
        1. yes. cpu and player pick their tactic card
            - at first, it can be random for cpu.
            - check what units it has in system. 
                - prioritize cards that vehiclebonus vehicle is in system.
        2. reveal tactic cards.
            - carry out action of card. 
                - can be immediate or in affect at end of round
        3. roll dice.
            - attacker rolls first
            - max: 5 red, 5 black, 3 green
            - check leader space units
                - can reroll up to that number
                    - logic to determine if cpu needs to reroll or not.
                    - what to reroll as well
                    - don't want cpu to reroll random dice.
            - assign dmg. 
                - cpu will need a priority sheet. 


"""

import json
import sys

# import config.json file
with open("C:\\Users\\drewr\\Documents\\starWarsRebellion\\config.json", "r") as config:
    info = json.load(config)
pathVariables = info["variables"]
combatCards = pathVariables["cardsVariables"]["combat"]


# not sure if this sys.path is best practice for importing things or not. 
    # this path should be in the config.
sys.path.append("C:\\Users\\drewr\\Documents\\starWarsRebellion")
from src.entities.Combat_Card_Space import CombatCard
from src.entities.Dice import Dice


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
    data = readJsonCardInfo(combatCards["rebelSpaceBattleCards"])
    faction = data["faction"]
    theater = data["theater"]
    cardSet = data["cards"]
    rebelSpaceBattleCardList = importCombatCards(cardSet, faction, theater)
    printCardSet(rebelSpaceBattleCardList)

    # open empire space cards json file and create Empire Space tactic cards.
    # open ground cards next.

    # get info on what units, and what system, and what leaders are present in this combat round.


main()
