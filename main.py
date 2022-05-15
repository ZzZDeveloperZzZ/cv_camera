import cv2
import plotly.graph_objects as go


scaleFactor = 2.1,
minNeighbors=5
minSize =(30, 90)
flags=cv2.CASCADE_SCALE_IMAGE

for (x, y, w, h) in faces:
    cv2.rectangle(cam1, (x, y))

    cv2.imshow('Video', cam1)
    if cv2.waitKey(1) & 0xFF == ord
        break
    video_capture.release()
    cv2.destroyWindow()
