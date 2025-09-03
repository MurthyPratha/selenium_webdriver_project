from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#Create and configure the Chrome Web Driver.
driver = webdriver.Chrome(options=chrome_options)

#Navigation
driver.get("https://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME,value="fName")
f_name.send_keys("murhty",Keys.ENTER)

l_name = driver.find_element(By.NAME,value="lName")
l_name.send_keys("p",Keys.ENTER)

mai = driver.find_element(By.NAME,value="email")
mai.send_keys("murthy@gmail.com",Keys.ENTER)