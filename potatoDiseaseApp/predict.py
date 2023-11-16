import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing import image
import numpy as np
from tensorflow import keras
import io
from PIL import Image

import tensorflow as tf
from tensorflow.keras.layers import Layer

class RandomFlipLayer(Layer):
    def __init__(self, **kwargs):
        super(RandomFlipLayer, self).__init__(**kwargs)

    def call(self, inputs, training=None):
        # Your layer's logic here
        pass

    def get_config(self):
        config = super(RandomFlipLayer, self).get_config()
        return config

    @classmethod
    def from_config(cls, config):
        return cls(**config)

model = keras.models.load_model('potato-disease-classification-model/potatoes.h5')

def predict_image(image_file):
    try:

        image_content = image_file.read()

        img = image.load_img(io.BytesIO(image_content), target_size=(256, 256))
        img = np.expand_dims(img, axis=0)
        img = img / 255.0  # Normalize the image

        # Perform prediction
        predictions = model.predict(img)

 
        class_labels = ["Early Blight","Late Blight", "Healthy"]
        predicted_class = class_labels[np.argmax(predictions)]

        return predicted_class

    except Exception as e:
        return str(e)