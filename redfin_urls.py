from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#import redfin_starter as rd 

import pandas as pd


urls = ['https://www.redfin.com/NJ/West-Deptford/877-Dante-Ct-08051/home/36494417', 
		'https://www.redfin.com/NJ/Williamstown/516-Waverly-Ct-08094/home/148721296', 
		'https://www.redfin.com/NJ/Williamstown/1350-Trenton-Ave-08094/home/36435557']


data1 = {}


driver = webdriver.Chrome()

for url in urls:
    for page in range(1,3):
    	data = driver.get(url)
    	#wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#tournamentTable tr.deactivate")))

#dataProcess(data1)      #skipping over loop (lines 21 through 23)



dataProcess(data) 
 
	