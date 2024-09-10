# Applysia

**Applysia** is a movement tracking program designed to track the movement of sea-snails. This project was developed as part of our final project for the CS degree at Bar-Ilan University (BIU).

## Home Screen
![image](https://github.com/user-attachments/assets/d43ce886-aecd-4e08-8d3f-b91806c7fb01)

The Home Screen allows users to input details and run the analysis process. Users can select between analyzing:
- A 1-hour video at 1x speed
- A 30-minute video at 2x speed

## Report Screen
![image](https://github.com/user-attachments/assets/c80bcffd-9475-4091-8e3f-256c9caea9df)

The Report Screen displays the results of the analysis. For a 1-hour video, movement is sampled every 5 minutes. If a snail moves more than a predefined threshold (epsilon = 0.1), it is considered as having moved.

Features:
- View individual movement for each Aplysia and the average movement for all.
- Visualize the trail points of the snails' movement within the cage.
- Export the report to Word, Excel, or as a trail point movement graph (video).

## Library Screen
![image](https://github.com/user-attachments/assets/0293a06b-530d-4d8d-bfcd-22c4d5c665c9)

The Library Screen provides interaction with the MongoDB database. 

Features:
- Filter reports by date, time, and movement (LEQ, GEQ).
- Delete specific reports (either by a specific report or for all snails at a given time) by dragging the report to the trash can.

## Requirements
- Python
- MongoDB

## How to Run
1. Install the required dependencies: `pip install -r requirements.txt`.
2. Run the program using the command: `python main.py`.

## Customization
- You can customize the model for other creatures in the cage by changing the path in `algo/output/exp4` to your model (alternatively, add your model in any path you choose and update `algo/analyze.py` to use the correct path).
- Modify epsilon and other constants in `constants.py`.
- Update icons and images in the `res` folder.
