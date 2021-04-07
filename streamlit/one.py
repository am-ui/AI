#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st


# In[2]:


import numpy as np


# In[3]:


st.title("this is my first app")
st.header("header")
st.subheader("sub header")
st.text("This is about basic tutorials of streamlit")
st.markdown(""" # h1 tag
##h2 tag
###h3 tag
:moon: <br>
:sunglass: <br>
**bold** <br>
_italic_

""", True)

st.latex(r''' a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
     \sum_{k=0}^{n-1} ar^k =
     a \left(\frac{1-r^{n}}{1-r}\right)''')
d ={
    "name":"Harsh",
    "language":"Python",
    "topic":"Streamlit"
} 
st.write(d)


# In[ ]:




