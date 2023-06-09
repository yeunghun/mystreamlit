import streamlit as st 
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plt

st.title("MAP")
df = pd.DataFrame(np.random.randn(500,2)/[50,50]+[37.76,-122.4],columns=['lat','lon'])
st.map(df)
# x = st.slider('Select a value')
# st.write(x, 'squared is', x*x)

rand = np.random.normal(1, 1, size=20)
fig, ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)
