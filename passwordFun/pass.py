from asyncio.windows_events import NULL
import random
import os.path
#import cryptography
from tkinter import * 
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import pyperclip as pc

# import numpy

#Program to generate random keys for passwords

dictAddy = "./passDict.txt"

#len == 26
alphaL = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
         #97   98   99   100  101  102  103  104  105  106  107  108  109
         #110  111  112  113  114  115  116  117  118  119  120  121  122
#len == 26
alphaU = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
         'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
         #65   66   67   68   69   70   71   72   73   74   75   76   77
         #78   79   80   81   82   83   84   85   86   87   88   89   90
#len == 10
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#       48   49   50   51   52   53   54    55   56   57
#len == 8
special = ['!', '@', '#', '$', '%', '^', '&', '*']
#           33   64   35   36   37   94   38   42
#char list
charList = [alphaL, alphaU, nums, special]
# Big Dict has three inner arrays
# 1. Password number
# 2. Password plaintext
# 3. Name
bigDict = [[], [], []]


# The first character changing function
# TBH no idea what the character changing means. Don't wanna deal with it
def changeChar(c):
    if len(c) != 1:
        print("Char Error")
        return NULL
    if ord(c) >= 65 and ord(c) <= 90:
        return chr(round((ord(c) << 2) / 16) + 37)
    if ord(c) >= 97 and ord(c) <= 122:
        return chr((ord(c)  >> 2) + 75)
    if ord(c) == 33 or ord(c) == 35 or ord(c) == 36 or ord(c) == 37 or ord(c) == 38 or ord(c) == 42:
        return chr(ord(c) << 1)
    if ord(c) == 64 or ord(c) == 94:
        return chr( (ord(c) >> 1) + 1)
    if ord(c) >= 48 and ord(c) <= 57:
        return chr( ord(c) + 20 )
# End changeChar(c)

# Same as above
# Similar functions that don't make sense
def changeChar2(c):
    if len(c) != 1:
        print("Char Error")
        return NULL
    if ord(c) >= 65 and ord(c) <= 90:
        return chr(round((ord(c) << 2) / 14) + 37)
    if ord(c) >= 97 and ord(c) <= 122:
        return chr((ord(c)  >> 2) + 75)
    if ord(c) == 33 or ord(c) == 35 or ord(c) == 36 or ord(c) == 37 or ord(c) == 38 or ord(c) == 42:
        return chr( (ord(c) << 2) - 50 )
    if ord(c) == 64 or ord(c) == 94:
        return chr( (ord(c) >> 1) + 3)
    if ord(c) >= 48 and ord(c) <= 59:
        return chr( ord(c) + 25 )
# End changeChar2(c)

# for c in nums:
#    print(changeChar2(c))

# Just joins the characters in an array returns a string
def makeStr(s):
    return "".join(s)

# The main making password function
# Takes a string representation of the index of each password
def makeFunc(numP):
    W = ['', '', '', '', '']
    X = ['', '', '', '', '']
    Y = ['', '', '', '', '']
    Z = ['', '', '', '', '']
    #First Set
    for i in range(0, 5):
        chosen = random.randint(0, 3)
        ofChosen = random.randint(0, len(charList[chosen]) - 1)
        W[i] = charList[chosen][ofChosen]
    #Second Set
    X[0] = changeChar(W[0])
    X[1] = changeChar(W[1])
    X[2] = changeChar(W[2])
    X[3] = changeChar(W[3])
    X[4] = changeChar(W[4])
    #Third Set 5757 words
    lines = []
    wordFile = open('C:/Users/owlma/Desktop/Notes/School_Notes/gitRepo/passwordFun/words.txt', 'r')
    lines = wordFile.readlines()
    # print( "wordFileLength == " + str(len(lines)) )
    wordFile.close()
    num = random.randint(0, len(lines))
    Y[0] = lines[num][0]
    Y[1] = lines[num][1]
    Y[2] = lines[num][2]
    Y[3] = lines[num][3]
    Y[4] = lines[num][4]

    #Fourth Set
    Z[0] = changeChar2(W[0])
    Z[1] = changeChar2(X[1])

    Z[2] = numP[0] #chr(ord(amt[lst][0]))
    Z[3] = numP[1] #chr(ord(amt[lst][1]))
    Z[4] = numP[2] #chr(ord(amt[lst][2]))

    return makeStr(W) + "-" + makeStr(X) + "-" + makeStr(Y) + "-" + makeStr(Z)
# end MakeFunc(numP)

def isCool(stinky):
    coolio = False
    length = len(stinky)
    score = 0
    
    # It's cute cus they all the same length <3
    if (length > 20):
        score = score + 0
    for i in range(0, length):
        # Numeric Representation of Char
        cat = ord(stinky[i])
        # Numbers
        if cat >= 48 and cat <= 57:
            score+=2
        # Uppercase
        if cat >= 65 and cat <= 90:
            score-=2
        # If 3 in a row match
        if i > 1 and i < length - 1:
            if ord(stinky[i-1]) == cat and ord(stinky[i+1]) == cat:
                score-=10
    if score > 0:
        coolio = True
        print("Def cool: " + str(score))
        return coolio
    elif score == 0:
        coolio = True
        print("J Chillin: " + str(score))
        return coolio
    else:
        coolio = False
        print("Not cool: " + str(score))
        return coolio
# End isCool(stinky)



def createDict():
    
    if os.path.exists(dictAddy):
        dictFile = open(dictAddy, 'r')
        lastLine = dictFile.readlines()
        fileLength = len(lastLine)
        dictText = ""
        # Set up current dictionary
        # Iterate through how many exist
        i = 0
        while i < fileLength:
            # For each number add entry to number, password, and name
            bigDict[0].append(lastLine[i][0:3])
            dictText += lastLine[i][0:3] + " "
            bigDict[1].append(lastLine[i][4:27])
            dictText += lastLine[i][4:27] + " "
            # Each password gets the name initially in the log. If empty put "noname"
            if ( len(lastLine[i]) > 28 ):
                bigDict[2].append(lastLine[i][28:len(lastLine[i])])
                dictText += lastLine[i][28:len(lastLine[i])]
            else:
                bigDict[2].append("Noname")
                dictText += "Noname\n"
            i+=1
        dictFile.close()
        newDictInTown = open(dictAddy, 'w')
        newDictInTown.writelines(dictText)
        newDictInTown.close()
        print(dictText)
        print(bigDict)
    else:
        print("No file to open... continuing on...")
    return 0
# End createDict()

def addToFile(count, name):
    passName = name
    
    stringer = ""
    numPass = 0
    count = ""+str(count)
    # Check if file exists
    # If so then open and check length
    # If length > 1000 then exit and say why
    # Also check if empty
    if os.path.exists(dictAddy):
        dictFile = open(dictAddy, 'r')
        lastLine = dictFile.readlines()
        fileLength = len(lastLine)
        # Basic check if more than 1k passwords
        if fileLength >= 999:
            print("Cannot make anymore passowrds")
            dictFile.close()
            exit()
        # Basically if the last line has nothing in it
        if fileLength == 0 or lastLine[fileLength - 1] == "" or len(lastLine[fileLength - 1]) < 3:
            numPass = "000"
        else:
            # Looks at last line and first 3 characters of dictionary to get the number
            numPass = lastLine[fileLength - 1][0:3]  
    else:
        # If doesn't exist, then create the file
        dictFile = open(dictAddy, 'w')
        numPass = "000"
    dictFile.close()

    # Second redundant check numerically out of dictionary
    manyToMake = int(numPass) + int(count)
    if manyToMake >= 1000:
        manyToMake = 999
    
    dictFile = open(dictAddy, 'a+')
    passer = ""
    j = int(numPass)
    if ( j == 0 ):
        while j < manyToMake:
            numNum = '{:0>3}'.format(j)
            passer = str(makeFunc(numNum))
            if isCool(passer):
                stringer = str(numNum) + " " + passer + " " + passName
                dictFile.write( stringer + "\n")
                print(stringer)
            else:
                cart = 0
                while not isCool(passer) and cart < 5:
                    passer = str(makeFunc(numNum))
                    cart+=1
                stringer = str(numNum) + " " + passer + " " + passName
                dictFile.write( stringer + "\n")
                print(stringer)
            j+=1
    else:
        while j < manyToMake:
            j+=1
            numNum = '{:0>3}'.format(j)
            passer = str(makeFunc(numNum))
            if isCool(passer):
                stringer = str(numNum) + " " + passer + " " + passName
                dictFile.write( stringer + "\n")
                print(stringer)
            else:
                cart = 0
                while not isCool(passer) and cart < 5:
                    passer = str(makeFunc(numNum))
                    cart+=1
                stringer = str(numNum) + " " + passer + " " + passName
                dictFile.write( stringer + "\n")
                print(stringer)

    dictFile.close()
    dictFile  = open(dictAddy, 'r')
    lastLine = dictFile.readlines()
    dictFile.close()
    
    # Code to add passwords to dictionary
    dictFile = open(dictAddy, 'a+')
    dictText = ""
    # Set up current dictionary
    # Iterate through how many exist
    i = 0
    while i < len(lastLine):
        # For each number add entry to number, password, and name
        bigDict[0].append(lastLine[i][0:3])
        dictText += lastLine[i][0:3] + " "
        bigDict[1].append(lastLine[i][4:27])
        dictText += lastLine[i][4:27] + " "
        # Each password gets the name initially in the log. If empty put "noname"
        if ( len(lastLine[i]) > 28 ):
            bigDict[2].append(lastLine[i][28:len(lastLine[i])])
            dictText += lastLine[i][28:len(lastLine[i])]
        else:
            bigDict[2].append("Noname")
            dictText += "Noname\n"
        i+=1
    dictFile.close()
    newDictInTown = open(dictAddy, 'w')
    newDictInTown.writelines(dictText)
    newDictInTown.close()
    print("Updated file and dictionary")
# End addToFile()

def findInFile(name):
    iterate = 0
    foundFile = False
    while iterate < len(bigDict[0]):
        #print(bigDict[2][iterate][0:len(bigDict[2][iterate])-1])
        if bigDict[2][iterate][0:len(bigDict[2][iterate])-1] == str(name):
            print(str(bigDict[1][iterate]))
            foundFile = True
            return
        iterate+=1
    if not foundFile:
        print("Nomenclature Error: could not find password under that name. Try again with another?")
        nomenAns = input("===============\nYes[0] or No[1]\n===============\n")
        if ( int(nomenAns) == 0 ):
            newName = input("Input new name to search for: ")
            findInFile(newName)
        elif ( int(nomenAns) == 1 ):
            print("No selected... exiting")
            exit()
        else:
            print("Input Error: exiting...")
            exit()
    else:
        print("Success: Go again?")
        nomenAns = input("===============\nYes[0] or No[1]\n===============\n")
        if ( int(nomenAns) == 0 ):
            newName = input("Input new name to search for: ")
            findInFile(newName)
        elif ( int(nomenAns) == 1 ):
            print("No selected... exiting")
            exit()
        else:
            print("Input Error: exiting...")
            exit()
# End findInFile()

def listInFile():
    
    return NULL
# End listInFile()


def inputAsk():
    genYesOr = input("Hello, welcome to the password protected dictionary!\nInput [0] to generate a password: \nInput [1] to request a password: \n<User (you)'s Input>: ")
    
    if genYesOr == NULL:
        print("Null Input Error")
        exit()
    elif int(genYesOr) == 0:
        name = input("Input a name for the password: ")
        addToFile(1, name)
    elif int(genYesOr) == 1:
        # Do search for password
        name = input("Input the name for the password: ")
        print("Searching for password")
        findInFile(name)
    else:
        print("Input Error: exiting...")
        exit()
        
# End inputAsk(count)

def setUp():
    createDict()
    inputAsk()
    
# root = Tk()
# frm = ttk.Frame(root, padding=100)
# frm.grid()
# label = ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# qButt = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
# pButt = ttk.Button(frm, text="How many passwords?", command=print("Hi")).grid(column=4, row = 0)
# print( ttk.Button.configure(self=True).keys())
# root.mainloop()

setUp()



# class App(ttk.Frame):
#     def __init__(self, container):
#         super().__init__(container)
#         # configure the root window
#         self.title = "Title"

#         # label
#         self.label = ttk.Label(self, text='Hello, Tkinter!')
#         self.label.pack()

#         # button
#         self.button = ttk.Button(self, text='Click Me')
#         self.button['command'] = self.button_clicked
#         self.button.pack()

#     def button_clicked(self):
#         addToFile()
#add rating system to vet passwords before adding to dictionary



#inputAsk(input("Input how many passwords to generate: "))

# def windowBaby():
#     window = tk.Tk()
#     # window.mainloop()
#     # window.frame()
#     app = App(window.frame)
#     app.mainloop()
# windowBaby()  