from selenium import webdriver
import time
import csv


driver = webdriver.Chrome() 

urls = ['https://www.redfin.com/county/1898/NJ/Gloucester-County/page-', 'https://www.redfin.com/county/1894/NJ/Camden-County/page-']


#index = 0 
#while index <= 2:

try:
	for url in urls:
		for page in range(1, 2):								
			driver.get(url) #+ str(page)) 
			print(url)
			#print(page)

			csvfile = open('search_results.csv', 'w')								#search_results.csv is resetting and rewriting for each URL. 
			writer = csv.writer(csvfile)
			search_results_urls_header = ['url']   
			writer.writerow(search_results_urls_header)

			#elems = driver.find_elements_by_xpath('//div[@class="homecardv2"]/a[@href]')

			pages = driver.find_elements_by_xpath('//div[@class="viewingPage"]/span[@class]')[0].text
			num1 = pages.strip('Viewing page 1 o')
			num = num1.strip('f ')
			int_num = int(num)
			upper = int_num - 1 
			index = 1
			while index <= upper:       

				try:
					print("Scraping Page number " + str(index)) #to show count number in terminal 
					#index = index + 1
					
					elems = driver.find_elements_by_xpath('//div[@class="homecardv2"]/a[@href]')

					
					for elem in elems: 
						home_link={} 
						#elems = driver.find_elements_by_xpath('//div[@class="homecardv2"]/a[@href]')
						home_link['url'] = elem.get_attribute('href')
						writer.writerow(home_link.values())
							
					button = driver.find_elements_by_xpath('//button[@class="clickable buttonControl button-text"]')[-1] #bug on page 17 to 18 Gloucester County, dublicates data
					button.click()
					time.sleep(2)
					index = index + 1

				except Exception as e:
					print(e)
					csvfile.close()
					driver.close() 
					break 
except Exception as e:
	print(e)
	


# one of the loops are allowing the button to click through the 18 pages 