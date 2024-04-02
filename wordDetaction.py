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
file=st.file_uploader('uploade the image',type=['jpg','jpeg','png'])
def get_data(file):
    if file:

        img = cv2.imread(f"C:\\Users\subha\Downloads\\{file.name}")
        # st.image(file, use_column_width=True)
        # img = cv2.resize(img, (640, 480))
        output = pytesseract.image_to_string(img)
        # st.image(file, use_column_width=True)
        # print(output)
        # st.write(output)
        hImg, wImg, _ = img.shape
        # img=img.resize((600,400))

        boxes = pytesseract.image_to_data(img)
        # print(boxes)
        for a,b in enumerate(boxes.splitlines()):
            if  a!=0:
                b = b.split()
                if len(b)==12:


                    x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                    cv2.rectangle(img, (x-2, y-2), (w+x, h+y+2), (50, 50, 255), 1)
                    # cv2.putText(img, b[11], (x+10,y+h + 20), cv2.FONT_ITALIC, .5, (50, 50, 255), 1)
                    # cv2.imshow('img', img)
                    # cv2.waitKey(1)

    # st.button(label="copy", on_click=pyperclip.copy(output))
    st.image(img, use_column_width=True)


button=st.button(label="generate")
if button and file is not None:
    with st.spinner("loding..."):
        # print( file)
        get_data(file)

    # st.image(img)
    # print(pyperclip.paste())
    # cv2.imshow("imag",img)
    # cv2.waitKey(0)
