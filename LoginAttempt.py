from requests import Session
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def insertNameNPassword(websiteLink):
	print("In the following, please insert name and password.\nYou can cancel the login by typing 'quit'.\n")

	checker = 1

	while bool(checker):

		payload = {}
	
		un = input("\nPlease type ypur E-Mail address:  ")

		if un == "quit":
			checker = 0
		else:
			payload["email"] = un

		if bool(checker):

			pw = input("\nPlease type your password:  ")

			if pw == "quit":
				checker = 0
			else:
				payload["passwd"] = pw

		
		if bool(checker):
                        DRIVER_PATH = "/usr/share/man/man1"
			driver = webdriver.Safari(executable_path=DRIVER_PATH)
			driver.implicitly_wait(10)
			driver.get("http://automationpractice.com/index.php?controller=authentication")
			driver.find_element_by_id("email").clear()
			driver.find_element_by_id("email").send_keys(payload.get("email"))
			driver.find_element_by_id ("passwd").clear()
			driver.find_element_by_id ("passwd").send_keys(payload.get("passwd"))
			loginBut = driver.find_element_by_id("SubmitLogin")
			loginBut.send_keys("\n")
			
