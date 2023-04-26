#!/usr/bin/env python
# coding: utf-8

# # Spotify top 50 2019 Songs Analysis 

# ### Importing Libraries

# In[18]:


#!pip install plotly


# In[35]:


#!pip install spotipy


# In[108]:


#!pip install pytrends


# In[8]:


#!pip install chardet


# In[1]:


import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from plotly.subplots import make_subplots
import plotly.graph_objs as go
import plotly.offline as pyo
pyo.init_notebook_mode()
from pytrends.request import TrendReq


# ### Importing CSV File

# In[2]:


import csv

with open('top50.csv', encoding='latin1') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# In[3]:


df = pd.read_csv('top50.csv', encoding='latin1')
df.head()


# ### Checking shape of data set

# In[4]:


df.shape


# ### Checking null or missing values

# In[5]:


df.isna().sum()


# ### Checking info of data set

# In[6]:


df.info()


# ### Describing data set

# In[7]:


df.describe()


# ### Checking columns in the data set

# In[8]:


df.columns


# In[9]:


df.head()


# In[10]:


df.tail()


# ### Data Mining

# In[11]:


df.corr()


# ### Finding the correlation between the variables

# In[12]:


plt.figure(figsize=(15,7))
sns.heatmap(df.corr(), annot=False, fmt='.2f')


# In[13]:


# With annotation
plt.figure(figsize=(20,10))
# Displaying graph
sns.heatmap(df.corr(), annot=True, fmt='.2f')


# ### Scatter Plot - Relationship between popularity and other numerical features

# In[14]:


# Visualize the relationship between popularity and other numerical features
sns.pairplot(df, x_vars=['Beats.Per.Minute', 'Energy', 'Danceability', 'Loudness..dB..', 'Liveness', 'Valence.', 'Length.', 'Acousticness..', 'Speechiness.'], y_vars=['Popularity'])
plt.show()


# ### Analysing the relationship between energy and loudness

# In[15]:


fig=plt.subplots(figsize=(8,8))
sns.regplot(x='Energy',y='Loudness..dB..',data=df,color='black')


# ## Data Exploration/Visualization

# ### Finding the most popular genres

# In[16]:


df['Genre'].value_counts()


# In[17]:


px.histogram(df, x='Genre',color='Genre',text_auto='3s')


# In[19]:


Main_Genres = ['hip hop','jazz','reggae','techno','trap','regga','rap','r&b','rock','pop','blues']
def check_genre(sir):
    for word in Main_Genres:
        if sir.find(word) != -1:
            if word == 'rap':
                return 'hip hop'
            else:
                return word
    return sir

df['Main_Genres'] = df['Genre'].apply(check_genre)


# In[20]:


df['Main_Genres'].value_counts()


# In[21]:


px.histogram(df,x='Main_Genres',color='Main_Genres',title='Frequent of different music genre',text_auto='3s')


# ### Top 10 most popular artists

# In[22]:


top_10_artist = df['Artist.Name'].value_counts()[:10]
top_10_genres = df['Genre'].value_counts()[:10]
top_10_songs = df.iloc[df['Popularity'].nlargest(10).index,:]
top_10_artist.to_frame()
top_10_songs


# ### Gender Analysis 

# In[23]:


gender = {'Ed Sheeran':'Male','Shawn Mendes':'Male','Post Malone':'Male','Sech':'Male','Marshmello':'Male','J Balvin':'Male', 'Lil Nas X':'Male',
          'Daddy Yankee':'Male','Y2K':'Male','DJ Snake':'Male','Lewis Capaldi':'Male','Chris Brown':'Male','Khalid':'Male','Lizzo':'Female','Lauv':'Male',
          'Kygo':'Male','Ali Gatie':'Male','Bad Bunny':'Male','Lunay':'Male','Sam Smith':'Male','Anuel AA':'Male','Nicky Jam':'Male','Lil Tecca':'Male',
          'Young Thug':'Male','Martin Garrix':'Male','Jhay Cortez':'Male','Drake':'Male','MEDUZA':'Male','Maluma':'Male',
          
          'The Chainsmokers':'Group','Jonas Brothers':'Group',
          
          'Billie Eilish':'Female','Ariana Grande':'Female','Lady Gaga':'Female','ROSALÍA':'Female','Katy Perry':'Female','Tones and I':'Female','Taylor Swift':'Female'
         }
df['Artist_Gender'] = df['Artist.Name'].apply(lambda x: gender[x])


# In[24]:


df['Artist_Gender'].value_counts()


# In[25]:


px.histogram(df,x='Artist_Gender',color='Artist_Gender',text_auto='3s',title='Artist Gender analysis')


# # Google Trends

# In[26]:


pytrends = TrendReq(hl='en-US', tz=360)


# In[27]:


search_terms = ['Spotify Top 50']
start_date = '2019-01-01'
end_date = '2021-01-01'
pytrends.build_payload(search_terms, timeframe=f'{start_date} {end_date}')


# In[28]:


trends_data = pytrends.interest_over_time()


# In[41]:


plt.plot(trends_data.index, trends_data['Spotify Top 50'])
plt.xlabel('Date')
plt.ylabel('Search Interest')
plt.title('Google Trends Search Interest for "Spotify Top 50"')
plt.show()


# In[45]:


search_terms2 = ['pop']
start_date2 = '2019-01-01'
end_date2 = '2021-01-01'
pytrends.build_payload(search_terms2, timeframe=f'{start_date2} {end_date2}')


# In[46]:


trends_data2 = pytrends.interest_over_time()


# In[47]:


plt.plot(trends_data.index, trends_data2['pop'])
plt.xlabel('Date')
plt.ylabel('Search Interest')
plt.title('Google Trends Search Interest for "Pop"')
plt.show()


# In[33]:


search_terms3 = ['Billie Eilish']
start_date3 = '2019-01-01'
end_date3 = '2021-01-01'
pytrends.build_payload(search_terms3, timeframe=f'{start_date3} {end_date3}')


# In[139]:


trends_data3 = pytrends.interest_over_time()


# In[142]:


plt.plot(trends_data.index, trends_data3['Billie Eilish'])
plt.xlabel('Date')
plt.ylabel('Search Interest')
plt.title('Google Trends Search Interest for "Billie Eilish"')
plt.show()

