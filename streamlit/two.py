#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np


# In[2]:


data = pd.read_csv("titanic.csv")


# In[10]:


st.dataframe(data,width=600, height=600)
st.write(data)


# In[12]:


@st.cache
def ret_time(a):
    time.sleep(5)
    return time()

if st.checkbox("1"):
    st.write(ret_time(1))
    
if st.checkbox("2"):
    st.write(ret_time(2))


# In[11]:


X = dict(data)
st.json(X)


# In[ ]:




