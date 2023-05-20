# -*- coding: utf-8 -*-
"""app

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ALwzfg7Vr0xmXTkFDJ1qE78-ptbNt8lw
"""

import streamlit as st
import tensorflow as tf

@st.cache(allow_output_mutation=True)
def load_model():
  model=tf.keras.models.load_model('Pikachu or Ditto.hdf5')
  return model
model=load_model()
st.write("""
# Pikachu or Ditto Classifier"""
)
file=st.file_uploader("Choose Ditto or Pikachu from computer",type=["jpg","png"])
A
import cv2
from PIL import Image,ImageOps
import numpy as np
def import_and_predict(image_data,model):
    size=(64,64)
    image=ImageOps.fit(image_data,size,Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image,use_column_width=True)
    prediction=import_and_predict(image,model)
    class_names=['Ditto', 'Pikachu']
    string="OUTPUT : "+class_names[np.argmax(prediction)]
    st.success(string)