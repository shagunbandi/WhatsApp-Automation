from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import time

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
print("Scan QR Code, And then Enter")
input()
print("Logged In")

contact = input("Enter The Contact Name: ")
# text = input("Enter the text")

selected_contact = driver.find_element_by_xpath("//span[@title='"+contact+"']")
selected_contact.click()

inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
input_box = driver.find_element_by_xpath(inp_xpath)
time.sleep(2)

text = 'a'

while True:

	text += 'a'
	input_box.send_keys(text + Keys.ENTER)
	# time.sleep(1)

driver.quit()
