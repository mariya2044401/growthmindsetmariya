#streamlit
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title= "growth mindset project", project_icon="💥")
st.title("Growth Mindset Challenge: web App with Streamlit")

st.header("Welcome to Your Growth Journey!")
st.write("Embarace challenges,learn from mistakes,and Unlock your full potential.This AI-poweed app helps you build a growth mindset with reflection,challenges and achievements!")

#quote section
st.header("Today's Growth Mindset Quote")
st.write("Success is not a final, failure is not fatal:it is the courage to continue that counts." "-Winston Churchill")

st.header("What's your Challenge Today?")
user_input=st.text_input("Describe the Challenge you're facing:")

#Condition
if user_input:
    st.success(f"You are facing: {user_input}. Keep pushing forward towards your goal")
else:
    st.warning("Tell us about your challenge to get started!")

#reflexing
st.header("Reflection on your learning")
reflection = st.text_area("Reflect on your learning and challenges:")

if reflection:
    st.success(f"Great insight! Your reflection: {reflection}")
else:
    st.info("Reflecting on past experience help you grow!Share your difficulties")

    #achievements
    st.header("Achievements Celebrarte you r wins!")
    achievement = st.text_input("Share something you've recently accomplished")

    if achievement:
        st.success(f"Congratulations! You've achieved: {achievement}")
    else:
        st.info("Celebrating your achievements can help you stay motivated")

 #footer
st.write ( "- - -")  
st.write  ("Keep believin g  in  yourself.  Growth is a journey, not a destination!")
st.write ("**Created by Mariya khan**")
     


 

