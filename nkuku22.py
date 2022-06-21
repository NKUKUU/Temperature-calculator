#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
st.title( """temperature calculator""")
st.header("creator NKUKU")
fahrenheit= st.number_input("enter tempereture")
celcius=(fahrenheit-32)*5/9
st.write("% 2f fahrenheit is: % 0.2f celsius" % (fahrenheit,celcius))

st.subheader("Sign In")
username="nkuku"
password="124"
x=st.text_input("enter username :")
y=st.number_input("enter password:")
if x==username and y==password:
    st,write("yes")
else:
    st.write("no")
    
