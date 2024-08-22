import cv2

# Function to handle mouse click events
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        original_x = int(x * original_width / 1200)
        original_y = int(y * original_height / 720)
        print(f"Clicked coordinates (original): ({original_x}, {original_y})")

# Open video file
video_path = 'C:\\Users\\noam1\\OneDrive\\Desktop\\10h.mp4'  # Replace with your video file path
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# Get the original frame size
ret, frame = cap.read()
if not ret:
    print("Error: Could not read video file.")
    exit()
original_height, original_width = frame.shape[:2]

cv2.namedWindow('Video')
cv2.setMouseCallback('Video', mouse_callback)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame to 720x960
    frame_resized = cv2.resize(frame, (1200, 720))

    cv2.imshow('Video', frame_resized)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
