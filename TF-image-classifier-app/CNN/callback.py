import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


class Call_back(tf.keras.callbacks.Callback):

    def __init__(self, acc_threshold=0.9, print_msg=True):
        super(Call_back, self).__init__()
        self.acc_threshold = acc_threshold
        self.print_msg = print_msg

    def on_epoch_end(self, epoch, logs={}):
        if(logs.get('accuracy') > self.acc_threshold):
            if self.print_msg:
                print("\n-->Reached 90% accuracy so cancelling the training")
            self.model.stop_training = True
        else:
            if self.print_msg:
                print("\nAccuracy not high enough. Starting another epoch...\n")
# callbacks = Call_back()

