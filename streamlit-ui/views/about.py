import streamlit as st
from PIL import Image
from app.st_functions import st_button

class About:
    class Model:
        pageTitle = "About"

    def view(self, model):
        # st.title(model.pageTitle)

        st.write(
            "[![Star](https://img.shields.io/github/stars/kyledinh/slowblood.svg?logo=github&style=social)](https://github.com/kyledinh/slowblood)")

        col1, col2, col3 = st.columns(3)
        col2.image(Image.open('assets/logo.png'))

        st.markdown("<h1 style='text-align: center; color: black; font-weight: bold;'>Streamlit Demo </h1>",
                    unsafe_allow_html=True)

        st.info(
            '.... is a tool for data extraction from PDFs, images, and other documents. It is a part of, '
            'a platform for data science and machine learning.')

        icon_size = 20

        st_button('youtube', 'https://kyledinh.com', 'Kyle Dinh', icon_size)
        st_button('', 'https://huggingface.co', 'Hugging Face', icon_size)
