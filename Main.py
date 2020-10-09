from bs4 import BeautifulSoup
import urllib.request
import re

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
    print("\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\nError: "+message+"\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")

#Greeting to explain the context
print("Good Day and welcome to the automated operating for the 'Your Logo' web store.\n\n")

#This loop will continue for as long as no recognizable input has been made
#If a value of us is inserted, the following value will be set to '0'
acceptableValueChecker = 1

while bool(acceptableValueChecker):
	#instructions
	print("How would you like to begin?\n\n")

	print("Log-in: 		To log in, please press (1)\n")

	print("Account-Creation:	To Create a new account, please press (2)\n")

	print("To quit, please type 'quit'\n")
	
	#requesting user-input based on the instructions
	command = input("Enter Command: ")

	#handling based on the input
	if command == "1":
    		print(searchLink("Sign in"))
	elif command == "2":
    		print(searchLink("Sign in"))
	elif command == "quit":
		#Since the User requested to quit, the loop will be terminated
		acceptableValueChecker = 0
	else: 
    		showError("The program does not recognise your input!")

print("\nThe program will now terminate. Goodbye!\n")