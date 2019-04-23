MACHINE LEARNING PROBLEM SET 1

The purpose of this project is to gather data on board games via boardgamegeek.com. The programs should be run as follows:

1. BOARDGAME_SCRAPPER.PY
	Uses the Selenium package to open a chrome browser and load each page of boardgamegeek.com's table. Once loaded, it saves the HTML files for parsing in the BOARDGAME_PARSER.PY program.

2. BOARDGAME_PARSER.PY
	Utilizes BeautifulSoup to parse HTML files from boardgamegeek.com.
	Variables:
		game_name: name of the boardgame
		game_year: year the game was released/invented
		game_rank: rank of game given by the geeks
		avg_rating: average rating (1-10) given by voters
		geek_rating: rating (1-10) given by the geeks
		num_votes: number of users who rated the game
		avg_price: average of the available prices 

3. BOARDGAME_LEARN.PY
	Uses sklearn's linear model to predict avg_price for games without listed prices.


ADDITIONAL CONTENTS
	- html_files: contains the 1060 html files scraped.
	- parsed_files: csv file of cleaned data
	- chromedriver: for Selenium
	- images: plots of data
	- Machine_Learning_Assignment: write-up for the project