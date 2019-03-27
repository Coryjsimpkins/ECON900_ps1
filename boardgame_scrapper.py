import os
from selenium import webdriver
import time


if not os.path.exists("html_files"):
	os.mkdir("html_files")


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
driver = webdriver.Chrome(options=options)

for i in range(1060):
	print("scraping page "+ str(i+1))
	driver.get('https://boardgamegeek.com/browse/boardgame/page/' + str(i + 1))
	time.sleep(3) #lets the prices load
	html = driver.page_source 
	f = open("html_files/boardgamegeek" + str(1+ i) + ".html", "w", encoding="utf8")
	f.write(html)
	f.close()