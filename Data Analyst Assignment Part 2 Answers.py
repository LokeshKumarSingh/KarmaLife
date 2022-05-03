#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing libraries
import numpy as np
import pandas as pd


# ### Question 1: Some of the orders are stored in another csv file named `bigkart_newsales`. Read the csv file, store it in a data frame and add it to the `bigkart_sales` data frame. Find the total sales value of the category 'Office Supplies' after combining the dataframes 

# In[30]:


bigkart_sales = pd.read_csv('bigkart_sales.csv')
bigkart_newsales = pd.read_csv('bigkart_newsales.csv')
# bigkart_sales = bigkart_sales.merge(bigkart_newsales, on = 'Order ID', how = 'outer')


# In[31]:


bigkart_sales.shape


# In[32]:


dataframes = [bigkart_sales, bigkart_newsales]

main_frame = pd.concat(dataframes,axis=0,ignore_index=True, sort=False)
main_frame.groupby(by='Category').Sales.sum()


# #### So the total sales value of the category 'Office Supplies' is 7970
# 

# ### Question 2: There are some duplicate rows in the data frame. Drop these rows and calculate the total sales value of the category Office Supplies.

# In[33]:


main_frame.drop_duplicates(subset=None,keep='first',inplace = True)
main_frame.groupby(by='Category').Sales.sum()


# #### After dropping the duplicate rows. the total sales value of the category Office Supplies is 6964.

# ### Question 3: Find the most profitable category and sub category combination based on the net profit.

# In[34]:


main_frame.groupby(by=['Category','Sub-Category']).Profit.sum()


# #### The most profitable category and sub category combination based on net profit is Technology-Phones

# ### Question 4: How many invalid order IDs are there in the data frame. An order id is of the form AZ-2011-Y where Y represents a whole number. A Order ID is said to be valid only if Y consists of 7 digits. Find the number of invalid order order IDs in the data frame.

# In[35]:


main_frame['Order no']=main_frame['Order ID'].str.split('-')
main_frame['Order no']=main_frame['Order no'].apply(lambda x: x[2])
main_frame['no_of_digits']=main_frame['Order no'].apply(lambda x: len(x))
main_frame['no_of_digits'].value_counts()


# #### The number of invalid order id is 7.

# ### Question 5: Find the top 25 orders based on sales value and find the number of orders which belong to furniture category.

# In[36]:


top_25=main_frame.sort_values(by='Sales', ascending=False)
top_25=top_25.iloc[:25,]
top_25['Category'].value_counts()


# #### So in the top 25 orders based on sales value, Office Supplies category has 11 orders, Technology category has 9 orders and Furniture category has 5 orders.

# ### Question 6: Among the orders with sales>250 and profit>50, find the product name of the fourth highest order based on sales value.

# In[40]:


highest_order=main_frame.loc[(main_frame['Sales']>250) & (main_frame['Profit']>50)]
highest_order=highest_order.sort_values(by='Sales',ascending=False) 
print(highest_order)


# #### The product name of the fourth highest order based on sales value is 'Motorola Headset, with Caller ID'

# ### Question 7: Remove the orders with negative profit by dropping the corresponding rows with negative `Profit`. Find the product that makes the lowest profit per Quantity in the Technology category.

# In[38]:


lowest_profit=main_frame[main_frame.Profit>0]
lowest_profit=lowest_profit.loc[lowest_profit.Category=='Technology']
lowest_profit['Profit_per_qty']=lowest_profit['Profit']/lowest_profit['Quantity']
lowest_profit.sort_values(by='Profit_per_qty',ascending=True)


# #### After removing product with negative profit, The product that makes the lowest profit per quantity in the Technology category is 'Logitech Keyboard, Programmable' with profit per quantity value of '7.333333'
