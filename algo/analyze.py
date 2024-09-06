import cv2  # openCV
import torch
import pathlib

from .coordinates import get_cage_num
from constants import *

LAST_FIVE = "last_five"


def calc_rec_center(x_right, y_top, x_left, y_bottom):
    x_center = x_left + ((x_right - x_left) / 2)
    y_center = y_bottom + ((y_top - y_bottom) / 2)
    return (x_center, y_center)


def is_different(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) > EPSILON or abs(y2 - y1) > EPSILON


def analyze(video_path, video_speed, progress_callback):
    pathlib.PosixPath = pathlib.WindowsPath
    # Load the model
    model = torch.hub.load("algo/yolov5", 'custom', path="algo/output/exp4/weights/best.pt", source="local", force_reload=True)

    # load the video
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        return None
    
    results = {}  # going to store the result dict of app_num: movement, [movement_every_five], [trail_points]
    
    # Get the total number of frames and the frame rate
    fps = capture.get(cv2.CAP_PROP_FPS)  # Frames per second
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    one_hour_frames = int(60 * (60 / video_speed) * fps)
    # Calculate the number of frames for every half minute
    frames_per_30_sec = int(0.5 * (60 / video_speed) * fps)  # half minute * 60 seconds * fps

    # Iterate through the video at 5-minute and 30-seconds intervals
    five_counter = 0
    all_frames_number = min(total_frames, one_hour_frames)
    for frame_number in range(0, all_frames_number, frames_per_30_sec):
        progress_callback(int((frame_number / all_frames_number) * 100))
        # Set the video capture to the current frame
        capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        
        # Read the frame
        ret, frame = capture.read()
        if not ret:
            break
        five_counter += 1
        if five_counter // 10 > 11:  # another safety in case of more than an hour
            break

        # start the analysis on this frame
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        res = model(gray_frame)
        checked = [False for _ in range(15)]  # safety in case the model recognize 2 aplysias in same cage
        for obj in res.pred[0]:
            x_right, y_top, x_left, y_bottom, confidence, category = obj.numpy()
            if confidence < 0.5:
                continue
            x_right, y_top, x_left, y_bottom, category = int(x_right), int(y_top), int(x_left), int(y_bottom), int(category)
            center = calc_rec_center(x_right, y_top, x_left, y_bottom)

            app_num = get_cage_num(center)
            if not app_num or checked[app_num-1]:
                print("Unrecognize applysia")
                continue
            checked[app_num-1] = True
            if app_num not in results:
                results[app_num] = {
                    MOVEMENT_DB: 0,
                    MVMNT5_DB: { i: 0.0 for i in range(12) },
                    TRAIL_POINTS_DB: [],
                    LAST_FIVE: (0, 0)
                }

            # add to trail points
            results[app_num][TRAIL_POINTS_DB].append(center)

            # if moved add to movement
            if five_counter % 10 == 0:  # there is 10 30-seconds in 5-minutes
                if is_different(center, results[app_num][LAST_FIVE]):
                    results[app_num][LAST_FIVE] = center
                    results[app_num][MVMNT5_DB][five_counter // 10] = 1 / 12
                    results[app_num][MOVEMENT_DB] += 1 / 12
                else:
                    results[app_num][MVMNT5_DB][five_counter // 10] = 0.0

    progress_callback(100)

    for key in results:
        results[key][MVMNT5_DB] = list(results[key][MVMNT5_DB].values())
        print(key)
        print((len(results[key][MVMNT5_DB])))

    return results


