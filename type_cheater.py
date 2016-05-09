#!/usr/bin/python3
import time
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys


URL = 'http://10fastfingers.com/typing-test/english'
driver = webdriver.Chrome()
driver.get(URL)
words = driver.find_element_by_xpath('//*[@id="row1"]')
input_box = driver.find_element_by_xpath('//*[@id="inputfield"]')

counter = 1
timeout = time.time() + 59   # 1 minute from now
while counter < 341:
	if time.time() > timeout:
		break;
	xpath = '//*[@id="row1"]/span[' + str(counter) + ']'
	this_word = driver.find_element_by_xpath(xpath).text
	print(this_word)
	input_box.send_keys(this_word)
	input_box.send_keys(Keys.SPACE)
	counter += 1


#driver.close()
#driver.quit()