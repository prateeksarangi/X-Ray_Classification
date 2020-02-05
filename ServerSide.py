from keras.models import model_from_json
from keras.preprocessing import image
import numpy as np
import os

with open("model.json") as json_file:
    model = model_from_json(json_file.read())
    model.load_weights("first_try.h5")

img_width, img_height = 150, 150

model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

img = image.load_img(os.getcwd()+"/chest_xray/test/PNEUMONIA/person1_virus_7.jpeg", target_size = (img_width, img_height))

x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)

images = np.vstack([x])
classes = model.predict_classes(images, batch_size = 1)

print(classes)
