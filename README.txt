This is an implementation of the Also Bought Algorithm using the MovieLens Dataset.

Dataset description :
This dataset has 100,000 ratings and 1,300 tag applications applied to 9,000 movies by 700 users 
Each user has rated atleast 20 movies.

Exploratory Data Analysis outcome : There were 59 movies which have not been rated by any user. Since also bought algorithm focuses on similar items bought by other users in its recommendation calculation, these movies(items) will not feature in any recommendation and hence have been removed from consideration.

There are three main scripts :
1. item-item.py : 
This script first subsets the movies.csv file by removing the unrated movies. It then implements the following algorithm specified by Amazon for implementing item based collaborative filtering:

			For each item in product catalog, I1 
				For each customer C who purchased I1 
					For each item I2 purchased by customer C 
						Record that a customer purchased I1 and I2 
			
					For each item I2 
						Compute the similarity between I1 and I2

The first portion of the algorithm essentially calculates the co-occurence of two items. In this script, a boolean vector is created for 		 each user formed by the movie ids as vector components. The vector component is 1 if the user has rated the movie and 0 otherwise.
Thus, a user-item matrix is created. Computing the product of this matrix with the transpose of itself gives us the final co-occurence 		         count item-item matrix.

2. scripts for calculating the similarity matrix : 
The co-occurrence count item-item matrix is normalized by using similarity measures to generate similarity matrix. similarity_calc.py uses cosine similarity for computation while pearson_sim_calc.py uses pearson coefficient.The cosine similarity is computed using the cosine_similarity() function from sklearn.metrics.pairwise library. The pearson similarity is computed using corrcoef() function from numpy.
After creating the similarity matrix, the scripts extract the 10 (number can be changed) most similar movies for every movie stores them in a csv file which is used for recommendations

3. recommendations.py : This script recommends movies for a particular (user id, movie id) pair. It retrieves the movies most similar to the given movie id 	and outputs only those which have not been rated by the user.

All intermediate results like the co-occurence item-item matrix and the similar movie lists are stored as csv files.
