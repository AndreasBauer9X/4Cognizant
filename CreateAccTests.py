from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


browser = webdriver.Safari()
browser.get(('http://automationpractice.com/index.php?controller=authentication'))

        
WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'email_create'))).send_keys("andreas.bauer@apple.com")

createButton = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.ID,'SubmitLogin')))
time.sleep(3)
browser.execute_script("arguments[0].click();", createButton)
        
print("Please wait a couple of seconds. Your request is being processed...!")
time.sleep(5)
