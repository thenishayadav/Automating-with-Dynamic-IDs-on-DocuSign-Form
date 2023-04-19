import logging
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

# Authentication
password=input("Enter your Gmail App password :")
s.login('email.com', password)
while(True):
   options = webdriver. ChromeOptions()
   #options.add_argument("--headless")
   options.add_experimental_option( "prefs",{'profile.managed_default_content_settings.javascript': 1})
   driver = webdriver. Chrome(chrome_options=options, executable_path=r'C:\Users\ASUS\PycharmProjects\seleniumtest1\Driver\chromedriver.exe')
   driver.get("https://tracker-suivi.apps.cic.gc.ca/en/dashboard")
   driver.find_element(By.XPATH,'//*[@id="uci"]').send_keys("  ")
   driver.find_element(By.XPATH,'//*[@id="password"]').send_keys("  ")
   ActionChains(driver).send_keys(Keys.ENTER * 2).perform()
   time.sleep(5)




   # creates SMTP session


   # message to be sent
   SUBJECT = "Hourly Update on your application"
   TEXT = driver.find_element(By.XPATH,'/html/body/app-root/app-loading/div/app-shell/main/app-dashboard/div/section[1]').text+"\n\n"+driver.find_element(By.XPATH,'/html/body/app-root/app-loading/div/app-shell/main/app-dashboard/div/section[2]').text
   message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
   # sending the mail
   s.sendmail('email.com', 'email.com', message)
   # terminating the session
   s.quit()
   time.sleep(3600)