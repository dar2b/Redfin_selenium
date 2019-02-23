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
details_page_info_headers = ['Price', 'Beds', 'Bath', 'Town' 'Square feet', '$ per Sq. Ft.', 'Property Value', 'County']	 
writer.writerow(details_page_info_headers)								## The counties should be compared. Should I have county data included and seperated for the dataset(s)? Included 'county'.

for url in list_of_search_result_urls:
	# Go to the page that we want to scrape								#other values first then table 
	driver.get(url)

	resi_estate={}
	
	try: 
		## Need MLS ID for primary key 
		button = driver.find_element_by_xpath('.//span[@class="bottomLink font-color-link"]')		              ## MLS ID should come first in script 
		button.click()
		mls_id = driver.find_elements_by_xpath("//div[@class='source-info font-b2 font-color-gray-light']").text    #span[@class='header font-color-gray-light font-weight-roman']/ .. taking the wrong class 
		print(mls_id)
	except:
		pass  


	try:
		product_price = driver.find_element_by_xpath("//div[@class='info-block price']").text
		
		resi_price = product_price.strip('b \n $ Price')    					
		resi_price_ = resi_price.strip(' \n Listed at price ').strip('Last Sol')
		resi_price_2 = resi_price_.replace(',', '')
		int_resi_price = resi_price_2

		print('\n' + int_resi_price)
		resi_estate['Price'] = int_resi_price       			#.encode('utf-8')
		
		bed_dict={}
		bed = driver.find_element_by_xpath("//div[@class='info-block']/div[@class='statsValue']").text
		print('Bed ' + bed)
		resi_estate['Beds'] = bed

		bath = driver.find_element_by_xpath("//div[@data-rf-test-id='abp-baths']/div[@class='statsValue']").text
		print('Bath ' + bath) 
		resi_estate['bath'] = bath

		town_name = driver.find_element_by_xpath("//span[@itemprop='addressLocality']").text
		town_name_edit= town_name.strip(',')
		#town_name = town_or_community.strip('\n Community')
		print(town_name_edit)
		#resi_estate['town'] = town_name_edit

	
		sq_feet = driver.find_element_by_xpath("//div[@class='info-block sqft']").text	

		sq_feet_split = sq_feet.split('$' )											## how do you seperate the string and make it into two variables? Removed the dollar sign. 
		square_footage = sq_feet_split[0] 
		square_foot_dollar = sq_feet_split[1]
		square_foot_total = square_footage.replace('Sq. Ft.' , '')					#.strip was not working on this function. Why? 
		square_foot_noline =  square_foot_total.strip(' \n')
		square_foot_comma = square_foot_noline.replace(',' ,'')	
		dollar_per = square_foot_dollar.strip('/ Sq. Ft.')	

		print('Sq FT and $/per : ' + square_foot_comma, dollar_per)
		resi_estate['sq feet'] = square_foot_comma
		resi_estate['sq_feet_per_$'] = dollar_per
	

	###### historical pricing or time series -- delete from here down to use script ######
	#try: 
		button = driver.find_element_by_xpath('.//span[@class="bottomLink font-color-link"]')		              
		button.click()																					
		table = driver.find_element_by_xpath('.//table[@class="basic-table-2"]').text      
		table_2 = table.split('\n')
		print(table_2)
		date = table_2[1]
		print(date)
		mls_price = table_2[3].strip('BRIGHT')
		print(mls_price)


		no_button_table = driver.find_element_by_xpath('.//tr[@class="PropertyHistoryEventRow"]') 			##This xpath is not taking the home's pricing information that does not have a full table or button
		print(no_button_table)
	#except:
	#	pass  

		prop = driver.find_element_by_xpath("//div[@class='tax-table']").text
		prop_format= prop.strip('$ Land ').split('\n')
		property_val_no_comma = prop_format[0].replace(',','')
		additions_price = prop_format[1].replace(',','').strip('$ Additions')
		total_taxable_value	= prop_format[2].replace(',','').strip('$ Total')
		#prop_strip = prop_format.split('$ ') 

		print(property_val_no_comma)
		resi_estate['property value'] = property_val_no_comma
		print(additions_price)
		print(total_taxable_value)

		MLS = driver.find_elements_by_xpath("//div[@class='keyDetail font-size-base']")[7].text	
		MLS = town_or_community.strip('\n ')
		print(MLS)
		#town_or_community = driver.find_elements_by_xpath("//div[@class='keyDetail font-size-base']")[1].text		
		#town_name = town_or_community.strip('\n Community')
		#print(town_name)
		#resi_estate['town'] = town_name

		county_type = driver.find_element_by_xpath("//span[@class='content font-weight-roman']/a[@href]").text	
		print(county_type)
		resi_estate['county'] = county_type
	except:
		pass


	##resi_price = "289,900 \n Listed on price"

	##resi_price_ = resi_price.strip(' \n Listed on price ')
	##resi_price_2= resi_price_.replace(',', '')

	##int_resi_price = int(resi_price_2)

	##int_resi_price

	##plt.hist(list_of_asset_details, bins=5000)
	
	#plt.scatter(list_of_asset_details, list_of_asset_details)



	#####real esate historical pricing 

	#property_value = driver.find_element_by_xpath("//div[@class='no-break-inside'/li[@class='entryItem']").text          #xpath for property value not scraping 
	#print('acres' + property_value)


	#dollar_per_sqft = driver.find_element_by_xpath("//div[@data-rf-test-id='abp-sqFt']").text
	#print('Dollar per sq foot ' + dollar_per_sqft)
	#acres_num = driver.find_elements_by_xpath("//span[@class='content font-weight-roman']")[5].text 
	#print(acres_num)
	
	
	writer.writerow(resi_estate.values())    ## What is the purpose of coverting into a dataframe?


	
##cap rate = noi / value 


###20,000.00	purchase price
##11,000.00	5% down payment
##6,600.00	3% closing costs
##17,600.00	cash at closing


### sum and scrape loan information for debt serviced 
##pd.Dataframe(price_dict)


csv_file.close()
driver.close()
