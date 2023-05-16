import streamlit as st 
import unmpy as np
import pandas as pd

st.title("Map")
df = pd.DataFrame(np.random.randn(500,2) / [50, 50] + [37.76, -122.4],columns=['lat','lon'])
st.map(df)
