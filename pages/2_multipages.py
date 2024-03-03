import streamlit as st
import st_pages as stp
from annotated_text import annotated_text, annotation, parameters

stp.add_indentation() 

st.title("Организация документа")

'''#### В Streamlit существует два основных способа создания многостраничных документов.
#### Рассмотрим каждый из них в отдельности.'''

st.subheader('1) Папка _pages_')

st.markdown("""
##### Данный способ использовался нашей группой при подготовке данного доклада. Cлева можно видеть список из названий созданных страниц, который удобен для быстрой навигации и отображает структуру проекта. 
##### Метки страниц в пользовательском интерфейсе боковой панели создаются на основе имен файлов. Имена файлов состоят из четырех частей: 
 - **число** (для регуляции порядка следования страниц); 
 - **разделитель** (может быть _, -, пробелом или любой их комбинацией);
 - **лейбл** (включает в себя все, что угодно, кроме расширения); 
 - **расширение** (всегда _.py_). 
 
 _Примечание_.
 Бывает крайне неудобно прописывать в названии файла заголовки слайдов, особенно на русском языке. 
 Также иногда требуется объединять определенные группы страниц в подразделы. 
 Пользовательская библиотека _st_pages_ расширяет возможности встроенного редактора многостраничных документов.""")


def hello():
    import streamlit as st
    import streamlit_lottie

    # parameters.LABEL_FONT_SIZE = 10

    # annotated_text(annotation("Приветствие", "", font_family="Comic Sans MS", border="2px dashed red"))

    hi = st.text_area('Как Вас зовут?', '')

    # st.code(f"""
    # import streamlit as st
# 
    # st.markdown('''{md}''')
    # """)
    if hi:
        st.markdown(f'Привет, {hi}! :wave:')
        #with st.echo():
        st.lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json")

    '''_Пример кода_:'''
    st.code("""
      def hello():
            import streamlit as st
            import streamlit_lottie

            hi = st.text_area('Как Вас зовут?', '')

            if hi:
                st.markdown(f'Привет, {hi}! :wave:')
                st.lottie("https://assets5.lottiefiles.com/packages/lf20_V9t630.json") """)


def counter():
    import streamlit as st

    # annotated_text(annotation("Счетчик", "", font_family="Comic Sans MS", border="2px dashed red"))
    strr = st.text_area('Впишите какую-нибудь строку:', '')

    if strr:
        st.write(f'Количество символов в строке: {len(strr)}.')
    
    '''_Пример кода_:'''
    st.code("""
        def counter():
            import streamlit as st

            strr = st.text_area('Впишите какую-нибудь строку:', '')

            if strr:
                st.write(f'Количество символов в строке: {len(strr)}.') """)


def buttons():
    import streamlit as st

    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button(":rainbow[Шарики!!!]:balloon::balloon::balloon:"):
            st.balloons()
    with col2:
        if st.button('Котики!!!:cat::cat::cat:'):
            st.page_link("https://catgdp.streamlit.app/", label="Значит идем к котикам!", icon="🐈")
        # annotated_text(annotation("Кнопочки", "", font_family="Comic Sans MS", border="2px dashed red"))
    with col3:
        if st.button(":blue[Снег!!!]:snowman::snowman::snowman:"):
            st.snow()

    '''_Пример кода_:'''
    st.code(""" 
        def buttons():
            import streamlit as st

            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button(":rainbow[Шарики!!!]:balloon::balloon::balloon:"):
                    st.balloons()
            with col2:
                if st.button('Котики!!!:cat::cat::cat:'):
                    st.page_link("https://catgdp.streamlit.app/", label="Значит идем к котикам!", icon="🐈")
            with col3:
                if st.button(":blue[Снег!!!]:snowman::snowman::snowman:"):
                st.snow()""")



st.subheader('2) _st.selectbox_')

st.markdown("""
##### Данная функция предоставляет пользователю возможность выбора интересующей его страницы из выпадающего списка на боковой панели. Если в предыдущем случае каждая страница — отдельный файл, то здесь для каждой страницы создается собственная функция. Рассмотрим следующие примеры. """)

page_names_to_funcs = {
    "Приветствие": hello,
    "Счетчик": counter,
    "Кнопки": buttons,
}

demo_name = st.sidebar.selectbox("Выберите подстраницу:", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()


