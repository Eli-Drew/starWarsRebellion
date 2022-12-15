"""
Author:     Drew Rinker
Date:       12/15/2022

entry point of app.
"""
import json

# import config.json file
with open("C:\\Users\\drewr\\Documents\\starWarsRebellion\\config.json", "r") as config:
    info = json.load(config)
pathVariables = info["variables"]

import sys
sys.path.append(pathVariables["generalVariables"]["parentDirectory"])

def main():
    pass
    # combatInfo = 


main()