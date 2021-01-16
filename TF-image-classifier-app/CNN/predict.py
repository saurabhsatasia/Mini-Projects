import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import streamlit as st


class Predict:
    def __init__(self, filename):
        self.filename =filename

    def prediction(self):
        # load model
        model = load_model('D:\Strive\Mini-Projects\TF-image-classifier-app\model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (256, 256))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        predictions = model.predict(test_image)
        st.write(type(predictions))
        st.write(predictions)
        score = tf.nn.softmax(predictions[0])
        prediction=None
        # ['daniel_radcliffe', 'hermione_granger', 'professor_albus_dumbledore', 'professor_severus_snape', 'ron_wesley']
        if predictions[0][0] == 1:
            prediction = 'daniel_radcliffe'

        elif predictions[0][1] == 1:
            prediction = 'hermione_granger'

        elif predictions[0][2] == 1:
            prediction = 'professor_albus_dumbledore' # daniel

        elif predictions[0][3] == 1:
            prediction = 'professor_severus_snape'

        elif predictions[0][4] == 1:
            prediction = 'ron_wesley'

        # print("This image most likely belongs {} with a {:.2f} percent confidence".format(class_indices[np.argmax(score)], 100*np.max(score)))
        return [{"image": prediction}] # , "score": score

