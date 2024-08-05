import streamlit as st
import numpy as np
import pandas as pd




st.title("HELLO GUYS")


## display a single text
st.write("this is a simple text")


## create a dataframe
df=pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

## displaying the df
st.write("here is the dataframe")
st.write(df)

## creating linechart

chart_data=pd.DataFrame(np.random.randn(20,3),columns=["a",'b','c'])

st.line_chart(chart_data)

