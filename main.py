import pandas as pd
import numpy as np
import difflib     #to compare the moviename from the movie input as the user my provide incorrectly
from sklearn.feature_extraction.text import TfidfVectorizer     #used to convert textual data into numerical numbers
from sklearn.metrics.pairwise import cosine_similarity       #used to give similarity score of the movie with other movies
#(basically it compares movie input with the other movies on the basis of numbers/points provided for similarity)

#loading the data from dataset with the help of pandas library
movies_data = pd.read_csv('/content/movies.csv')


# printing a few of the data from dataset
movies_data.head()   #The .head() method in pandas is used to quickly inspect the first few rows of a DataFrame
# finding numbwe of rowa and columns int the dataset
movies_data.shape #shape will tell us the number of rows and columns

# replacing the null valuess with null string

for feature in selected_features:
 movies_data[feature] = movies_data[feature].fillna('')

# Now let's select the features we want to compare and get suggestions on

selected_features = ['genres','keywords','tagline','cast','director']
# Restore the original print function
del print

# Now you can use the print function as intended
print(selected_features)
# Combine all the features for optimal recommendation
combine = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']+ ' ' + movies_data['tagline']
print = combine
# Fix the overwritten print function
del print

# Handle missing values in 'combine' before vectorization
combine = combine.fillna('')  # Replace NaN with empty strings

# Converting text data to feature vector
vectorizer = TfidfVectorizer()
featurevector = vectorizer.fit_transform(combine) # this just represent data into numerical form


print(featurevector)

# Similarity score for the movie
similarity = cosine_similarity(featurevector)

del print

print(similarity)

del print
print (similarity.shape) # this will give rows and columns

# movie which the recommendation is for
Moviename = input('Enter the movie name: ')


listmovietitles = movies_data['title'].tolist()
print(listmovietitles)

# Movies name

# Convert the 'Movie' column to a list
Movies = movies_data['title']

# Print the list of movies
print(Movies)

# Searching for the most optimal recommendation for the movie
close_match = difflib.get_close_matches(Moviename, Movies) #Movies here is the list of all the movies, so it will recommend the movie from the list
print(close_match)

perfect_match = close_match[0] # This will suggest the first movie
print(perfect_match)
# This is a completely optional step if only 1 movie is required

# Finding the serial number of a movie by it's title
indexofthemovie = movies_data[movies_data.title == perfect_match]['index'].values[0]
print (indexofthemovie)

# similar movies
similarmovies = list(enumerate(similarity[indexofthemovie])) # represent the title of movies with the similarity to the movie
# greater similarity points equals the more like the movie is to be recommended
print(similarmovies)
# These similarity points are based on genres, keyword, tagline, cast, director

len(similarmovies)

# Arranging the movies based on their similarity score
sortedsimilarmovies = sorted(similarmovies, key = lambda x:x[1], reverse=True) # it prints the movies that are most similar to the movie
print(sortedsimilarmovies)

len(sortedsimilarmovies)

# Print the name of the similar movies
print ('The optimal recomendation are: ')
i = 1

# Getting movies names from the index values
for movie in sortedsimilarmovies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index == index]['title'].values[0]
  if (i<11):
    print(i, '.',title_from_index)
    i+=1