MACHINE LEARNING PROBLEM SET 1

BOARDGAME_SCRAPPER.PY
	Gathers HTML pages of 1060 pages of the boardgamegeek.com board game ranking table.

BOARDGAME_PARSER.PY
	Utilizes BeautifulSoup to parse HTML files from boardgamegeek.com.
	Variables:
		game_name: name of the boardgame
		game_year: year the game was released/invented
		game_rank: rank of game given by the geeks
		avg_rating: average rating (1-10) given by voters
		geek_rating: rating (1-10) given by the geeks
		num_votes: number of users who rated the game
		avg_price: average of the available prices 

BOARDGAME_LEARN.PY
	Uses sklearn's linear model to predict avg_price for games without listed prices.
