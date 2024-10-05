import cv2
import time
from win10toast import ToastNotifier  # Correct toast notifier for Windows 10/11
import threading  # Import threading module to run notifications in a separate thread

# Notify the user to include (1) facial expression, (2) different headpose, (3) rapid blinks
def notify():
    toast = ToastNotifier()
    toast.show_toast(
        "THÔNG BÁO",
        "(1) Nheo mắt hoặc cười - (2) Quay mặt đi chỗ khác và chớp mắt một lần - (3) chớp mắt liên tục 2-3 lần",
        duration=10,  # Notification duration in seconds
    )

# Define the video capture object (0 is the default camera)
video_stream = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not video_stream.isOpened():
    print("Error: Could not open the video stream.")
    exit()

# Define the codec and create VideoWriter object to save the video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Define codec for mp4 format
out = cv2.VideoWriter('output_video.mp4', fourcc, 30.0, (640, 480))  # 30 FPS, 640x480 resolution

# Set window name for display
cv2.namedWindow('Video Capture', cv2.WINDOW_NORMAL)

# Start capturing the video
start_time = time.time()  # Record start time
last_notify_time = start_time  # Record last notify time

while True:
    ret, frame = video_stream.read()

    if not ret:
        print("Error: Failed to grab frame.")
        break

    # Display the current frame
    cv2.imshow('Video Capture', frame)

    # Write the current frame to the video file
    out.write(frame)

    # Press 'q' to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Check recording duration (10 minutes)
    elapsed_time = time.time() - start_time
    if elapsed_time >= 180:  # 3 minutes = 60 seconds/minute * 3 minutes
        break
    
    # Notify every 30 seconds, using a separate thread for notification
    if time.time() - last_notify_time >= 30:
        notification_thread = threading.Thread(target=notify)
        notification_thread.start()  # Start the thread to show notification
        last_notify_time = time.time()

# Release the video capture and writer objects
video_stream.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()

print("Video saved as 'output_video.mp4'.")
