import cv2 #openCV
import torch

from .coordinates import get_cage_num

def calc_rec_center(x_right, y_top, x_left, y_bottom):
    x_center = x_left + ((x_right - x_left) / 2)
    y_center = y_bottom + ((y_top - y_bottom) / 2)
    return (x_center, y_center)

def is_different(p1, p2):
    return p1 != p2

def analyze(video_path):
    # Load the model
    model = torch.hub.load("algo/yolov5", 'custom', path="algo/output/exp5/weights/best.pt", source="local")

    # load the video
    capture = cv2.VideoCapture(video_path)
    if not capture.isOpened():
        return None
    
    results = {} # goint to result dict of app_num: movemnt, [movement_every_five], [trail_points]
    
    # Get the total number of frames and the frame rate
    fps = capture.get(cv2.CAP_PROP_FPS)  # Frames per second
    total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
    one_hour_frames = int(60 * 60 * fps)
    # Calculate the number of frames for every half minute
    frames_per_30_sec = int(0.5 * 60 * fps)  # half minute * 60 seconds * fps

    # Iterate through the video at 5-minute and 30-seconds intervals
    five_counter = 0
    for frame_number in range(0, min(total_frames, one_hour_frames), frames_per_30_sec):
        # Set the video capture to the current frame
        capture.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        
        # Read the frame
        ret, frame = capture.read()
        if not ret:
            break
        five_counter += 1

        # start the analysis on this frame
        res = model(frame)
        checked = [False for _ in range(15)] # safety in case the model recognize 2 applysias in same cage
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
                    "movement": 0,
                    "movement_every_five": { i: 0.0 for i in range(12) },
                    "trail_points": [],
                    "last_five": (0, 0)
                }

            # add to trail points
            results[app_num]["trail_points"].append(center)

            # if moved add to movement
            if five_counter % 10 == 0: # there is 10 30-seconds in 5-minutes
                if is_different(center, results[app_num]["last_five"]):
                    results[app_num]["last_five"] = center
                    results[app_num]["movement_every_five"][five_counter // 10] = 1 / 12
                    results[app_num]["movement"] += 1 / 12
                else:
                    results[app_num]["movement_every_five"][five_counter // 10] = 0.0


    for key in results:
        results[key]["movement_every_five"] = list(results[key]["movement_every_five"].values())

    return results

if __name__ == "__main__":
    res = analyze("C:\\Users\\noam1\\OneDrive\\Desktop\\10h.mp4")
    print(res[2])
    print(len(res[2]["trail_points"]))