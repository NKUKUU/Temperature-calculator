#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title( """temperature calculator""")
st.header("creator NKUKU")
fahrenheit= st.number_input("enter tempereture")
celcius=(fahrenheit-32)*5/9
st.write("% 2f fahrenheit is: % 0.2f celsius" % (fahrenheit,celcius))

