from sklearn import linear_model
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 

dataset = pd.read_csv("parsed_files/boardgamegeek_dataset.csv")

#print (dataset.head(20))

trainer = dataset[dataset.avg_price.notnull()]
trainer = trainer.dropna()

target = trainer.avg_price.values

#print(target)

data = trainer[['avg_rating', 'geek_rating', 'game_rank', 'game_year', 'num_votes']].copy()

plt.scatter(data['avg_rating'], trainer['avg_price'])
plt.savefig('scatter.png')

#print(data)

regression = linear_model.LinearRegression()

regression.fit(data, target)


test = dataset.loc[dataset['avg_price'].isnull()]

X = test[['avg_rating', 'geek_rating', 'game_rank', 'game_year', 'num_votes']].copy()

X = X.dropna()

#print(X)
#print(len(X))
#print(len(data))
#print(trainer.head(20))

results = regression.predict(X)

plt.scatter(X['avg_rating'], results)
plt.savefig('predicted_scatter.png')

print(results)