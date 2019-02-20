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
details_page_info_headers = ['Price', 'Beds', 'Bath']		## Headers are not alligning with columns. Why? 
writer.writerow(details_page_info_headers)

for url in list_of_search_result_urls:
	# Go to the page that we want to scrape					#other values first then table 
	driver.get(url)

	resi_estate={}
	product_price = driver.find_element_by_xpath("//div[@class='info-block price']").text
	resi_price = product_price.strip('b \n $ Price')    #remove $ ... how do you remove " "  around price ?
	print('\n' + resi_price)
	resi_estate['Price'] = resi_price       #.encode('utf-8')
	
	bed_dict={}
	bed = driver.find_element_by_xpath("//div[@class='info-block']/div[@class='statsValue']").text
	print('Bed ' + bed)
	resi_estate['Beds'] = bed

	bath = driver.find_element_by_xpath("//div[@data-rf-test-id='abp-baths']/div[@class='statsValue']").text
	print('Bath ' + bath) 
	resi_estate['bath'] = bath

	sq_feet = driver.find_element_by_xpath("//div[@class='info-block sqft']").text		
	print(sq_feet)
	resi_estate['sq_feet'] = sq_feet



	###### historical pricing or time series -- delete from here down to use script ######
	#button = driver.find_element_by_xpath('.//span[@class="bottomLink font-color-link"]')		#button erroring when not avaiable to click on first page 
	#button.click()


	## Need MLS ID for primary key 
	#mls_id = driver.find_elements_by_xpath("//span[@class='content font-weight-roman']").text    span[@class='header font-color-gray-light font-weight-roman']/ .. taking the wrong class 
	#print(mls_id)

	table = driver.find_element_by_xpath('.//table[@class="basic-table-2"]').text      
	print(table)


	#####real esate historical pricing 

	#property_value = driver.find_element_by_xpath("//div[@class='no-break-inside'/li[@class='entryItem']").text  #xpath for property value not scraping 
	#print('acres' + property_value)


	#dollar_per_sqft = driver.find_element_by_xpath("//div[@data-rf-test-id='abp-sqFt']").text
	#print('Dollar per sq foot ' + dollar_per_sqft)
	#acres_num = driver.find_elements_by_xpath("//span[@class='content font-weight-roman']")[5].text 
	#print(acres_num)
	
	
	writer.writerow(resi_estate.values()) 


	
##cap rate = noi / value 


###20,000.00	purchase price
##11,000.00	5% down payment
##6,600.00	3% closing costs
##17,600.00	cash at closing


### sum and scrap loan information for debt serviced 
##pd.Dataframe(price_dict)


csv_file.close()
driver.close()
