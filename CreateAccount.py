from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def askForUserData(websiteLink):
    print("Some information is required to create an account. \nPlease answer the following questions to collect this user-data.\nYou can type 'quit' at any time to cancel this process.\n\n")

    checker = 1

    userdata = {}
    
    if bool(checker):
        emadr = input("\nPlease type your E-Mail address:  ")

        if emadr is not 'quit':
            userdata["email"] = emadr
        else:
            checker = 0

    
    if bool(checker):
        fn = input("\nWhat is your first name:  ")

        if fn is not 'quit':
            userdata["firstname"] = fn
        else:
            checker = 0

    if bool(checker):
        ln = input("\nWhat is your family name:  ")

        if ln is not 'quit':
            userdata["lastname"] = ln
        else:
            checker = 0

    if bool(checker):
        checker2 = 1
        while bool(checker2):
            gndr = input("\nWhat gender do you identify (more) with?  \nFor 'male' type (1), for 'female' type 2:")

            if gndr is '1':
                userdata["gender"] = "male"
                checker2 = 0
            elif gndr is '2':
                userdata["gender"] = "female"
                checker2 = 0
            elif gndr is 'quit':
                checker2 = 0
                checker = 0
            else:
                checker = 0

    
    if bool(checker):
        pwd = input("\nPlease choose a secure password:  ")

        if pwd is not 'quit':
            userdata["password"] = pwd
        else:
            checker = 0

            
    if bool(checker):
        browser = webdriver.Safari()
        browser.get(('http://automationpractice.com/index.php?controller=authentication'))

        
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'email_create'))).send_keys(userdata.get("email"))

        createButton = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'SubmitCreate')))
        time.sleep(3)
        browser.execute_script("arguments[0].click();", createButton)
        
        print("Please wait a couple of seconds. Your request is being processed...!")
        time.sleep(5)
    
        if userdata.get("gender") is "male":
            print("Andy")
            radiobtn=WebDriverWait(browser,20).until(EC.presence_of_element_located((By.ID,"id_gender1")))
            browser.execute_script("arguments[0].click();", radiobtn)
        elif userdata.get("gender") is "female":
            print("Roman")
            radiobtn=WebDriverWait(browser,20).until(EC.presence_of_element_located((By.ID,"id_gender2")))
            browser.execute_script("arguments[0].click();", radiobtn)

        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'customer_firstname'))).send_keys(userdata.get("firstname"))
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'customer_lastname'))).send_keys(userdata.get("lastname"))
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'email'))).send_keys(userdata.get("email"))
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'passwd'))).send_keys(userdata.get("password"))

        Select(browser.find_element_by_id('days')).select_by_value('13')
        
        Select(browser.find_element_by_id('months')).select_by_value('5')
        Select(browser.find_element_by_id('years')).select_by_value('1995')

        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'firstname'))).send_keys(userdata.get("firstname"))
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'lastname'))).send_keys(userdata.get("lastname"))
    
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'address1'))).send_keys("2200 Bonforte Blvd")
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'city'))).send_keys("Pueblo")

        Select(browser.find_element_by_id('id_state')).select_by_visible_text('Colorado')

        
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'postcode'))).send_keys("81001")

        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'phone_mobile'))).send_keys("11880")
        WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'alias'))).send_keys(userdata.get("email"))

        signInButton = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'submitAccount')))


        browser.execute_script("arguments[0].click();", signInButton)

        time.sleep(7)

        if ("error" in browser.page_source):
            print("Your account could not be created for one or more reason.\nPlease close the browser and then try again!")
            browser.quit()
        else:
            print("Your login was created successfully!")

        

        
