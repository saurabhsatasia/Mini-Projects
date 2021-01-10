from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout

class Model:
    def __init__(self):
        pass

    def model_building(self):
        # self.act_func = self.act_func
        classifier = Sequential()
        classifier.add(Conv2D(16, (3.3), input_shape=(64,64,3), activation='relu'))
        classifier.add(MaxPool2D( pool_size=(2,2) ))
        classifier.add(Conv2D(32, (3.3), input_shape=(64, 64, 3), activation='relu'))
        classifier.add(MaxPool2D(pool_size=(2, 2)))
        classifier.add(Conv2D(64, (3.3), input_shape=(64, 64, 3), activation='relu'))
        classifier.add(MaxPool2D(pool_size=(2, 2)))

        classifier.add(Flatten())
        classifier.add(Dense(units=128, activation='relu'))
