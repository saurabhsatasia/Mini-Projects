import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np


class Predict:
    def __init__(self, filename):
        self.filename =filename

    def prediction(self):
        # load model
        model = load_model('model.h5')

        # summarize model
        #model.summary()
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        predictions = model.predict(test_image)
        score = tf.nn.softmax(predictions[0])
        return score

    # print("This image most likely belongs {} with a {:.2f} percent confidence".format(class_names[np.argmax(score)], 100*np.max(score)))
