import torch
import subprocess
from yolov5 import detect

# Define device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Define path to video for inference
video_path = "C:\\Users\\noam1\\OneDrive\\Desktop\\17.mp4"
weights_path = "output\\exp3\\weights\\best.pt"

# Run inference on video
subprocess.run(["python", "yolov5/detect.py", "--source", video_path, "--weights", weights_path, "--conf", "0.1", "--device", str(device), "--save-csv", "--save-txt", "--save-conf"])