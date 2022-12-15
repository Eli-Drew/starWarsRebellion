"""
Author:     Drew Rinker
Date:       12/13/2022

Lot's to do here. 

**** Erik made a good point. Remember that only 5 red, 5 black, and 3 green dice can be used in a turn.
"""
import json 
# from CombatInfoScreenData import CombatInfoScreenData
from guiTest import CombatInfoScreen


def main():

    # TODO
    # finish guiTest. 
    #  - populate the CombatInfoScreenData object that's being returned. 
    # this line gets our info needed to start combat. 
    info = ""
    CombatInfoScreen().mainloop()
    infoX = CombatInfoScreen.getCombatInfo()
    print(infoX)
    

    

if __name__ == "__main__":
    main()