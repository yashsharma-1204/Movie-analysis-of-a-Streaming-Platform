#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[9]:


df = pd.read_csv('mymoviedb.csv', lineterminator = '\n')
df.head(10)


# In[10]:


df.info()


# In[11]:


df['Genre'].head()


# In[12]:


df.duplicated().sum()


# In[13]:


df.describe()


# # Exploration Summary
#   
# ##> We have a dataframe consisting of 9827 rows and 9 columns.
# ##> our dataset looks a bit tidy with no NaNs or duplicated valus.
# ##> column needs to be casted into time and extract only the year value
# ##> Overview , Original_language and Poster-URL wouldn't be so useful during analysis, so we'll drop them.
# ##> there is noticable outlier in popularity column
# ##> Vote_average better be categorized for proper analysis.
# ##> Genre column has comma seperated value and white spaces that needs to be handled and casted into category.Exploration Summary 

# In[14]:


df.head(10)


# In[17]:


df['Release_Date'] = pd.to_datetime(df['Release_Date'])

print(df['Release_Date'].dtypes)


# In[18]:


df['Release_Date'] = df['Release_Date'].dt.year

df['Release_Date'].dtypes


# In[19]:


df.head(10)


# # Dropping the Columns

# In[20]:


cols = ['Overview', 'Original_Language', 'Poster_Url']


# In[21]:


df.drop(cols, axis = 1, inplace = True)
df.columns


# In[22]:


df.head(10)


# # categorizing vote_average columns
# 
# We would cut vote_avg values and make 4 ctegories popular average below_avg not_popular to describe it more using categorize_col() funstion provided above.

# In[27]:


def categorize_col(df, col, labels):
    edges = [df[col].describe()['min'],
             df[col].describe()['25%'],
             df[col].describe()['50%'],
             df[col].describe()['75%'],
             df[col].describe()['max']]
    df[col] = pd.cut(df[col], edges, labels = labels, duplicates = 'drop')
    return df


# In[28]:


labels = ['not_popular', 'below_avg', 'average', 'popular']

categorize_col(df, 'Vote_Average', labels)

df['Vote_Average'].unique()


# In[35]:


df.head(10)


# In[31]:


df['Vote_Average'].value_counts()


# In[36]:


df.dropna(inplace = True)

df.isna().sum()


# In[37]:


df.head(10)


# # we'd split genres into list and then explode our dataframes to have only one genre per row for each movie

# In[38]:


df['Genre'] = df['Genre'].str.split(',')
df = df.explode('Genre').reset_index(drop=True)

df.head(10)


# In[39]:


#casting column into category

df['Genre'] = df['Genre'].astype('category')

df['Genre'].dtypes


# In[40]:


df.info()


# In[41]:


df.nunique()


# In[42]:


df.head(10)


# # Data Visualization

# In[43]:


sns.set_style('whitegrid')


# # What is the most frequent genre of movies realeased on Netflix?

# In[44]:


df['Genre'].describe()


# In[47]:


sns.catplot(y = 'Genre', data = df, kind = 'count',
           order = df['Genre'].value_counts().index,
           color = '#4287f5')
plt.title('Genre column distrubtion')
plt.show()


# # Which has highest votes in vote avg column?

# In[48]:


df.head(10)


# In[50]:


sns.catplot(y = 'Vote_Average', data = df, kind = 'count',
          order = df['Vote_Average'].value_counts().index,
          color = '#4287f5')
plt.title('Votes distribution')

plt.show()


# # What movie got the highest popularity? whats the genre?

# In[51]:


df[df['Popularity'] == df['Popularity'].max()]


# # What movie got the lowest popularity? whats the genre?

# In[52]:


df[df['Popularity'] == df['Popularity'].min()]


# # Which Year has the most filmmed movies?

# In[53]:


df['Release_Date'].hist()
plt.title("Release Data column Distribution")
plt.show()


# Conclusion:
# Q1: What is the most frequent genre in the dataset?
#     Drama genre is the most frequent genre in our dataset and has appeared more than 14% of time than 19 others genre.
#     
# Q2: what genre has the highest vote?
#     We have 25.5% of our dataset with popular vote (6520 rows). Drama again gets the highest popularity among fans by 
#     being having more than 18.5% of movies.
#     
# Q3: What mpvie got the lowest popularity?
#     The United states, thread has the lowest rate in our dataset and it has genre of music, drama, 'war', 'sci-fi' and 'history'
#     
# Q4: Which year has the most filmmed movies?
#     Year 2020 has the highest filmming rate in our dataset

# In[ ]:




