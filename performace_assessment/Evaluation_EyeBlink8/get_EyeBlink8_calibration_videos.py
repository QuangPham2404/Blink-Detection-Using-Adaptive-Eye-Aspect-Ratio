# Define file paths
EAR_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\1\26122013_223310_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\2\26122013_224532_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\3\26122013_230103_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\4\26122013_230654_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\8\27122013_151644_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\9\27122013_152435_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\10\27122013_153916_cam.avi",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\11\27122013_154548_cam.avi",
]

tag_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\1\26122013_223310_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\2\26122013_224532_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\3\26122013_230103_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\4\26122013_230654_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\8\27122013_151644_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\9\27122013_152435_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\10\27122013_153916_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\11\27122013_154548_cam.tag",
]


# Read the tag files and create a nested list --> read the tag files and return a list with dictionary for the annotation of each frame
def read_tag_file(path):
    tags = []
    tag_features = [
        "frameID",
        "blinkID",
        "NF",
        "LE_FC",
        "LE_NV",
        "RE_FC",
        "RE_NV",
        "F_X",
        "F_Y",
        "F_W",
        "F_H",
        "LE_LX",
        "LE_LY",
        "LE_RX",
        "LE_RY",
        "RE_LX",
        "RE_LY",
        "RE_RX",
        "RE_RY",
        "endln",
    ]
    with open(path, "r") as tag_file:
        data = tag_file.readlines()
        for line in data:
            line = line.strip().split(":")
            tag = {}
            for i, ele in enumerate(line):
                tag[tag_features[i]] = ele
            tags.append(tag)
    return tags

tag_lists = []
for path in tag_paths:
    tag_lists.append(read_tag_file(path))

'''print(read_tag_file(tag_paths[0]))'''
'''print(tag_lists)'''


#retrieve the blink frames in lists of blink sequences
blink_frameID_lists = []
for tag_list in tag_lists:
    # Create a blink_ID_list specific to each tag_list
    blink_ID_list = set(frame["blinkID"] for frame in tag_list if frame["blinkID"] != "-1")
    blink_frameID_list = []  # This will store all blink sequences for the current video
    for blinkID in blink_ID_list:
        blink_sequence_frameID = []  # To store frames for the current blinkID
        for frame in tag_list:
            if frame["blinkID"] == blinkID:
                blink_sequence_frameID.append(int(frame["frameID"]))
        # Append the current blink sequence (if not empty)
        if blink_sequence_frameID:
            blink_frameID_list.append(blink_sequence_frameID)
    # Append the list of blink sequences for the current video to the main list
    blink_frameID_lists.append(blink_frameID_list)

'''#add +- 30 additional frameID to the blink sequence in the blink_frameID_list(s) in the blink_frameID_lists to make sure that the algorithm capture the whole blink sequences
for blink_frameID_list in blink_frameID_lists:
    for blink_sequence in blink_frameID_list:
        i = 1
        start_frameID = int(blink_sequence[0])
        end_frameID = int(blink_sequence[len(blink_sequence)-1])
        while i <= 30:
            blink_sequence.append(start_frameID - i)
            blink_sequence.append(end_frameID + i)
            i += 1'''

print(blink_frameID_lists[0])
for lst in blink_frameID_lists:
    print(len(lst))
'''for lst in blink_frameID_lists[0]:
    print(lst)
    print()
print(len(blink_frameID_lists[0]))'''


'''#get the time stamp of the start frame and end frame of each blink sequence
start_end_timestamp_lists = []
for blink_frameID_list in blink_frameID_lists:
    start_end_timestamp_list = []
    for blink_sequence in blink_frameID_list:
        #identify the start frame index and the end frame index, which are the min and the max frameID
        start_frameID = min(blink_sequence)
        end_frameID = max(blink_sequence)
        #identify the start frame and end frame time stamp by dividing the frame ID by the FPS
        FPS = 30
        start_frame_timestamp = round(start_frameID/FPS, 3)
        end_frame_timestamp = round(end_frameID/30, 3)
        start_end_timestamp_list.append((start_frame_timestamp, end_frame_timestamp))
    start_end_timestamp_lists.append(start_end_timestamp_list)

print(start_end_timestamp_lists)
print(len(start_end_timestamp_lists))
print(len(start_end_timestamp_lists[0]))


from moviepy.editor import VideoFileClip, concatenate_videoclips

# Loop through the videos in the EyeBlink8 dataset
for index, EAR_path in enumerate(EAR_paths):

    # Load the video
    video = VideoFileClip(EAR_path)
    
    # Get the start and end timestamps for the blinks of the current video
    trimmed_timestamps = start_end_timestamp_lists[index]
    
    for i, trimmed_timestamp in enumerate(trimmed_timestamps):
        start_timestamp = trimmed_timestamp[0]
        end_timestamp = trimmed_timestamp[1]
        
        # Check if the timestamps are valid before trimming
        if start_timestamp >= 0 and end_timestamp <= video.duration:
            try:
                # Trim the video based on the timestamps
                trimmed_video = video.subclip(start_timestamp, end_timestamp)
                trimmed_video.write_videofile(f"calibration{i}_video{index}.mp4", codec="libx264", audio_codec="aac")
                # Explicitly close the trimmed video resource after saving
                trimmed_video.close()
            except Exception as e:
                print(f"Error trimming video {EAR_path} from {start_timestamp} to {end_timestamp}: {e}")
        else:
            print(f"Invalid timestamp {start_timestamp}-{end_timestamp} for video {EAR_path}")


    # Close the main video resource
    video.close()'''