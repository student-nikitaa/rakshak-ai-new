import streamlit as st
import cv2
import numpy as np

st.title("🛡 Rakshak AI - Live Camera Detection")

# Browser camera
camera_image = st.camera_input("Take a picture")

if camera_image is not None:
    # Convert to OpenCV format
    file_bytes = np.asarray(bytearray(camera_image.read()), dtype=np.uint8)
    frame = cv2.imdecode(file_bytes, 1)

    # Face detection
    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    st.image(frame, channels="BGR")

    if len(faces) > 0:
        st.warning(f"🟡 {len(faces)} Person Detected")
    else:
        st.success("🟢 No Person Detected")
