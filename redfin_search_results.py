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
			driver.get(url + str(page)) 
			print(url)
			print(page)

			csvfile = open('search_results.csv', 'w')
			writer = csv.writer(csvfile)
			search_results_urls_header = ['url']   # What is this line and where are the actual URLs written? 
			writer.writerow(search_results_urls_header)

			#elems = driver.find_elements_by_xpath('//div[@class="homecardv2"]/a[@href]')

			pages = driver.find_elements_by_xpath('//div[@class="viewingPage"]/span[@class]')[0].text
			num1 = pages.strip('Viewing page 1 o')
			num = num1.strip('f ')
			int_num = int(num)

			index = 0
			while index <= int_num:

				#elems = driver.find_elements_by_xpath('//div[@class="homecardv2"]/a[@href]')

				try:
					print("Scraping Page number " + str(index))
					#index = index + 1
					
					elems = driver.find_elements_by_xpath('//div[@class="homecardv2"]/a[@href]')

					
					for elem in elems: 
						home_link={} 
						#elems = driver.find_elements_by_xpath('//div[@class="homecardv2"]/a[@href]')
						home_link['url'] = elem.get_attribute('href')
						writer.writerow(home_link.values())
							
					button = driver.find_element_by_xpath('//button[@class="clickable buttonControl button-text"]')
					button.click()
					time.sleep(5)
					index = index + 1

				except Exception as e:
					print(e)
					csvfile.close()
					driver.close() 
					break 
except Exception as e:
	print(e)
	


# one of the loops are allowing the button to click through the 18 pages 