"""
=================================================
Author:     Drew Rinker
Date:       12/11/2022.

Defines a fundatmental unit. Unit being the 
    minatures in the board game. (Attack/Defend
    units.) i.e.. ships and troopers.
=================================================
"""

class Unit(object):

    def __init__(self, faction, name, typeId, theater, needToBeTransported, canBeTransported, transportAmount, blackDmg, redDmg, greenDmg, shieldColor, shieldStrength, description):
        self.faction = faction
        self.name = name
        self.typeId = typeId
        self.theater = theater
        self.needToBeTransported = needToBeTransported
        self.canBeTransported = canBeTransported
        self. transportAmount = transportAmount
        self.blackDamage = blackDmg
        self.redDamage = redDmg
        self.greenDamage = greenDmg
        self.shieldColor = shieldColor
        self.shieldStrength = shieldStrength
        self.description = description

        # variables not imported from json
        self.damageTaken = 0
        self.damageRemoved = 0
        self.destroyed = False

    def assignDamage(self, amountOfDamage):
        self.damageTaken += amountOfDamage

    def assignRemoveDamage(self, amountOfDamage):
        # be careful here. i sense a bug with this.
        # make sure this removed damage is cleared once it removes damage.
        # don't want it stacking and removing too much damge.
        self.damageRemoved += amountOfDamage

    def removeDamage(self):
        self.damageTaken -= self.damageRemoved
        # reset damageRemoved to 0 once the removal has taken place
        self.damageRemoved = 0

    def isDestroyed(self):
        if self.damageTaken >= self.shieldStrength:
            return True
        else:
            return False

    def removeAllDamage(self):
        """This function is only to take place at the end of combat. Remove all damage tokens from units after combat just like in game."""
