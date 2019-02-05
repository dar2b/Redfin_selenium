from selenium import webdriver
import time

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome()
# Go to the page that we want to scrape
driver.get("https://www.redfin.com/NJ/West-Deptford/877-Dante-Ct-08051/home/36494417")

# Click review button to go to the review section
#estimate_button = driver.find_element_by_xpath('//*[@id="content"]/div[6]/div[4]/div/div/div/div/div[4]/a')

#estimate_button = driver.find_element_by_xpath("//a[@class='navigation-link ']/@href") 

#estimate_button.click()



print("\nScraping page..")

reviews = driver.find_elements_by_xpath('.//span[@class="street-address"]').text

print(reviews)				#trying to print out the first part of list is sending garbage 

price = driver.find_elements_by_xpath('.//div[@class="statValue"]').text

print(price)

numbed = driver.find_elements_by_xpath('.//div[@class="statValue"]')

print(numbed) 
driver.close() 


#git hub line for errors 