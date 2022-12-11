"""
Space Battle Driver
"""

import sys
import json
from entities.Combat_Card_Space import CombatCard

# just create your space battle cards and print them.
with open("rebelSpaceBattleCards.json", "r") as readFile:
    data = json.load(readFile)

rebelSpaceBattleCardList = []

for x in data:
    if x == "cards":
        for y in x:
            name = y["name"]
            newCard = CombatCard()
            rebelSpaceBattleCardList.append(newCard)

print(data)
