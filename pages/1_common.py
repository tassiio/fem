import streamlit as st
from streamlit_lottie import *
import st_pages as stp
from PIL import Image

stp.add_indentation() 


st.header('Что такое Streamlit и с чем его едят?')

st.image(Image.open('pages/figs/logo_dark.png'))

# _left, mid, _right = st.columns(3)
# 
# with mid:
#    st.image("./gifs/streamlit.gif")
st.markdown(
    """
    Streamlit - это фреймворк для веб-программирования на Python, 
    который позволяет разработчикам создавать интерактивные веб-приложения. Он предназначен для 
    упрощения процесса разработки и развертывания приложений, которые обрабатывают и визуализируют данные.

    Streamlit предоставляет набор инструментов для создания пользовательского интерфейса, 
    обработки данных и визуализации. Он также поддерживает интеграцию с различными 
    библиотеками Python, такими как Pandas, NumPy и Matplotlib, 
    что позволяет легко работать с данными и создавать интерактивные графики и диаграммы.

    ### Ссылки:
    - Страница проекта: [streamlit.io](https://streamlit.io)
    - Документация: [documentation](https://docs.streamlit.io)
    - Форум сообщества: [community forums](https://discuss.streamlit.io).

"""
)
