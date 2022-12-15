"""
Author:     Drew Rinker
Date:       12/15/2022

Information passing class
"""

class CombatInfoScreenData(object):

    def __init__(self, planet, attackingFaction, rebelLeaders, empireLeaders, empireSpaceUnits, rebelSpaceUnits, empireGroundUnits, rebelGroundUnits):
        self.attackingFaction = attackingFaction
        self.planet = planet
        self.rebelLeaders = rebelLeaders
        self.empireLeaders = empireLeaders
        self.empireSpaceUnits = empireSpaceUnits
        self.rebelSpaceUnits = rebelSpaceUnits
        self.empireGroundUnits = empireGroundUnits
        self.rebelGroundUnits = rebelGroundUnits

