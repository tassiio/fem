import streamlit as st
import st_pages as stp
import pandas as pd
import numpy as np

stp.add_indentation() 
st.title('Таблицы в Streamlit. Pandas, DataFrames и st.table()')

'''#### Streamlit поддерживает интеграцию с *Pandas* и очень удобен для работы с датафреймами. Рассмотрим основной функционал для работы с различными вида таблицами. '''
'''### 1) *st.table()*'''
df = pd.DataFrame(np.random.randn(10, 5), columns=("col %d" % i for i in range(5)))

st.table(df)