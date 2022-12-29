"""
Author:     Drew Rinker
Date:       12/22/22

Second attempt at a gui. The aim is to be more organized and look better.
"""
from tkinter import *
import json
from CombatInfoScreenData import CombatInfoScreenData

# import config.json file
with open("C:\\Users\\drewr\\Documents\\starWarsRebellion\\config.json", "r") as config:
    info = json.load(config)

class BaseApp(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.frame = None
        self.switch_frame(Combat)

        # TODO
        # Do i need to keep track of variables and such here? not sure how passing info works. 

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.frame is not None:
            self.frame.destroy()
        self.frame = new_frame
        self.frame.pack()

class Combat(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Combat Information")
        self.grid()

if __name__ == "__main__":
    app = BaseApp()
    app.mainloop()



