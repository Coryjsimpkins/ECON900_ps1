from bs4 import BeautifulSoup
import os
import glob
import pandas as pd

if not os.path.exists("parsed_files"):
	os.mkdir("parsed_files")

# df = pd.DataFrame(columns=['scrapping_time','short_name','name','market_cap','price','volume','supply','24H_change'])
df = pd.DataFrame()

one_file_name = "boardgamegeek1.html" 
#for one_file_name in glob.glob("html_files/*.html"):
print("parsing " + one_file_name)
#scrapping_time = os.path.splitext(os.path.basename(one_file_name))[0].replace("coinmarketcap","")
f = open(one_file_name, "r", encoding="utf8")
soup = BeautifulSoup(f.read(), 'html.parser')
f.close()
games_table = soup.find("table", {"id": "collectionitems"})
games_tbody = games_table.find("tbody")
game_rows = games_tbody.find_all("tr", {"id": "row_"})

for r in game_rows:
	game_rank = r.find("td", {"class": "collection_rank"}).text
	game_name = r.find("td", {"class": "collection_objectname"}).find("a").text
	game_year = r.find("td", {"class": "collection_objectname"}).find("span", {"class": "smallerfont dull"}).text
	game_rating_data = r.find_all("td", {"class": "collection_bggrating"})
	geek_rating = game_rating_data[0].text
	avg_rating = game_rating_data[1].text
	num_votes = game_rating_data[2].text
	list_price = r.find("td", {"class": "collection_shop"}).find("div").text



print(list_price)




		# currency_name = r.find("td", {"class": "currency-name"}).find("a",{"class":"currency-name-container"}).text
# 		currency_market_cap = r.find("td", {"class": "market-cap"})['data-sort']
# 		currency_price = r.find("a",{"class": "price"}).text
# 		currency_volume = r.find("a",{"class": "volume"}).text
# 		currency_supply = r.find("td", {"class": "circulating-supply"})['data-sort']
# 		currency_change = r.find("td", {"class": "percent-change"})['data-sort']
# 		# print(scrapping_time)
# 		# print(currency_short_name)
# 		# print(currency_name)
# 		# print(currency_market_cap)
# 		# print(currency_price)
# 		# print(currency_volume)
# 		# print(currency_supply)
# 		# print(currency_change)
# 		# print("\n")
# 		df = df.append({
# 			'scrapping_time': scrapping_time, 
# 			'short_name': currency_short_name,
# 			'name': currency_name,
# 			'market_cap': currency_market_cap,
# 			'price': currency_price,
# 			'volume': currency_volume,
# 			'supply': currency_supply,
# 			'24H_change': currency_change
# 			}, ignore_index=True)



# # print(df)
# df.to_csv("parsed_files/coinmarketcap_dataset.csv")

