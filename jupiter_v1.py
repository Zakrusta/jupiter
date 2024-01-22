#!/usr/bin/env python
# coding: utf-8

# ### TASK 1
# 
# Before exploring, there is a typo in the series for groups (Hamilia is wrong, Himalia is right) which only occured on the moon "Lysithea". This has been corrected during importing the data from the database

# In[379]:


import numpy as np
import math
import matplotlib.pyplot as plt
"""at a glance, some points
have noted
-typo in name of group for one moon, "Lysithea", which was Hamilia instead of Himalia
-using the summary stats, we can calculate each group's summary statistics (seperated by each series (indicated by column))
-there should be a correlation between period and distance(moon to jupiter)(this is by Kepler's Third Law)
-the radius of moon is the only way to determine "size" of moon (mass of moon is missing, dataset is incomplete)"""


# In[380]:


import pandas as pd
import sqlite3 as sql
connection = sql.connect("jupiter.db")
data = pd.read_sql("SELECT * FROM moons",connection)
data = data.set_index("moon")
#to fix the typo with Hamilia
data = data.replace("Hamilia","Himalia")

#list of moons, groups and vars in the data, returns a numpy array of the list
def list_of_moons():
    moon_list=data.index.to_numpy()
    return moon_list
def list_of_vars():
    var_list=data.columns.to_numpy()
    return var_list
def list_of_groups():
    group_list=data["group"].drop_duplicates().to_numpy()
    return group_list


# To find a list of moons, variables, or names for the groups of moons in the dataset, write:
# 
# - for moons, `list_of_moons()`
# - for variables, `list_of_vars()`
# - for groups, `list_of_groups()`

# In[353]:


class Moons:
    def __init__(self,name):
        # initialising Jupiter moons class by giving each moon their own value
        self.name = name
        self.period = data.loc[name][0]
        self.distance = data.loc[name][1]
        self.radius = data.loc[name][2]
        self.mag = data.loc[name][3]
        self.mass = data.loc[name][4]
        self.group = data.loc[name][5]
        self.ecc = data.loc[name][6]
        self.inclination = data.loc[name][7]
    def by_group(group):
        #divide moons by group, returns a filtered dataframe
        if group == "all":
            #if want to check generally, put "all"
            return data
        else:
            return data[data["group"]==group]


# In[374]:


#summary statistics for the variables by group
def summary(variable, group):
    data = Moons.by_group(group)
    return data[variable].describe()


# In[377]:


"""-each moon is classified into groups based on their distance to jupiter (that means we can check properties of each group)
-inclination has an effect on the period of the moon (i think)
-we could find a way to calculate mass of the moon"""


# In[347]:


#tinkering with distance and period
fig, ax = plt.subplots(1, 1, figsize=(6, 6))
ax.set_title("Period against Distance")
ax.set_xlabel("distance (km)")
ax.set_ylabel("period (days)")
x = data["distance_km"]
y = data["period_days"]
ax.scatter(x,y)
#noticing an exponential correlation
# through Kepler's Third Law, the correlation is T^2 ∝ a^3, where T is period, a is distance

#can see best fit line
a, b = np.polyfit(x**3,y**2,1)
x_sort = x.sort_values()
ax.plot(x_sort,np.sqrt(a*x_sort**3))


# In[381]:


data


# In[ ]:




