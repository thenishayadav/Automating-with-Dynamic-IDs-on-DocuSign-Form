import logging
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as Wait
from datetime import datetime
from datetime import timedelta

from selenium.webdriver.common import window
from datetime import date
s = Service(r'C:\Users\ASUS\PycharmProjects\seleniumtest1\Driver\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://powerforms-d.docusign.net/e1a2bb26-4b59-4690-80eb-e28669ccccde?env=demo&acct=ef34e020-d61c-4a39-a196-4035bf470d7a&Appellant%20or%20Attorney_UserName=Pericles%20Abbasi&Appellant%20or%20Attorney_Email=pericles@uchicago.edu&EnvelopeField_PIN=16-11-410-011-0000&EnvelopeField_AY=2020&AssessmentYear=2020&County=Cook&Township=West%20Chicago&AttyLastName=Abbasi&PINNumber=16-11-410-011-0000&NID=2739&AttyFirstName=Pericles&AttyFirmName=The%20Pericles%20Organization&AttyAddress1=6969%20West%20Wabansia%20Avenue&AttyAddress2=&AttyCity=Chicago&AttyState=IL&AttyZip=60707&AttyPhone=773-368-5423&AttyEmail=pericles@uchicago.edu&chkMultiParcel=&accountId=ef34e020-d61c-4a39-a196-4035bf470d7a")
Wait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="powerform-finish-later-callout"]/div[2]/button'))).click()
Wait(driver, 300).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="action-bar-btn-continue"]'))).click()
driver.find_element(By.XPATH,"//div[@class='doc-tab text-tab owned signing-required has-tab-error']/input").send_keys("apple")




