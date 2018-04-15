# Ingestion

> Read the movie data
	
	import numpy as np
	import pandas as pd
	movies = pd.read_csv('./movie_data/movies.csv', sep=",")
	print('OBJECT Type: ', type(movies)) # show the first 5 entries
	print(movies.head()) # show the first 5 entries

> Read the tags data

	tags = pd.read_csv('./movie_data/tags.csv', sep=",")
	print(tags.head())

> Read the ratings data

	ratings = pd.read_csv('./movie_data/ratings.csv', sep=",", parse_dates=['timestamp'])
	print(ratings.head())

> Read the links data

	links = pd.read_csv('./movie_data/links.csv', sep=",")
	print(links.head())

> For Current analysis, we will remove timestamp (We will come back to it)

	del ratings['timestamp']
	del tags['timestamp']


## DATA STRUCTURES

### Series

> extract 0th row: notice that it is a series

	row_o = tags.iloc[0]
	print(type(row_o))
	print(row_o)
	print(row_o.index)
	print(row_o['userId']) # 15
	print('rating' in row_o) # is rating an index in row_o (false)
	print("Row Name:",row_o.name)

> rename the row_o
	
	row_o = row_o.rename('first_row')
	print("New Row Name:", row_o.name)


### DataFrames

> get sme shots of tags

	print(tags.head())
	print(tags.index)
	print(tags.columns)

> Extract row 0, 11, 22 from the dataframe

	rowsz = tags.iloc[[0, 11, 22]]
	print("rowsz:\n", rowsz)


## Descriptive Statistics

> describe() : Shows the summary statistics of a dataframe

> Example

	print(ratings['rating'].describe())

> corr() : Computes pairwise Pearson coefficient (p) of columns

> Example

	print(ratings.corr())

> Other Methods: .min() .max() .mode() .median()

> Example

	print(ratings['rating'].max())
	print(ratings['rating'].mode())

> .any() : returns whether ANY element is True

	* Benefits
		Can Detect if a cell matches a condition very quickly

> Example:

	filter1 = ratings['rating'] > 5
	filter1.any()

> .all() : returns whether ALL elements are True

	* Benefits
		Can Detect if a column or row matches a condition very quickly

> Example:

	filter2 = ratings['rating'] > 0
	filter2.any()

> Other Methods: .Count() .Clip() .Rank() .Round()

	https://pandas.pydata.org/pandas-docs/stable/genindex.html