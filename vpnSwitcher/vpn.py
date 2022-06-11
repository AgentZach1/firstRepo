import os
from time import sleep
import random

#Works on ubuntu or something not on windows

# List of VPN Server Codes
codeList = ["TR", "US-C", "US", "US-W", "CA", "CA-W", 
            "FR", "DE", "NL", "NO", "RO", "CH", "GB", "HK"]
vpnON = True

try:

    #connect to VPN
    os.system("windscribe connect")
    while vpnON:

        #assigning random VPN Server Code
        choiceCode = random.choice(codeList)

        #changing IP after random time period
        sleep(random.randrange(15, 30))
        print("Changing IP Address...")
        os.system("windscribe connect " + choiceCode)
except:

    #disconnect
    os.system("windscribe disconnect")
    print("Error occurred")
