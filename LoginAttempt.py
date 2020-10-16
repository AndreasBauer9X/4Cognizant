from requests import Session
from bs4 import BeautifulSoup as bs
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class insertNameNPassword:
        
        def __init__(self,websiteLink):
                self.websiteLink = websiteLink
                self.checker = True
                self.browser = None
                self.payload = {}
                
                
        def handleInformationInput(self,key,infoItself):
                if infoItself == "quit":
                        return False
                else:
                        self.payload[key] = infoItself
                        return True
                

        def prepareBrowser(self,websiteLink):
                browser = webdriver.Safari()
                #browser.get(('http://automationpractice.com/index.php?controller=authentication'))
                browser.get((websiteLink))

                username = browser.find_element_by_id('email')
                username.send_keys(self.payload.get("email"))

                password = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID, 'passwd')))
                password.send_keys(self.payload.get("passwd"))

                print("\nYou will now be attempted to be logged-in. \nPlease be patient for a few seconds.")
                signInButton = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'SubmitLogin')))

                browser.execute_script("arguments[0].click();", signInButton)
                print("\nPlease wait a couple of seconds. Your login is being verified...!")

                return browser
        

        def check4FailedLogin(self,browser):

                text = 'Authentication failed'
        
                if (text in browser.page_source):
                        print("I'm sorry, but your login failed due to a wrong E-mail address or password.\nPlease try again!")
                        browser.quit()
                        return False
                else:
                        print("Your login was successful!")
                        return True
                
        
        def eingabe(self):
                print("In the following, please insert name and password.\nYou can cancel the login by typing 'quit'.\n")
                while self.checker:
                        payload = {}
                        if self.checker:
                                un = input("\nPlease type your E-Mail address:  ")
                                self.checker = self.handleInformationInput("email",un)

                        if self.checker:

                                pw = input("\nPlease type your password:  ")
                                self.checker = self.handleInformationInput("passwd",pw)

		
                        if self.checker:
                                self.browser = self.prepareBrowser(self.websiteLink)

                                time.sleep(7)

                                self.check4FailedLogin(self.browser)
