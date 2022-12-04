#!/usr/bin/env python
# coding: utf-8

# # 1# Write a python program to display all the header tags from wikipedia.org.

# In[150]:


import requests
import pandas
import numpy
from bs4 import BeautifulSoup


# In[143]:


url = requests.get('https://www.wikipedia.org')


# In[144]:


soup = BeautifulSoup(url.text, 'html.parser')


# In[148]:


titles = soup.find_all(['h1','h2','h3','h4'])


# In[149]:


for header in titles:
    print(header)


# # 2#Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release)
# and make data frame.
# 

# In[152]:


page = requests.get("https://www.imdb.com/chart/top/?ref_=nv_mv_250")
page


# In[153]:


soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


# In[154]:


scraping_movies = soup.find_all('td', class_= 'titleColumn')
scraping_movies

movies = []

for movie in scraping_movies:
    movie = movie.get_text().replace('\n', "")
    movie = movie.strip(" ")
    movies.append(movie)
movies


# In[155]:


ratings = soup.find_all('td', class_= 'ratingColumn imdbRating')
ratings
Ratings = []

for rates in ratings:
    rates = rates.get_text().replace('\n', '')
    Ratings.append(rates)
Ratings


# In[156]:


year = soup.find_all('span', class_= 'secondaryInfo')
year
Release_year = []
for years in year:
    years = years.get_text().strip()
    Release_year.append(years)
Release_year


# In[158]:


import pandas as pd
data = pd.DataFrame()
data['Movies'] = movies
data['Ratings'] = ratings
data['Release_year'] = years
data.head(100)


# # 3) Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of
# release) and make data frame.
# 

# In[159]:


page = requests.get("https://www.imdb.com/india/top-rated-indian-movies/")
page


# In[161]:


soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


# In[163]:


movies = soup.find_all('td', class_ = 'titleColumn')
movies
IndianMovies = []

for movie in movies:
    movie = movie.get_text().replace('\n', "")
    movie = movie.strip(" ")
    
    IndianMovies.append(movie)
IndianMovies


# In[164]:


Year = soup.find_all('span', class_ = 'secondaryInfo')
Year
Release_year =[]

for year in Year:
    year = (year.get_text().strip())
    Release_year.append(year)
Release_year


# In[165]:


rating = soup.find_all('td', class_ ='ratingColumn imdbRating')
rating
Ratings = []

for rates in rating:
    rates = (rates.get_text().strip())
    Ratings.append(rates)
    
Ratings


# In[166]:


Data = pd.DataFrame()
Data['IndianMovies'] =movies
Data['Release_year']=year
Data['Ratings'] =rates
Data.head(100)


# # 4) Write s python program to display list of respected former presidents of India(i.e. Name , Term of office)
# from https://presidentofindia.nic.in/former-presidents.htm
# 

# In[171]:


page = requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page


# In[172]:


soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


# In[173]:


presidents = soup.find_all('div', class_ = 'presidentListing')
presidents
President_name = []
for name in presidents:
    name = (name.h3.get_text())
    President_name.append(name)
President_name


# In[ ]:


terms = ??? #Unable to scrape


# In[ ]:





# # 7) Write a python program to scrape mentioned news details from https://www.cnbc.com/world/?region=world :

# In[184]:


page = requests.get("https://www.cnbc.com/world/?region=world")
page


# In[185]:


soup7 = BeautifulSoup(page.content, 'html.parser')
(soup7.prettify())


# In[186]:


header = soup7.find_all('div', class_='LatestNews-headlineWrapper')
header

Headlines =[]
for headline in header:
    headline= headline.a.get_text()
    Headlines.append(headline)
Headlines


# In[187]:


time = soup7.find_all('time', class_='LatestNews-timestamp')
time

Time = []
for times in time:
    times= (times.get_text())
    Time.append(times)
Time


# In[ ]:





# # 8) Write a python program to scrape the details of most downloaded articles from AI in last 90 days. https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles
# Scrape below mentioned details :

# In[188]:



page = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page


# In[189]:


soup8 = BeautifulSoup(page.content, 'html.parser')
print(soup8.prettify())


# In[190]:


title = soup8.find_all('h2')
title
page_title = []
for titlename in title:
    titlename = titlename.get_text()
    page_title.append(titlename)
    
page_title


# In[191]:


author = soup8.find_all('span', 'sc-1w3fpd7-0 dnCnAO')
author


Author_name = []

for authorname in author:
    authorname = authorname.get_text()
    Author_name.append(authorname)
Author_name


# In[192]:


date = soup8.find_all('span','sc-1thf9ly-2 dvggWt')
date

published_Date = []
for dates in date:
    dates= dates.get_text()
    published_Date.append(dates)
published_Date


# # 9) Write a python program to scrape mentioned details from dineout.co.in :
# 

# In[193]:


page = requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[194]:


soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())


# In[195]:


restaurant = soup.find_all("a", class_="restnt-name ellipsis")
restaurant
Restaurant_name =[]
for name in restaurant:
    name = (name.get_text().strip())
    Restaurant_name.append(name)
Restaurant_name


# In[196]:


Cusine = soup.find_all('span', class_ ='double-line-ellipsis')
Cusine
CUSINE_name = []
for cusine in Cusine:
    cusine = (cusine.get_text().strip())
    CUSINE_name.append(cusine)
CUSINE_name


# In[197]:


Location = soup.find_all('div', class_='restnt-loc ellipsis')
Location
location_name = []
for locationname in Location:
    locationname = (locationname.get_text().strip())
    location_name.append(locationname)

location_name


# In[198]:


restaurantrating = soup.find_all('div', class_= "restnt-rating rating-4")
restaurantrating
Restaurant_rating = []
for ratings in restaurantrating:
    ratings = (ratings.get_text())
    Restaurant_rating.append(ratings)
Restaurant_rating


# In[199]:


image = soup.find_all('img' , src=True)
image
Imageurl = []
for url in image:
    print(url['src'])


# # 10-GOOGLE SCHOLAR WEB SCRAPING

# In[200]:


page = requests.get("https://scholar.google.com/citations?view_op=top_venues&hl=en")
page


# In[201]:


soup10 = BeautifulSoup(page.content, 'html.parser')
soup10


# In[202]:


Rank = soup10.find_all('td', 'gsc_mvt_p')
Rank
Ranks = []
for rank in Rank:
    rank =(rank.get_text().strip())
    Ranks.append(rank)
Ranks


# In[203]:


publications = soup10.find_all('td', 'gsc_mvt_t')
publications
Publication_name = []
for publication in publications:
    publication = publication.get_text()
    Publication_name.append(publication)
Publication_name


# In[204]:


h5index = soup10.find_all('td','gsc_mvt_n')
h5index
H5index = []
for h5 in h5index:
    h5 = h5.get_text()
    H5index.append(h5)
H5index


# In[205]:


h5median = soup10.find_all('span', 'gs_ibl gsc_mp_anchor')
h5median

H5_median = []
for H5median in h5median:
    H5median = H5median.get_text()
    H5_median.append(H5median)
H5_median


# In[ ]:




