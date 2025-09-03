from bs4 import BeautifulSoup
from selenium import webdriver
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

web_page = response.text
soup=BeautifulSoup(web_page,"html.parser")
properties_adress=[]
all_properties = soup.find_all(name="ul",class_="List-c11n-8-84-3-photo-cards")
for all_properties_list in all_properties: 
    properties_adress_list = soup.find(name="a",class_="StyledPropertyCardDataArea-anchor")
    pr=properties_adress_list.getText()
    properties_adress.append(pr)

    
print(all_properties)






