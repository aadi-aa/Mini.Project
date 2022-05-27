#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
sns.set(color_codes=True)


# In[8]:


weather = pd.read_csv('Test.csv')


# In[9]:


weather.head()


# In[10]:


weather.info()


# In[11]:


plt.figure(figsize = (20, 4))
sns.barplot(x='humidity', y='temperature',data=weather)


# In[23]:


sns.displot(weather['humidity'],kde=True)


# In[19]:


sns.displot(weather['humidity'], kde=False, rug=True);


# In[24]:


sns.jointplot(data=weather,x='humidity', y='temperature')


# In[25]:


sns.jointplot(data=weather,x='humidity',y='temperature', kind="hex")


# In[26]:


sns.jointplot(data=weather,x='humidity', y='temperature',kind="kde")


# In[27]:


sns.pairplot(weather[['humidity', 'temperature', 'air_pollution_index']])


# In[28]:


sns.stripplot(x=weather['weather_type'],y=weather['temperature'])


# In[29]:


sns.stripplot(x=weather['weather_type'], y=weather['temperature'], jitter = True)


# In[39]:


plt.figure(figsize = (40, 4))
sns.swarmplot(x=weather['humidity'],y=weather['temperature'])


# In[44]:


plt.figure(figsize = (20, 8))
sns.boxplot(x=weather['humidity'],y=weather['temperature'], hue=weather['weather_type'])


# In[46]:


plt.figure(figsize = (20, 4))
sns.barplot(x='humidity',y='temperature', hue='weather_type',data=weather)


# In[47]:


sns.countplot(x='weather_type',data=weather)


# In[51]:


plt.figure(figsize = (20, 8))
sns.pointplot(x='humidity', y='temperature', hue='weather_type',data=weather)


# In[52]:


sns.lmplot(x="humidity", y="temperature", data=weather)


# In[53]:


sns.lmplot(x="humidity", y="temperature", hue="weather_type", data=weather)


# In[ ]:




