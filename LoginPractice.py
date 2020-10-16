from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

usernameStr = 'andreas.bauer@cognizant.com'
passwordStr = 'Andrew'
text = 'Authentication failed'

browser = webdriver.Safari()
browser.get(('http://automationpractice.com/index.php?controller=authentication'))

username = browser.find_element_by_id('email')
username.send_keys(usernameStr)

password = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID, 'passwd')))
password.send_keys(passwordStr)
 
signInButton = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID,'SubmitLogin')))


browser.execute_script("arguments[0].click();", signInButton)

time.sleep(7)

if (text in browser.page_source):
    print("Roman")
else:
    print("Chuong")


#driver.quit()



