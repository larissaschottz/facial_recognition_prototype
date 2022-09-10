import cv2
import mediapipe as mp

# initializing opencv and mediapipe
webcam = cv2.VideoCapture(0)
face_solution = mp.solutions.face_detection
face_reg = face_solution.FaceDetection(0)
drawing = mp.solutions.drawing_utils

# checking frame after frame with a loop
# read webcam infos
# recognize faces
# draw face in the image
# esc stops loop
while True:
    verifier, frame = webcam.read()
    if not verifier:
        break
    face_list = face_reg.process(frame)
    if face_list.detections:
        for face in face_list.detections:
            drawing.draw_detection(frame, face)

    cv2.imshow('Webcam Faces', frame)

    if cv2.waitKey(5) == 27:
        break

# 27 is the code for esc key
# deactivating webcam
webcam.release()