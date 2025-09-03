from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

#Create and configure the Chrome Web Driver.
driver = webdriver.Chrome(options=chrome_options)
#Navigating to Wikipedia 
driver.get("https://en.wikipedia.org/wiki/Main_Page")
#Finding an anchor tag using a CSS selector. 
a_count = driver.find_element(By.CSS_SELECTOR,value="#articlecount a" )
searh=driver.find_element(By.NAME,value="search")

searh.send_keys("Python",Keys.ENTER)





