import tensorflow as tf
import cv2
import numpy as np

from webapp.settings import MODEL_PATH


def predict(image):
    image = np.asarray(image)

    model = tf.keras.models.load_model(MODEL_PATH)
    image = cv2.resize(image, (200, 200))
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    x = np.array(image).reshape(-1, 200, 200, 1)
    y = model.predict_classes(x)
    return y[0][0]
