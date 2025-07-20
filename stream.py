import pandas as pd
import numpy as np
import streamlit as st
st.write("hello kalyan")
x=st.text_input("which is your favourite movie ?")
st.write(f"your favourite movie is{x}")
button=st.button("click here")
data=pd.read_csv(r"C:\Users\kalyan\Downloads\adult 3.csv")
st.write(data)

char_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=["a","b","c"]
)
st.bar_chart(char_data)
st.line_chart(char_data)