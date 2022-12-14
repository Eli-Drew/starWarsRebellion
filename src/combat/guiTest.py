"""
Author:     Drew Rinker
Date:       12/13/2022

Just a test for the gui that takes in unit counts
and other combat information.
"""

from tkinter import *
import json
from CombatInfoScreenData import CombatInfoScreenData

# import config.json file
with open("C:\\Users\\drewr\\Documents\\starWarsRebellion\\config.json", "r") as config:
    info = json.load(config)
unitsPathVariables = info["unitsPathVariables"]

class CombatInfoScreen(Frame):
    # TODO 
    # rearrange the gui

    def __init__(self):
        Frame.__init__(self, width=1000, height=450)
        self.master.title("Combat Round Information")
        self.grid()
        self.pageTitle = Label(self, text="COMBAT")
        self.pageTitle.grid(row=0, columnspan=2)
        self.attackSentence = Label(self, text="Who's attacking?")
        self.attackSentence.grid(row=1, columnspan=2)

        # create CombatInfoScreenData object. file and class have same name. 
        self.combatInfo = CombatInfoScreenData()

        # radio buttons for who is attacking
        self.attackingVar = StringVar(value="1")
        self.empireRadioBtn = Radiobutton(self, text="Empire", variable=self.attackingVar, value="e", padx=10)
        self.empireRadioBtn.grid(row=2, column=0)
        self.rebelRadioBtn = Radiobutton(self, text="Rebels", variable=self.attackingVar, value="r", padx=10)
        self.rebelRadioBtn.grid(row=2, column=1)

        # START Leader selection
        self.leadersLabel = Label(self, text="Leaders in Combat")
        self.leadersLabel.grid(row=3)
        # perhaps read these leaders names' in from json storage.

        # path to units json files
        leaderPathVariables = info["leaderPathVariables"]
        planetPathVariables = info["planetImages"]

        # empire leaders
        self.empireLeadersList = self.getLeaders(leaderPathVariables["empireLeaders"])
        self.empireLeaderVar = Variable(value=self.empireLeadersList)
        self.empireLeaderScollBar = Scrollbar(self, orient=VERTICAL)
        self.empireLeaderListBox = Listbox(self, listvariable=self.empireLeaderVar, height=5, selectmode=EXTENDED, exportselection=False, yscrollcommand=self.empireLeaderScollBar.set)
        self.empireLeaderListBox.grid(row=4, column=0)
        self.empireLeaderListBox.bind("<<ListboxSelect>>", self.empireLeadersSelected)

        # rebel leaders
        self.rebelLeadersList = self.getLeaders(leaderPathVariables["rebelLeaders"])
        self.rebelLeaderVar = Variable(value=self.rebelLeadersList)
        self.rebelLeaderListBox = Listbox(self, listvariable=self.rebelLeaderVar, height=5, selectmode=EXTENDED, exportselection=False)
        self.rebelLeaderListBox.grid(row=4, column=1)
        self.rebelLeaderListBox.bind("<<ListboxSelect>>", self.rebelLeaderSelected)

        # START Unit info
        self.unitEntryTitle = Label(self, text="Enter amount of each unit.")
        self.unitEntryTitle.grid(row=5)
        self.empireNameLabel1 = Label(self, text="Imperial Space Units")
        self.empireNameLabel1.grid(row=6, column=0)
        self.rebelNameLabel1 = Label(self, text="Rebel Space Units")
        self.rebelNameLabel1.grid(row=6, column=1)

        # these following 'units' blocks of code could be made into a single function. 

        # empire space units
        self.dataFrameEmpireSpace = Frame(self)
        self.dataFrameEmpireSpace.grid(row=7,column=0)
        self.empireSpaceUnits = self.getUnits(unitsPathVariables["empireSpaceUnits"])
        self.displayUnits(self.empireSpaceUnits, self.dataFrameEmpireSpace)

        # rebel space units
        self.dataFrameRebelSpace = Frame(self)
        self.dataFrameRebelSpace.grid(row=7, column=1)
        self.rebelSpaceUnits = self.getUnits(unitsPathVariables["rebelSpaceUnits"])
        self.displayUnits(self.rebelSpaceUnits, self.dataFrameRebelSpace)

        self.empireNameLabel2 = Label(self, text="Imperial Ground Units")
        self.empireNameLabel2.grid(row=8, column=0)
        self.rebelNameLabel2 = Label(self, text="Rebel Ground Units")
        self.rebelNameLabel2.grid(row=8, column=1)

        # empire ground units
        self.dataFrameEmpireGround = Frame(self)
        self.dataFrameEmpireGround.grid(row=9,column=0)
        self.empireGroundUnits = self.getUnits(unitsPathVariables["empireGroundUnits"])
        self.displayUnits(self.empireGroundUnits,self.dataFrameEmpireGround)

        # rebel ground units
        self.dataFrameRebelGround = Frame(self)
        self.dataFrameRebelGround.grid(row=9,column=1)
        self.rebelGroundUnits = self.getUnits(unitsPathVariables["rebelGroundUnits"])
        self.displayUnits(self.rebelGroundUnits, self.dataFrameRebelGround)

        # submit information
        self.finalSubmissionBtn = Button(self, text="Start Combat", command=self.startCombat)
        self.finalSubmissionBtn.grid(row=10, columnspan=2)

        # image test.
        self.planetImage = PhotoImage(file="C:\\Users\\drewr\\Documents\\starWarsRebellion\\images\\planets\\hoth.gif")
        # self.planetImage = PhotoImage(file="C:\Users\drewr\Documents\starWarsRebellion\images\planets\hoth.webp")
        self.planetImageLabel = Label(self, image=self.planetImage)
        self.planetImageLabel.grid(row=11, columnspan=2)
   
            
    # START: Controllers/Model.
    # at least, i think most of these would be considered controllers.
    # not sure why i need to be able to pass the event here. i dont reference it, but without it, it doesn't work. the method apparently expects 2 arguments.
    def empireLeadersSelected(self, event):
        selectedIndexes = self.empireLeaderListBox.curselection()
        print(selectedIndexes)

    def rebelLeaderSelected(self, event):
        selectedIndexes = self.rebelLeaderListBox.curselection()
        print(selectedIndexes)

    def getLeaders(self, file):
        leaderList = []
        with open(file, "r") as leaderFile:
            leaderInfo = json.load(leaderFile)
            leaders = leaderInfo["leaders"]
            for leader in leaders:
                leaderList.append(leader["name"])
            return leaderList


    # access to dao. (json) so model...
    def getUnits(self, file):
        with open(file, "r") as unitFile:
                unitInfo = json.load(unitFile)
                units = unitInfo["units"]
                return units

    # controller
    def displayUnits(self, units, frame):     
        self.unitRow = 0
        self.unitColumn = 0
        for unit in units:
            unitName = unit["name"]
            self.unitEntryLabel = Label(frame, text=unitName)
            self.unitEntryLabel.grid(row=self.unitRow,column=self.unitColumn)
            self.unitColumn += 1
            self.unitVar = IntVar()
            self.unitEntry = Entry(frame, textvariable=self.unitVar)
            self.unitEntry.grid(row=self.unitRow,column=self.unitColumn)
            self.unitColumn += 1
            if self.unitColumn >= 4:
                self.unitColumn = 0
                self.unitRow += 1

    def startCombat(self):
        pass

    def getCombatInfo(self):
        return self.combatInfo

def main():
    CombatInfoScreen().mainloop()


if __name__ == "__main__":
    main()