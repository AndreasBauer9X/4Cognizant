from bs4 import BeautifulSoup
import urllib.request
import re
from LoginAttempt import insertNameNPassword
from CreateAccount import askForUserData

#This function searches the Link with the specified text

def searchLink(linkText):
	html_page = urllib.request.urlopen("http://automationpractice.com/index.php")
	soup = BeautifulSoup(html_page)

	for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
		
		if link.text is not None:
			if linkText in link.text:
				return link['href']
		
#prints a striking error message
def showError(message):
        errormessage = "\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: "+message+"\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        return errormessage

def handleFirstStepInput(command):
        #handling based on the input
        if command == "1":
                loginLink = searchLink("Sign in")
                la = insertNameNPassword(loginLink)
                la.eingabe()
                return True
        elif command == "2":
                loginLink = searchLink("Sign in")
                ca = askForUserData(loginLink)
                ca.informationInsertion()
                return True
        elif command == "quit":
                #Since the User requested to quit, the loop will be terminated
                return False
        else: 
                print(showError("The program does not recognise your input!"))
                return True


        
acceptableValueChecker = True
#Greeting to explain the context
print("Good Day and welcome to the automated operating for the 'Your Logo' web store.\n\n")
        
#This loop will continue for as long as no recognizable input has been made
#If a value of us is inserted, the following value will be set to '0'

while acceptableValueChecker:
        #instructions
                
        print("How would you like to begin?\n\n")

        print("Log-in: 		To log in, please press (1)\n")

        print("Account-Creation:	To Create a new account, please press (2)\n")

        print("To quit, please type 'quit'\n")

        #requesting user-input based on the instructions
        command = input("Enter Command: ")
                
        acceptableValueChecker = handleFirstStepInput(command)
                
print("\nThe program will now terminate. Goodbye!\n")
