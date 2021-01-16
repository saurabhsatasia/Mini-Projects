import streamlit as st
from PIL import Image
from CNN.predict import Predict


@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img



def main():
    st.header("Tensorflow Image Classifier")
    img_file = st.file_uploader("Upload Images", type=['png','jpg','jpeg'])
    if img_file is None:
        st.image(load_image("general.jpg"), width=500, height=500)
    elif img_file is not None:
        st.image(load_image(img_file),width=400,height=400)
        pred = st.button("Predict")
        if pred:
            pred = Predict(filename=img_file)
            result = pred.prediction()
            st.header(result)






if __name__ == '__main__':
    main()