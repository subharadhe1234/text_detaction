import cv2
import pytesseract
import streamlit as st
import pyperclip
import numpy as np
from PIL import ImageGrab
import time

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
# ----------------------  streamlit app----------------------------------

st.title("image to text")
file = st.file_uploader("uplode an image", type=["jpg", "jpeg", 'png'])
def get_data(file):
    if file:
        # st.image(file, use_column_width=True)
        img = cv2.imread(file.name)
        output = pytesseract.image_to_string(img)
        # print(output)
        # st.write(output)
        hImg, wImg, _ = img.shape
        boxes = pytesseract.image_to_boxes(img)
        for b in boxes.splitlines():
            # print(b)
            b = b.split(' ')
            # print(b)
            x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
            cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
            cv2.putText(img, b[0], (x, hImg - y + 10), cv2.FONT_ITALIC, .5, (50, 50, 255), 1)
            # cv2.imshow('img', img)
            # cv2.waitKey(1)

    # st.button(label="copy", on_click=pyperclip.copy(output))
    st.image(img, use_column_width=True)


button=st.button(label="generate")
if button and file is not None:
    with st.spinner("loding..."):
        get_data(file)

    # st.image(img)
    # print(pyperclip.paste())
    # cv2.imshow("imag",img)
    # cv2.waitKey(0)
