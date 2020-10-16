from requests import Session
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def insertNameNPassword(websiteLink):
	print("In the following, please insert name and password.\nYou can cancel the login by typing 'quit'.\n")

	checker = 1

	while bool(checker):

		payload = {}
	
		un = input("\nPlease type your E-Mail address:  ")

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
                        
                        text = 'Authentication failed'

                        browser = webdriver.Safari()
                        browser.get(('http://automationpractice.com/index.php?controller=authentication'))

                        username = browser.find_element_by_id('email')
                        username.send_keys(payload.get("email"))

                        password = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'passwd')))
                        password.send_keys(payload.get("passwd"))
 
                        signInButton = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'SubmitLogin')))


                        browser.execute_script("arguments[0].click();", signInButton)
                        print("Please wait a couple of seconds. Your login is being verified...!")
                        time.sleep(7)

                        if (text in browser.page_source):
                                print("I'm sorry, but your login failed due to a wrong E-mail address or password.\nPlease try again!")
                                browser.quit()
                        else:
                                print("Your login was successful!")
