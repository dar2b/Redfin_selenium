from selenium import webdriver
import time
import csv
import pandas as pd

# Windows users need to specify the path to chrome driver you just downloaded.
# You need to unzip the zipfile first and move the .exe file to any folder you want.
# driver = webdriver.Chrome(r'path\to\the\chromedriver.exe')
driver = webdriver.Chrome()

# read in list of urls from search result
list_of_search_result_urls = list(pd.read_csv('search_results.csv')['url'])

# create a file for details page scraping
csv_file = open('details_page_info.csv', 'w')
writer = csv.writer(csv_file)
details_page_info_headers = ['price']
writer.writerow(details_page_info_headers)

for url in list_of_search_result_urls:
	# Go to the page that we want to scrape					#other values first then table 
	driver.get(url)

	price_dict={}
	product_price = driver.find_element_by_xpath("//div[@class='info-block price']").text
	price = product_price.strip('b \n $ Price')    #remove $ ... how do you remove " "  around price ?
	print('\n' + price)
	price_dict['name'] = price       #.encode('utf-8')
	
	bed = driver.find_element_by_xpath("//div[@class='info-block']/div[@class='statsValue']").text
	print('Bed ' + bed)
	bath = driver.find_element_by_xpath("//div[@data-rf-test-id='abp-baths']/div[@class='statsValue']").text
	print('Bath ' + bath) 
	sq_feet = driver.find_element_by_xpath("//div[@class='info-block sqft']").text
	print(sq_feet)

	#acres = driver.find_element_by_xpath("//span[@data-rf-test-id='abp-lotSize']").text         # error after a few homes 
	#print('acres' + acres)
	#dollar_per_sqft = driver.find_element_by_xpath("//div[@data-rf-test-id='abp-sqFt']").text
	#print('Dollar per sq foot ' + dollar_per_sqft)
	#acres_num = driver.find_elements_by_xpath("//span[@class='content font-weight-roman']")[5].text 
	#print(acres_num)
	
	## Need MLS ID for primary key 
	#mls_id = driver.find_elements_by_xpath("//span[@class='content font-weight-roman']").text    span[@class='header font-color-gray-light font-weight-roman']/ .. taking the wrong class 
	#print(mls_id)
	writer.writerow(price_dict.values() )

csv_file.close()
driver.close()
