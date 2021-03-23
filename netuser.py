#This program will open a GUI and ask for an input
#the input will be passed to a command in CMD 
#the output of the command will be returned in a GUI

#easygui setup, capture an input
#first, import easygui, and assign it a seperate namespace
import easygui as g
#display an enterbox to have a user enter a string and return it

boxText = "Enter a username, it must be in the correct format, all lowercase."
boxTitle = "Net user, displays user account information."

emplidCapture = g.enterbox(boxText, boxTitle)
#emplidCapture should return whatever was entered
#testing to see if the syntax was correct by outputting the input to a msgbox
#testMSGbox = g.msgbox("You entered " + str(emplidCapture))
#emplidCapture does return whatever is in the box

#now pass the output of emplidCapture to the net user command
import subprocess
import sys

def userinfo(emplidCapture):
    #need to build the command, each argument is put into a list
    #use the captured employeeid, errors will be dealt with at a later time

    #construct the line that will be passed into cmd, each argument is one list item
    cmd = ["net.exe", "user", str(emplidCapture), "/domain"]
    #this line will actually run the command 'net user 'username' /domain' and return the results
    netuserCMD = subprocess.check_output(cmd)
    #the output here will be an item, needs to be decoded to be human readable
    results = netuserCMD.decode("ascii", errors="ignore")
    #next, need to iterate over the items using a for loop and splitlines(), then adding a new line at the end
    strResults = ""
    for line in results.splitlines():
        strResults += line
        strResults += "\n"
    
    return(strResults)

#now put the results of userinfo into a textbox
g.msgbox(msg=userinfo(emplidCapture), title="Account User Information in Domain", ok_button="OK")
