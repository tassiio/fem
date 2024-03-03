import streamlit as st
import st_pages as stp
import pandas as pd
from PIL import Image
from streamlit_drawable_canvas import st_canvas

stp.add_indentation() 

st.title("Текстовые форматы")

st.title('1) *st.title()*: формат заголовков, используемый для именования слайдов;')
st.divider()
st.header('2) *st.header()*: формат заголовков, но чуть поменьше;')
st.divider()
st.subheader('3) *st.subheader()*: формат подзаголовков;')
st.divider()
st.markdown('4) *st.markdown()*: отображает текст в формате языка разметки *Markdown*;')
st.divider()
st.caption('5) *st.caption()*:  формат, используемый для подписи рисунков;')
st.divider()
st.code('''6) st.code(): 
print("Формат, используемый для вставок строк кода. Язык по умолчанию — Python.")''')
st.divider()
st.text('7) st.text(): формат, выравнивающий текст по ширине;')
st.divider()
'8) *st.latex():*'
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.latex(r'''
    \lim\limits_{x \to 0} \frac{\sin{x}}{x} = \text{?}
    ''')


'''Подробно ознакомиться с каждым форматом, а также узнать о других интересных 
пользовательских пакетах можно по ссылке https://docs.streamlit.io/library/api-reference/text.'''

'''### *Бонус*. Например, можно писать вот так:'''


# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])

realtime_update = st.sidebar.checkbox("Update in realtime", True)

    

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=150,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)
if canvas_result.json_data is not None:
    objects = pd.json_normalize(canvas_result.json_data["objects"]) # need to convert obj to str because PyArrow
    for col in objects.select_dtypes(include=['object']).columns:
        objects[col] = objects[col].astype("str")
    st.dataframe(objects)
