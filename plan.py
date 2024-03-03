import streamlit as st
import time
from datetime import date
from st_pages import Page, Section, show_pages, add_page_title

st.set_page_config(
    page_title="Streamlit: руководство",
    # page_icon=":sunglasses:",
)

show_pages(
    [
        Page("plan.py", "Вступление"),
        Page("./pages/1_common.py", "Общие сведения о Streamlit"),
        Section('Инструментарий'),
        Page("./pages/2_multipages.py", "Многостраничные документы"),
        Page("./pages/3_text.py", "Текстовые форматы"),
        Page("./pages/4_tables.py", "Использование таблиц"),
    ]
)

st.title('Метод конечных элементов')

st.header('**Обзор фреймворка _Streamlit_**')

today = date.today()
date_now = today.strftime("%B %d, %Y")
st.write(date_now)

""" Основной целью сегодняшнего доклада 
является первичное знакомство с фреймворком **Streamlit**. 
Мы рассмотрим базовые функции, примеры использования различных пакетов 
Python в интеграции со Streamlit."""

st.markdown(
    """
    ### План доклада:

    - общая характеристика фреймворка **Streamlit**;
    - многостраничный документ;
    - работа с текстом (markdown, LaTeX);
    - таблицы;
    - научная графика;
    - элементы графического интерфейса;
    - расчетная программа с параметрическим вводом;
    - компоновка страницы.
"""
)

auth = f"""Материалы доклада подготовлены студентами группы М23-205 Смирной Софией,
Томашевой Анастасией и Юшиным Кириллом.
"""

def stream_data():
    for word in auth.split():
        yield word + " "
        time.sleep(0.05)

if st.button("**Авторы доклада**"):
    st.write_stream(stream_data)


# 
# md = st.text_area('Type in your markdown string (without outer quotes)',
#                   "Happy Streamlit-ing! :balloon:")
# 
# st.code(f"""
# import streamlit as st
# 
# st.markdown('''{md}''')
# """)
# 
# st.markdown(md)