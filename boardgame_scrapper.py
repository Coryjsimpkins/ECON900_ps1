import urllib.request
import os
import time
import datetime

if not os.path.exists("html_files"):
	os.mkdir("html_files")

# for i in range(1060):
# 	current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y%m%d%H%M%S')
# 	print(str(i) + ": " + current_time_stamp)
# 	f = open("html_files/coinmarketcap" + current_time_stamp + ".html", "wb")
# 	response = urllib.request.urlopen('https://coinmarketcap.com/')
# 	html = response.read()
# 	f.write(html)
# 	f.close()
# 	time.sleep(10)

f = open("html_files/boardgamegeek1.html", "wb")
response = urllib.request.urlopen('https://boardgamegeek.com/browse/boardgame')
html = response.read()
f.write(html)
f.close()