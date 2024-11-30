'''
Program to retrieve RealWorldBlink dataset videos' properties: fps, res, framecount
'''
import cv2

# Load dataset videos' path
video_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\bao_output_video1.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\huy_output_video1.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\nhien_output_video1.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\quang_output_video1.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\fadahd_output_video.mp4",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_mp4\fadahd_output_video.mp4"
]

# Function to retrieve video properties
def process(video_path):
    # Create a dictionary to store the video's properties: fps, resolution, frame count, and duration
    video_properties = {}

    # Take video from video path
    video_stream = cv2.VideoCapture(video_path)

    # Check if the video stream opened successfully
    if not video_stream.isOpened():
        return "Video stream interrupted"

    # Get video properties
    fps = video_stream.get(cv2.CAP_PROP_FPS)
    video_properties["fps"] = fps
    width = int(video_stream.get(cv2.CAP_PROP_FRAME_WIDTH))
    video_properties["width"] = width
    height = int(video_stream.get(cv2.CAP_PROP_FRAME_HEIGHT))
    video_properties["height"] = height
    resolution = (width, height)
    video_properties["resolution"] = resolution

    # Get frame count
    frame_count = int(video_stream.get(cv2.CAP_PROP_FRAME_COUNT))
    video_properties["frame_count"] = frame_count

    # Calculate duration (in seconds)
    if fps > 0:
        duration = round(frame_count / fps, 1)
    else:
        duration = 0  # Handle edge case if FPS is zero
    video_properties["duration"] = duration

    # Release the video stream
    video_stream.release()
    
    return video_properties

# Loop through the videos in the dataset
videos_properties_list = []
for video_path in video_paths:
    videos_properties_list.append(process(video_path))

for video in videos_properties_list:
    print(video)
