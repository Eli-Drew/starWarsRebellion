"""
=================================================
Author:         Drew Rinker
Date:           12/10/2022

Defines Space Combat Card.
=================================================
"""


class CombatCard(object):

    def __init__(self, faction, name, descriptionTop, descriptionBottom, vehicleBonus):
        self.faction = faction
        self.name = name
        self.descriptionTop = descriptionTop
        self.descriptionBottom = descriptionBottom
        self.vehicleBonus = vehicleBonus

    # Getters and Setter methods
    def getFaction(self):
        return self.faction

    def setFaction(self, newFaction):
        self.faction = newFaction

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getDescriptionTop(self):
        return self.descriptionTop

    def setDescriptionTop(self, newDescriptionTop):
        self.descriptionTop = newDescriptionTop

    def getDescriptionBottom(self):
        return self.descriptionBottom

    def setDescriptionBottom(self, newDescriptionBottom):
        self.descriptionBottom = newDescriptionBottom

    def getVehicleBonus(self):
        return self.vehicleBonus

    def setVehicleBonus(self, newVehicleBonus):
        self.vehicleBonus = newVehicleBonus

    def __str__(self):
        line1 = "=" * 10
        line2 = "| " + str(self.name) + "\n"
        line3 = "| " + str(self.descriptionTop) + "\n"
        line4 = "| " + str(self.descriptionBottom) + "\n"
        line5 = "| " + str(self.vehicleBonus) + "\n"
        return line1 + line2 + line3 + line4 + line5
