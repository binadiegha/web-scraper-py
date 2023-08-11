import requests
import pandas as pd
from bs4 import BeautifulSoup



# ensure data links are not truncated
pd.set_option('display.max_colwidth', None)

# the site URL to scrape
site_url = 'https://www.rottentomatoes.com/browse/movies_in_theaters/'

# test requests
res = requests.get(site_url)

# get the soup here
soup = BeautifulSoup(res.content, 'html.parser')

# get movies
movies = soup.find_all(['a', 'div'], class_=['js-tile-link'], limit=100);

# store data of each move in a list of dictionaries
processed_movie_info = []

# get number of movies
length = len(movies)

# titles
titles = [] #empty titles list that holds titles of movies
ratings = [] #empty ratings list that holds rating of movies
posters = [] #empty url list that holds poster urls of movies

# get info for every movie and save in a dictionary
for movie in movies:
    # store each movie detail in a dictionary and append(adding) that dictionary to the processed_movie_info list => better approach :D
    # processed_movie_info.append({
    #     "title": movie.find('span', class_='p--small').string.strip(),
    #     "rating": movie.find('score-pairs')['criticsscore'] or 'N/A',
    #     "image_url": movie.find('img')['src']
    # })

    # get all movie titles and append it to titles list
    titles.append(movie.find('span', class_='p--small').string.strip())

    # get all movie ratings and append it to ratings list
    ratings.append(movie.find('score-pairs')['criticsscore'] or 'N/A' )

    # get all movie posters and append it to posters list
    posters.append(movie.find('img')['src'])
    

processed_movie_info

table = pd.DataFrame()

table['movie title'] = titles
table['movie rating(%)'] = ratings
table['movie poster link'] = posters

table.to_csv('processed_movie_info.csv')

table





