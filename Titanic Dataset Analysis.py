#!/usr/bin/env python
# coding: utf-8

# In[22]:


#importing classes and reading file
import pandas as pd
import matplotlib.pyplot as plt
data1 = pd.read_csv(r"D:\Studies\ML\python\Titanic\train.csv")


# In[23]:


#Checking data size
len(data1)


# In[24]:


#Displaying sample data
data1.head()


# In[25]:


data1.count()


# In[26]:


#Mininum age on the passenger list
Min_Age = data1['Age'].min()
Min_Age


# In[27]:


#Maximum age on the passenger list
Max_Age = data1['Age'].max()
Max_Age


# In[28]:


#Passengers Survived
Survived = data1['Survived'].value_counts()
Survived


# In[29]:


# Percentage of passengers who survived
Percent_Survived = data1['Survived'].value_counts() * 100/len(data1)
Percent_Survived


# In[33]:


#Passengers bu sex
Gender = data1['Sex'].value_counts()
Gender


# In[34]:


#Passenger count by comparment class travelled
Class = data1['Pclass'].value_counts()
Class


# In[35]:


#Graph depicting passengers who survived against who did not
alpha_color = 0.5
Survived.plot(kind = 'bar')


# In[38]:


#Passenger by gender comparision
Gender.sort_index().plot(kind = 'bar', color = ['r','b'])


# In[39]:


#passenger travelling by class
Class.sort_index().plot(kind = 'bar', alpha = alpha_color)


# In[40]:


#passengers who survived by age
data1.plot(kind = 'scatter' , x = 'Survived', y = 'Age')


# In[44]:


#detail of passengers survived by agebins
bins = [0,10,20,30,40,50,60,70,80]
data1['Agebins'] = pd.cut(data1['Age'],bins)
data1[data1['Survived'] == 1 ]['Agebins'].value_counts().sort_index().plot(kind = 'bar')


# In[45]:


#detail of passengers who did not survive by agebins
data1[data1['Survived'] == 0 ]['Agebins'].value_counts().sort_index().plot(kind = 'bar')


# In[47]:


#passengers by agebins
data1['Agebins'].value_counts().sort_index().plot(kind = 'bar')


# In[54]:


#detail of passengers survived in first class
data1[data1['Pclass'] == 1]['Survived'].value_counts().plot(kind = 'bar')


# In[55]:


#detail of passengers survived in third class
data1[data1['Pclass'] == 3]['Survived'].value_counts().plot(kind = 'bar')


# In[57]:


#detail of male passengers who survived
data1[data1['Sex'] == 'male']['Survived'].value_counts().plot(kind = 'bar')


# In[58]:


#detail of female passengers who survived 
data1[data1['Sex'] == 'female']['Survived'].value_counts().plot(kind = 'bar')


# In[59]:


#detail of male passengers who survived in by class they travelled
data1[data1['Sex'] == 'male']['Pclass'].value_counts().plot(kind = 'bar')


# In[60]:


#detail of female passengers who survived in by class they travelled
data1[data1['Sex'] == 'female']['Pclass'].value_counts().plot(kind = 'bar')


# In[ ]:




