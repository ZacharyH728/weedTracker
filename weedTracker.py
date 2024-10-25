from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

from dotenv import load_dotenv

from flask import Flask 

import requests
import time
import os

from datetime import datetime
  
app = Flask(__name__) 

load_dotenv()

firefox_options = Options()
firefox_options.add_argument('-headless')	


loginURL = 'https://patient.massciportal.com/mmj-patient/signin'
purchasesURL = 'https://patient.massciportal.com/mmj-patient/patient/purchaseHistory'
username = os.getenv('MA_MEDCARD_USERNAME')
password = os.getenv('MA_MEDCARD_PASSWORD')
timeFormat = '%m/%d/%Y %H:%M %p'
# soup = BeautifulSoup(requests.get(url).text, 'html.parser')

purchaseDict = []

def getPurchases():
	driver = webdriver.Firefox(options=firefox_options)

	driver.get(loginURL)

	usernameForm = driver.find_element(By.ID, "username")
	passwordForm = driver.find_element(By.ID, "password")

	usernameForm.send_keys(username)
	passwordForm.send_keys(password)
	passwordForm.submit()
	# print(usernameForm.)

	time.sleep(1)

	driver.get(purchasesURL)

	table = driver.find_element(By.XPATH, "//tbody")
	time.sleep(5)


	tableElements = table.find_elements(By.XPATH, "./*")


	for element in tableElements:
		rowElements = element.find_elements(By.XPATH, "./*")
		purchaseDict.append({'date': datetime.strptime(rowElements[1].text, timeFormat).timestamp(), 'amount': float(rowElements[6].text)})
	driver.quit()


@app.route("/")
def home():
	return "Hello World"

@app.route("/getLatestPurchase")
def getLatestPurchase():
	oldest = {'date': float('inf'), 'amount': 0.0}
	for purchase in purchaseDict:
		if (oldest['date'] > purchase["date"]):
			oldest = dict(purchase)
	return str(datetime.fromtimestamp(oldest['date']))

@app.route("/getTotalAmount")
def getTotalAmount():
	total = 0
	for purchase in purchaseDict:
		total += purchase['amount']
	return total

getPurchases()
print(getLatestPurchase())

if __name__ == "__main__": 
    app.run(debug=True) 

# print(latestPurchase())