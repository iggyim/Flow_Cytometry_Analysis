#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df=pd.read_csv("mot2.csv")


# In[2]:


def metdat1(s):
    return s.split("_")[2]

def metdat2(x):
    var = x.split("_")[3]
    
    if var[0] == "0":
        return 0
    else:
        return int(var)
    
    


# In[3]:


df["samp"] = df["Name"].apply(metdat1)
df["rep"] = df["Name"].apply(metdat2)


# In[4]:


filt_df = df[df["rep"] != 0]


# In[5]:


filt_df["samp_num"] = filt_df["samp"].astype("category").cat.codes


# In[6]:


apc = filt_df[3::13]
fitc = filt_df[4::13]


# In[7]:


import matplotlib.pyplot as plt


# In[8]:


# In[9]:


mean_apc = apc.groupby(by="samp").mean().reset_index()
sem_apc = apc.groupby(by="samp").std()/(3**0.5)



# In[10]:


plt.scatter(apc["samp_num"], apc["Statistic"])
plt.bar(mean_apc["samp_num"], mean_apc["Statistic"], 
        color= (0,0,0,0), edgecolor= (1,0,0,1), 
        tick_label= mean_apc["samp"], yerr=sem_apc["Statistic"], capsize=5
       )

plt.show()
