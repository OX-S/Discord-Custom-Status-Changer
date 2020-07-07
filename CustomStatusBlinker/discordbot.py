from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from configparser import ConfigParser
from webdriver_manager.chrome import ChromeDriverManager


file = 'config.ini'
config = ConfigParser()
config.read(file)

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get("https://discord.com/login")
email = driver.find_element_by_xpath("//input[@name=\"email\"]")
email.send_keys(config['login']['email'])
password = driver.find_element_by_xpath("//input[@name=\"password\"]")
password.send_keys(config['login']['password'])
password.send_keys(Keys.RETURN)
time.sleep(9)
n = 5
while n > 0:
	driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div/div[1]").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[6]/div/div/div/div/div[7]").click()
	time.sleep(1)
	status = driver.find_element_by_xpath("/html/body/div/div[6]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/input")
	status.clear()
	status.send_keys(config['messages']['message1'])
	status.send_keys(Keys.RETURN)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div/div[1]").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[6]/div/div/div/div/div[7]").click()
	time.sleep(1)
	status = driver.find_element_by_xpath("/html/body/div/div[6]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/input")
	status.clear()
	status.send_keys(config['messages']['message2'])
	status.send_keys(Keys.RETURN)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div/div[1]").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[6]/div/div/div/div/div[7]").click()
	time.sleep(1)
	status = driver.find_element_by_xpath("/html/body/div/div[6]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/input")
	status.clear()
	status.send_keys(config['messages']['message3'])
	status.send_keys(Keys.RETURN)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div/div[1]").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[6]/div/div/div/div/div[7]").click()
	time.sleep(1)
	status = driver.find_element_by_xpath("/html/body/div/div[6]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/input")
	status.clear()
	status.send_keys(config['messages']['message4'])
	status.send_keys(Keys.RETURN)
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[2]/div/div[2]/div/div/div/div[2]/div[1]/section/div/div[1]").click()
	time.sleep(1)
	driver.find_element_by_xpath("/html/body/div/div[6]/div/div/div/div/div[7]").click()
	time.sleep(1)
	status = driver.find_element_by_xpath("/html/body/div/div[6]/div[2]/div/div/div[2]/div[1]/div/div/div[2]/input")
	status.clear()
	status.send_keys(config['messages']['message5'])
	status.send_keys(Keys.RETURN)
	time.sleep(1)
	
