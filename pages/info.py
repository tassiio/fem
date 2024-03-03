#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:49:15 2024

@author: kirill
"""

import streamlit as st

st.title("Добро пожаловать в Streamlit!")

st.write("Streamlit - свободная Python-библиотека для быстрого создания веб-презентаций и приложений.")

st.subheader("В пару десятков строк кода вы можете:")

st.write("* Быстро превратить свою программу в красивое веб-приложение")
st.write("* Собрать работающий интерфейс с помощью готовых виджетов")
st.write("* Отрисовывать изображения, графики, LaTeX и таблицы")
st.write("***И сделать всё это интерактивным!***")

st.divider()

st.write("Для начала работы нужно установить Python и саму библиотеку:")
st.code("pip install streamlit", language='bash')

st.write("Для запуска скрипта с использованием streamlit нужно выполнить команду:")
st.code("streamlit run filename", language='bash')