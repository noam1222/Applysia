import torch
from pathlib import Path
from roboflow import Roboflow
from shutil import copyfile
import subprocess
import os

# Initialize Roboflow
rf = Roboflow(api_key="UBkfMbfpUckXdKPXR2WJ")

# Download dataset
project = rf.workspace("applysia").project("blue-snail")
dataset = project.version(4).download("yolov5")

# Define paths
data_dir = Path("Blue-Snail-4") # Path(dataset.location)
train_path = data_dir / "train"
val_path = data_dir / "valid"
data_yaml = data_dir / "data.yaml"
weights = "yolov5s.pt"  # Pretrained weights (or path to your custom trained weights)

# Define device
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Clone YOLOv5 repository
subprocess.run(["git", "clone", "https://github.com/ultralytics/yolov5.git"])

# Install dependencies
subprocess.run(["pip", "install", "-U", "-r", "yolov5/requirements.txt"])

# Prepare data.yaml file
copyfile(data_yaml, "data.yaml") #TODO need to add "../" in the beginning of val and train. 

# Train YOLOv5 model
weights = "yolov5s.pt"  # Pretrained weights (or path to your custom trained weights)
device = "cpu"  # or "cuda" if you have a GPU
subprocess.run(["python", "yolov5/train.py", "--img", "640", "--batch", "16", "--epochs", "50", "--data", "Blue-Snail-4/data.yaml", "--cfg", "yolov5/models/yolov5s.yaml", "--weights", weights, "--device", device, "--project", "output"])

