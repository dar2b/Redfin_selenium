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



print("Scraping page...")

address = driver.find_elements_by_xpath('.//span[@class="street-address"]')[0].text 

print(address)				#trying to print out the first part of list is sending garbage 

price = driver.find_elements_by_xpath('.//span[@class="statsValue"]')[0].text

print(price)

numbed = driver.find_elements_by_xpath('.//div[@class="statsValue"]')[0].text

print(numbed) 


#county = driver.find_elements_by_xpath('//*[@id="basicInfo"]/div[2]/div[1]/div[11]/div')
county = driver.find_elements_by_xpath('.//div[@class="table-value"]')[0].text

print(county) #printing a '-' instead of county 


mls = driver.find_elements_by_xpath('.//span[@class="header font-color-gray-light font-weight-roman"]')[0].text  

print(mls)   # printing 'Style' instead of MLS #

price1 = driver.find_elements_by_xpath('.//td[@class="price-col number"]')[0].text  # output: price1 is $110,000

print(price1)  

price2 = driver.find_element_by_xpath('.//td[@class="price-col number"]').text    # output is $110,000 price2 is a part of a table, can this be printed?
print(price2)

print('*' * 50) 


driver.close() 



#git hub line for errors 