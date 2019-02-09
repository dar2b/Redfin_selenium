from selenium import webdriver
import time
import csv

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome()
#row = webdriver.Chrome()
# Go to the page that we want to scrape
driver.get("https://www.redfin.com/NJ/West-Deptford/877-Dante-Ct-08051/home/36494417")

# Click review button to go to the review section
#estimate_button = driver.find_element_by_xpath('//*[@id="content"]/div[6]/div[4]/div/div/div/div/div[4]/a')
#estimate_button = driver.find_element_by_xpath("//a[@class='navigation-link ']/@href") 
#estimate_button.click()

class redStarter: 

	print("Scraping page...")

	address = driver.find_elements_by_xpath('.//span[@class="street-address"]')[0].text 
	print(address)			
	#price = driver.find_elements_by_xpath('.//span[@class="statsValue"]')[0].text
	#print(price)
	#numbed = driver.find_elements_by_xpath('.//div[@class="statsValue"]')[0].text
	#print(numbed) 

	#county = driver.find_elements_by_xpath('//*[@id="basicInfo"]/div[2]/div[1]/div[11]/div')
	#county = driver.find_elements_by_xpath('.//div[@class="table-value"]')[0].text
	#print(county) #printing a '-' instead of county 
	mls = driver.find_elements_by_xpath('.//span[@class="header font-color-gray-light font-weight-roman"]')[0].text  
	print(mls)   # printing 'Style' instead of MLS #

	price1 = driver.find_elements_by_xpath('.//td[@class="price-col number"]')[0].text  # output: price1 is $110,000
	#print(price1)  
	#price2 = driver.find_element_by_xpath('.//td[@class="price-col number"]').text    # output is $110,000 price2 is a part of a table, can this be printed?
	#print(price2)

	print('*' * 50) 

	#price2 = driver.find_element_by_xpath('//*[@id="propertyHistory-expandable-segment"]/div[1]/div/table').text  

	#click before table 
	button = driver.find_element_by_xpath('.//span[@class="bottomLink font-color-link"]')
	button.click()



data ={}	


def dataProcess(colum): 

	csv_file = open('pricing.csv', 'w', encoding='utf-8')         #save every 500 rows of data, if a problem w script 
	writer = csv.writer(csv_file)
	
	table = driver.find_element_by_xpath('.//table[@class="basic-table-2"]').text 
	#print(table)

	for ele in table:	
		i=0
		while i>=0: 
			#dictionary to intilize for file
			colum = {}  

			colum1 = driver.find_elements_by_xpath('.//tr[@class=" PropertyHistoryEventRow"]')[i].text
			#colum = driver.find_element_by_css_selector("td:nth-child(3)").text
			
			i+=1 #counter 

			colum['price']=colum1 

			print(i) 
			print(colum)
			writer.writerow(colum.values())
		
			if i == 9: 						#  set at 8 for each column 
				break 
				driver.close()
		break 
	

dataProcess(data) 

#git hub line for errors 