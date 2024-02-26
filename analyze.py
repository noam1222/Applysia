import cv2 #openCV
import torch

def calc_rec_center(x_right, y_top, x_left, y_bottom):
    x_center = x_left + ((x_right - x_left) / 2)
    y_center = y_bottom + ((y_top - y_bottom) / 2)
    return (x_center, y_center)

# Load the model
model = torch.hub.load("yolov5", 'custom', path="output/exp3/weights/best.pt", source="local")

# load the video
video_path = "C:\\Users\\noam1\\OneDrive\\Desktop\\17.mp4"
capture = cv2.VideoCapture(video_path)

# Iterate thorugh each frame
while capture.isOpened():
    ret, frame = capture.read()
    if not ret:
        break
    results = model(frame)
    for obj in results.pred[0]:
        x_right, y_top, x_left, y_bottom, confidence, category = obj.numpy()
        x_right, y_top, x_left, y_bottom, category = int(x_right), int(y_top), int(x_left), int(y_bottom), int(category) # only for showing the image
        print(x_right, y_top, x_left, y_bottom, confidence, category)
        center = calc_rec_center(x_right, y_top, x_left, y_bottom)
        if confidence > 0.5:
            cv2.rectangle(frame, (x_right, y_top), (x_left, y_bottom), (0,0,255), 2)
            cv2.rectangle(frame, (int(center[0]), int(center[1])), (int(center[0]), int(center[1])), (0,0,255), 4)
            cv2.putText(frame, f"Snail2, confidence: {confidence:.2f}", (x_right, y_top-6), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0,0,255), 1, 1)
    cv2.imshow("yolov5", frame)
    cv2.waitKey()
    break