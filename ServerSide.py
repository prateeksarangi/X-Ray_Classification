from tensorflow.keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
import os

def predict_class(path):
    with open("Model/model.json") as json_file:
        model = model_from_json(json_file.read())
        model.load_weights("Model/weight.h5")

    img_width, img_height = 150, 150
    img = image.load_img(path, target_size = (img_width, img_height))

    x = image.img_to_array(img)
    x = np.expand_dims(x, axis = 0)

    images = np.vstack([x])
    classes = model.predict(images, batch_size = 16)

    return classes

'''
c = predict_class(os.getcwd()+'/chest_xray/chest_xray/train/NORMAL/IM-0149-0001.jpeg')
print(c[0][0])


c = predict_class(os.getcwd()+'/chest_xray/chest_xray/train/PNEUMONIA/person1000_virus_1681.jpeg')
print(c[0][0])
'''
