#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sentiment = pd.read_csv("fear_greed_index - fear_greed_index.csv")
trader = pd.read_csv("historical_data - historical.csv")


# In[6]:


sentiment.isnull().sum()
trader.isnull().sum()


# In[7]:


sentiment.drop_duplicates(inplace=True)
trader.drop_duplicates(inplace=True)


# In[10]:


trader.columns


# In[12]:


trader['Timestamp'] = pd.to_datetime(trader['Timestamp'])
trader['date'] = trader['Timestamp'].dt.date


# In[13]:


sentiment.columns


# In[14]:


sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date


# In[15]:


data = pd.merge(trader,
                sentiment,
                left_on='date',
                right_on='date',
                how='left')


# In[16]:


data.head()


# In[22]:


daily_pnl = data.groupby(['Account','date'])['Closed PnL'].sum().reset_index()


# In[23]:


data['win'] = data['Closed PnL'] > 0

win_rate = data.groupby('Account')['win'].mean()


# In[25]:


avg_trade = data.groupby('Account')['Size Tokens'].mean()


# In[27]:


data['Side'].value_counts()


# In[29]:


data.columns


# In[33]:


data['Closed PnL'].value_counts()


# In[34]:


data['classification'].value_counts()


# In[35]:


sentiment['classification'].value_counts()


# In[36]:


data['date'].head()


# In[38]:


sentiment['date'].head()


# In[39]:


trader['Timestamp IST'] = pd.to_datetime(trader['Timestamp IST'])
trader['date'] = trader['Timestamp IST'].dt.date

sentiment['date'] = pd.to_datetime(sentiment['date']).dt.date


# In[40]:


data = pd.merge(
    trader,
    sentiment,
    left_on='date',
    right_on='date',
    how='left'
)


# In[42]:


data['classification'].value_counts()


# In[61]:


sns.boxplot(x='classification', y='Closed PnL', data=data)

plt.title("PnL Distribution by Market Sentiment")

plt.show()


# In[53]:


sns.countplot(x='classification', data=data)
plt.title("Trades by Market Sentiment")
plt.show()


# In[54]:


sns.boxplot(x='classification', y='Size USD', data=data)

plt.title("Trade Size vs Market Sentiment")

plt.show()


# In[48]:


sns.countplot(x='classification', hue='Side', data=data)


# In[50]:


data['leverage_group'] = np.where(
    data['Size USD'] > data['Size USD'].median(),
    'High Leverage',
    'Low Leverage'
)


# In[51]:


trade_count = data.groupby('Account').size()

data['trader_type'] = data['Account'].map(
    lambda x: 'Frequent' if trade_count[x] > trade_count.median()
    else 'Infrequent'
)


# In[55]:


data['trader_type'].value_counts()


# In[56]:


data['leverage_group'].value_counts()


# In[57]:


data['win'] = data['Closed PnL'] > 0


# In[58]:


win_rate = data.groupby('Account')['win'].mean()


# In[59]:


data['performance_type'] = data['Account'].map(
    lambda x: 'Consistent Winner' if win_rate[x] > 0.6
    else 'Inconsistent Trader'
)


# In[60]:


data['performance_type'].value_counts()


# In[62]:


# Insight 1

# Greed sentiment days show higher trading activity and leverage usage.


# In[63]:


# Insight 2

# Fear days have more volatile PnL results due to market uncertainty.


# In[ ]:


# Insight 3

# High leverage traders earn higher profits but face higher losses.

