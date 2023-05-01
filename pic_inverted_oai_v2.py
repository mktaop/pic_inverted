#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 22:45:27 2023

@author: avi_patel
"""
import streamlit as st
from PIL import Image
import cv2
import numpy as np

def invert_colors(img):
    inverted_img = cv2.bitwise_not(img)
    return inverted_img

def main():
    st.title("Picture Inverter")
    st.write("Upload a picture or take a picture with the webcam and see it inverted!")
    
    # add a file uploader and a webcam button to the sidebar
    menu = ["File Upload", "Webcam"]
    choice = st.sidebar.selectbox("Select an option", menu)
    
    # if the user selects "File Upload", ask them to upload a picture
    if choice == "File Upload":
        uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
        if uploaded_file is not None:
            # read the uploaded file as a PIL image and convert it to a NumPy array
            img = np.array(Image.open(uploaded_file))
            st.image([img, invert_colors(img)], caption=['Original', 'Inverted'], width=300)
    # if the user selects "Webcam", open the webcam and show the video stream
    elif choice == "Webcam":
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            st.error("Could not open webcam.")
        else:
            # read frames from the webcam and display them in the app
            ret, frame = cap.read()
            if ret:
                #st.image([frame, invert_colors(frame)], caption=['Original', 'Inverted'], width=300)
            # add a button to take a picture and invert its colors
                if st.button("Take Picture"):
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    img = frame
                    st.image([img, invert_colors(img)], caption=['Original', 'Inverted'], width=300)
        cap.release()

if __name__ == "__main__":
    main()







