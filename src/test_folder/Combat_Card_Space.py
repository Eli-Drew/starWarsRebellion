"""
=================================================
Author:         Drew Rinker
Date:           12/10/2022

Defines Space Combat Card.
=================================================
"""


class CombatCard(object):

    def __init__(self, faction, name, theater, descriptionTop, descriptionBottom, vehicleBonus):
        self.faction = faction
        self.theater = theater
        self.name = name
        self.descriptionTop = descriptionTop
        self.descriptionBottom = descriptionBottom
        self.vehicleBonus = vehicleBonus

    # Getters and Setter methods

    def getFaction(self):
        return self.faction

    def setFaction(self, newFaction):
        self.faction = newFaction

    def getTheater(self):
        return self.theater

    def setTheater(self, newTheater):
        self.theater = newTheater

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
        line1 = "=" * 50 + "\n"
        line2 = "| ***SPACE TACTIC CARD***" + "\n"
        line3 = "|" + "_" * 49 + "\n"
        line4 = "| " + str(self.name) + "\n"
        line5 = "|" + "_" * 49 + "\n"
        line6 = "| " + str(self.descriptionTop) + "\n"
        line7 = "|" + "-" * 49 + "\n"
        line8 = "| " + str(self.descriptionBottom) + "\n"
        line9 = "| " + str(self.vehicleBonus) + "\n"
        line10 = "=" * 50 + "\n"
        return line1 + line2 + line3 + line4 + line5 + line6 + line7 + line8 + line9 + line10
