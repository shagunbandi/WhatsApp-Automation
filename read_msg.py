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

while True:

	try:
		selected_contact = driver.find_element_by_xpath("//span[@class='OUeyt']")
		selected_contact.click()

		time.sleep(2)

		last_msg_div = driver.find_elements_by_xpath("//div[@class='_3_7SH _3DFk6']")[-1]
		last_msg_div = last_msg_div.find_elements_by_xpath("//div[@class='MVjBr _3e2jK']")[-1]
		last_msg_div = last_msg_div.find_elements_by_xpath("//div[@class='Tkt2p']")[-1]
		last_msg_div = last_msg_div.find_elements_by_xpath("//div[@class='_3zb-j']")[-1]
		last_msg = last_msg_div.find_elements_by_xpath("//div[@class='_3zb-j']")[-1]

		inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
		input_box = driver.find_element_by_xpath(inp_xpath)
		text = last_msg.text
		print(last_msg)
		input_box.send_keys(text + Keys.ENTER)
		time.sleep(2)
	except:
		time.sleep(5)

input("Enter to Exit")
driver.quit()
