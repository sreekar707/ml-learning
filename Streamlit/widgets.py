import streamlit as st
import pandas as pd
st.title("Streamlit Text Input")
name=st.text_input("Enter Your Name: ")
if name:
    st.write(f"Welcome, {name}!")
    
age=st.slider("Select your age: ",20,120,18)
st.write(f"Your age is {age}")


languages = ["MALAYALAM", "HINDI", "ENGLISH", "TAMIL", "TELUGU"]
choices = st.selectbox("Choose your native language", languages)
st.write(f"You picked {choices}")



st.write("Random Dataframe flexx")
data={
    "NAME" : ["Sreekar","Jane","Jack","Jacob"],
    "AGE" :  ["40","30","50","60"],
    "LOCATION" : ["Texas","Chicago","Los Angeles","Kannur"]
}
df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)




uploaded_file=st.file_uploader("Choose a csv file",type="csv")

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)