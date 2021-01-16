from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPool2D, MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout


def model_training(training_set, testing_set,calls):
    classifier = Sequential()
    classifier.add(Conv2D(128, (3, 3), input_shape=(256, 256, 3), activation='relu'))
    classifier.add(Conv2D(64, (3, 3), input_shape=(256, 256, 3), activation='relu'))
    classifier.add(MaxPool2D(pool_size=(2, 2)))

    classifier.add(Conv2D(32, (3, 3), activation='relu'))
    classifier.add(MaxPool2D(pool_size=(2, 2)))
    classifier.add(Conv2D(32, (3, 3), activation='relu'))
    classifier.add(MaxPool2D(pool_size=(2, 2)))
    # classifier.add(Conv2D(32, (3, 3), activation='relu'))
    # classifier.add(MaxPool2D(pool_size=(2, 2)))
    # #Step 3- Flattening
    classifier.add(Flatten())
    # #Step 4- Full connection
    classifier.add(Dense(units=128, activation='relu'))
    # #For the output step
    classifier.add(Dense(units=5, activation='softmax'))
    classifier.add(Dropout(0.01))
    classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    classifier.fit(training_set, epochs=15,
                   validation_data=testing_set,
                   validation_steps=150/30, callbacks=[calls])
    classifier.save("model.h5")
    print("Saved model to disk")




# class Model:
#     def __init__(self):
#         self.model_path = "models/"
#         # self.callback = Call_back()
#
#     def model_building(self):
#         # self.act_func = self.act_func
#         self.classifier = Sequential()
#         self.classifier.add(Conv2D(16, (3,3), input_shape=(64,64,3), activation='relu'))
#         self.classifier.add(MaxPool2D( pool_size=(2,2) ))
#         self.classifier.add(Conv2D(32, (3,3), input_shape=(64, 64, 3), activation='relu'))
#         self.classifier.add(MaxPool2D(pool_size=(2, 2)))
#         self.classifier.add(Conv2D(64, (3,3), input_shape=(64, 64, 3), activation='relu'))
#         self.classifier.add(MaxPool2D(pool_size=(2, 2)))
#
#         self.classifier.add(Flatten())
#         self.classifier.add(Dense(units=128, activation='relu'))
#         self.classifier.add(Dense(units=4))
#         return self.classifier
#
#     def model_train(self, classifier, callback, train_set, test_set):
#         self.callback = callback
#         self.classifier = classifier
#         self.classifier.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
#         self.model = self.classifier.fit(train_set, epochs=10, validation_data=test_set, validation_steps=2000) # callback = [callbakcs]
#         self.model.save("model.h5")
#         print("Saved model to disk")
#         return self.model


