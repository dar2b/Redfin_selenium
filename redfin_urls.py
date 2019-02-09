from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import redfin_starter as redstart
import pandas as pd


urls = ['https://www.redfin.com/NJ/West-Deptford/877-Dante-Ct-08051/home/36494417', 
		'https://www.redfin.com/NJ/Williamstown/516-Waverly-Ct-08094/home/148721296', 
		'https://www.redfin.com/NJ/Williamstown/1350-Trenton-Ave-08094/home/36435557']



data1 = {}


driver = webdriver.Chrome()

for url in urls:
    for page in range(1,8):
    	driver.get(url)
    	wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div#tournamentTable tr.deactivate")))

redstart.dataProcess(data1) 