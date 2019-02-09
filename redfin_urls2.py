from selenium import webdriver


#import redfin_starter as rd 

import pandas as pd


driver = webdriver.Chrome()
driver.get('https://www.redfin.com/county/1898/NJ/Gloucester-County')

#copied xpath from chrome; driver.find_element_by_xpath('//a[@href="'+url+'"]') not working 
button = driver.find_element_by_xpath('//*[@id="MapHomeCard_0"]/div/div/a')  
button.click()


print("Scraping page...")

#address = driver.find_elements_by_xpath('.//span[@class="street-address"]')[0].text
#print(address)	

driver.close() 


