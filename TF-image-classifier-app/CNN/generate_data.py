from tensorflow.keras.preprocessing.image import ImageDataGenerator

class GenerateData:
    def __init__(self):
        pass

    def datagen(self, dir_path):
        self.train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2,
                                           zoom_range=0.2, horizontal_flip=True)
        self.test_datagen = ImageDataGenerator(rescale=1./255)

        self.train_set = self.train_datagen.flow_from_directory(dir_path, target_size=(256,256),
                                                      batch_size=32, class_mode='categorical')
        self.test_set = self.test_datagen.flow_from_directory(dir_path, target_size=(256,256),
                                                    batch_size=32, class_mode='categorical')
        return self.train_set, self.test_set