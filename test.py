from selenium import webdriver
import time
import csv


driver = webdriver.Chrome() 

driver.get('https://www.redfin.com/county/1898/NJ/Gloucester-County')


csvfile = open('search_results.csv', 'w')
writer = csv.writer(csvfile)
search_results_urls_header = ['url']   # What is this line and where are the actual URLs written? 
writer.writerow(search_results_urls_header)




pages = driver.find_elements_by_xpath('//div[@class="viewingPage"]/span[@class]')[0].text
num1 = pages.strip('Viewing page 1 o')
num = num1.strip('f ')
int_num = int(num)

index = 0
while index <= int_num:
	try:
		print("Scraping Page number " + str(index))
		

		elems = driver.find_elements_by_xpath('//div[@class="homecardv2"]/a[@href]')

		for elem in elems: 
			home_link={} 
			home_link['url'] = elem.get_attribute('href')
			writer.writerow(home_link.values())
			
		button = driver.find_element_by_xpath('//button[@class="clickable buttonControl button-text"]')
		button.click()
		time.sleep(2)
		index = index + 1


	except Exception as e:
		print(e)
		csvfile.close()
		driver.close() 
		break 