from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class askForUserData:

    #link from which Account-Creation begins is established with object creation
    def __init__(self,websiteLink):
        self.websiteLink = websiteLink
        #Variable to indicate whether this proceedure should be stopped is initialized
        self.checker = True
        #Dictionary in which collected data is stored
        self.userdata = {}
        self.browser = None
    
    print("Some information is required to create an account. \nPlease answer the following questions to collect this user-data.\nYou can type 'quit' at any time to cancel this process.\n\n")

    def inputEvaluation(self,key,inputInformation):
        if inputInformation == 'quit':
            #since the User has wished to quit the Account-Creation, the check-variable is set to False, so that the following steps will not be performed
            return False
        else:
            #information is written in the dictionary 
            self.userdata[key] = inputInformation
            return True

        
    def genderEvaluation(self):
        
            while True:
                gndr = input("\nWhat gender do you identify (more) with?  \nFor 'male' type (1), for 'female' type 2:")

                if gndr == '1':
                    self.userdata["gender"] = "male"
                    return True
                elif gndr == '2':
                    self.userdata["gender"] = "female"
                    return True
                elif gndr == 'quit':
                    return False
                else:
                    print("\nYour input was invalid. Please try again!")

    
    def informationInsertion(self):

        while self.checker:
            #after every input the program will see whether the user has wished to cancel. This is depicked by whether checker is true or false
            if self.checker:
                emadr = input("\nPlease type your E-Mail address:  ")
                self.checker=self.inputEvaluation("email",emadr)
    
            if self.checker:
                fn = input("\nWhat is your first name:  ")
                self.checker=self.inputEvaluation("firstname",fn)

            if self.checker:
                ln = input("\nWhat is your family name:  ")
                self.checker=self.inputEvaluation("lastname",ln)

            if self.checker:
                self.checker=self.genderEvaluation()
            
            if self.checker:
                pwd = input("\nPlease choose a secure password:  ")
                self.checker=self.inputEvaluation("password",pwd)

            if self.checker:
                self.typeAndSendInformation()
            

    def valueIntoTextFieldById(self,fieldId,value):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID,fieldId))).send_keys(value)

    def selectorById(self,selectorId,valueId):
        Select(self.browser.find_element_by_id(selectorId)).select_by_value(valueId)
        

    def selectorByText(self,selectorId,valueText):
        Select(self.browser.find_element_by_id(selectorId)).select_by_visible_text(valueText)
        
    
    def typeAndSendInformation(self):
            
            try:
                print("\nYour instructions are being executed. Please have patience for a couple of seconds....")
                self.browser = webdriver.Safari()
                
                self.browser.get((self.websiteLink))
                
                WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID,'email_create'))).send_keys(self.userdata.get("email"))
                
                createButton = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID,'SubmitCreate')))
                time.sleep(3)
                
                self.browser.execute_script("arguments[0].click();", createButton)
                
                print("Please wait a couple of seconds. Your request is being processed...!")
                time.sleep(5)
                
                if self.userdata.get("gender") == "male":
                    radiobtn=WebDriverWait(self.browser,20).until(EC.presence_of_element_located((By.ID,"id_gender1")))
                    self.browser.execute_script("arguments[0].click();", radiobtn)
                elif self.userdata.get("gender") == "female":
                    radiobtn=WebDriverWait(self.browser,20).until(EC.presence_of_element_located((By.ID,"id_gender2")))
                    self.browser.execute_script("arguments[0].click();", radiobtn)
                
                self.valueIntoTextFieldById('customer_firstname',self.userdata.get("firstname"))
                self.valueIntoTextFieldById('customer_lastname',self.userdata.get("lastname"))
                
                self.valueIntoTextFieldById('email',self.userdata.get("email"))
                self.valueIntoTextFieldById('passwd',self.userdata.get("password"))
                
                self.selectorById('days','13')
                self.selectorById('months','5')
                self.selectorById('years','1995')
                
                self.valueIntoTextFieldById('firstname',self.userdata.get('firstname'))
                self.valueIntoTextFieldById('lastname',self.userdata.get('lastname'))
                self.valueIntoTextFieldById('address1',"2200 Bonforte Blvd")
                self.valueIntoTextFieldById('city',"Pueblo")
                
                self.selectorByText('id_state','Colorado')
                
                self.valueIntoTextFieldById('postcode',"81001")
                self.valueIntoTextFieldById('phone_mobile',"11880")
                self.valueIntoTextFieldById('alias',self.userdata.get("email"))
                
                

                signInButton = WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.ID,'submitAccount')))


                self.browser.execute_script("arguments[0].click();", signInButton)

                time.sleep(7)

                print("Your account was created successfully!")

            except Exception as e:
                print("Your account could not be created for the following reason:\n\n"+str(e)+".\n\nPlease try again!")
                
                self.browser.quit()
                

        

        
