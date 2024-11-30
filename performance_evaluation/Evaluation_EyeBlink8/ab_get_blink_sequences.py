# Use tag files to identify blink sequences in each video
# Define file paths
EAR_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear1.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear2.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear3.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear4.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear5.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear6.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear7.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear8.txt",
]

EAR_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear_RWB_1.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear_RWB_2.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear_RWB_3.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear_RWB_4.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear_RWB_5.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\ear_RWB_6.txt"
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

#load the tag file paths
tag_paths = [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\fadahd_output_video.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\bao_output_video2.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\nhien_output_video2.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\quang_output_video1.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\minh_output_video1.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\famohm_output_video1.tag"]


# Read EAR files and create a nested list
EAR_lists = []
for path in EAR_paths:
    file_list = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            try:
                file_list.append(float(line))
            except ValueError:
                file_list.append(line)
        EAR_lists.append(file_list)

# Read the tag files and create a nested list
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


# Read the target file and create a list
'''targets = []
with open(target_path, "r") as file:
    for line in file:
        target = list(map(int, line.split()))
        targets.append(target)'''


'''# get blink_frameID_lists and non_blink_framdeID from tag_lists
blink_frameID_lists = [] #for each video
non_blink_frameID_lists = [] #for the video dataset
blink_sequence = []
non_blink_flag = False
non_blink_flag_prev_state = True
for tag_list in tag_lists:
    blink_frameID_list = []
    non_blink_frame_ID_list = []
    blink_sequence = []  # Reset for each video
    non_blink_flag = False
    non_blink_flag_prev_state = True
    for frame in tag_list:
        blinkID = frame["blinkID"]
        if blinkID == "-1":  # Non-blink frame
            non_blink_flag = True
            if not non_blink_flag_prev_state:  # Transition from blink to non-blink
                blink_frameID_list.append(blink_sequence.copy())
                blink_sequence = []
            non_blink_flag_prev_state = True
        else:  # Blink frame
            non_blink_flag = False
            non_blink_flag_prev_state = False
            blink_sequence.append(int(frame["frameID"]))
        if non_blink_flag:
            non_blink_frame_ID_list.append(int(frame["frameID"]))
    # Append remaining blink sequence, if any
    if blink_sequence:
        blink_frameID_list.append(blink_sequence.copy())
    blink_frameID_lists.append(blink_frameID_list)
    non_blink_frameID_lists.append(non_blink_frame_ID_list)
'''

blink_frameID_lists = []  # For each video
non_blink_frameID_lists = []  # For the video dataset

for tag_list in tag_lists:
    blink_frameID_list = []
    non_blink_frame_ID_list = []
    blink_sequence = []
    previous_blinkID = None  # Track the previous blinkID

    for frame in tag_list:
        blinkID = frame["blinkID"]
        frameID = int(frame["frameID"])

        if blinkID == "-1":  # Non-blink frame
            # Save ongoing blink sequence if it exists
            if blink_sequence:
                blink_frameID_list.append(blink_sequence.copy())
                blink_sequence = []
            non_blink_frame_ID_list.append(frameID)

        else:  # Blink frame
            # Check if we transitioned to a new blinkID
            if previous_blinkID is not None and previous_blinkID != blinkID:
                # Save the previous blink sequence
                if blink_sequence:
                    blink_frameID_list.append(blink_sequence.copy())
                    blink_sequence = []
            # Add the current frame to the ongoing blink sequence
            blink_sequence.append(frameID)

        # Update previous_blinkID
        previous_blinkID = blinkID

    # Append any remaining blink sequence at the end of the video
    if blink_sequence:
        blink_frameID_list.append(blink_sequence.copy())

    blink_frameID_lists.append(blink_frameID_list)
    non_blink_frameID_lists.append(non_blink_frame_ID_list)

# Retrieve the EAR for each blink sequence
dataset_sequence_EAR = []

for i, blink_frameID_list in enumerate(blink_frameID_lists):  # Loop over videos
    video_sequence_EAR = []
    for blink_sequence in blink_frameID_list:  # Loop over blink sequences
        sequence_EAR = []
        for frameID in blink_sequence:  # Loop over frames in the blink sequence
            frameID = int(frameID)
            try:
                EAR_value = EAR_lists[i][frameID]
                if EAR_value != "None" and EAR_value is not None:  # Check for valid EAR
                    sequence_EAR.append(EAR_value)
            except IndexError:
                print(f"IndexError: frameID {frameID} is out of range for video {i}")
        if sequence_EAR:  # Only add non-empty sequences
            video_sequence_EAR.append(sequence_EAR)
    if video_sequence_EAR:  # Only add non-empty videos
        dataset_sequence_EAR.append(video_sequence_EAR)

# Print dataset details for verification
print(f"Number of videos processed: {len(dataset_sequence_EAR)}")
for idx, video in enumerate(dataset_sequence_EAR):
    print(f"Video {idx + 1}: {len(video)} blink sequences")

video_mins = []
video_mins_testing = []
for video in dataset_sequence_EAR:  # Iterate over videos
    sequence_mins = []  # Reset sequence_mins for each video
    sequence_mins_testing = []
    for sequence in video:  # Iterate over sequences within the video
        #sequence_mins.append(min(sequence))  # Find min EAR for each sequence
        try:
            #added_value = round((sequence[sequence.index(min(sequence))+1]+(min(sequence)*2))/3, 4)
            added_value = round((max(sequence)+(min(sequence)*2))/2, 4)
            #added_value = round((((max(sequence)+min(sequence))*2+max(sequence))/3), 4)
            #added_value = sequence[sequence.index(min(sequence))+1]
            #added_value = min(sequence)
        except IndexError:
            added_value = min(sequence)
        sequence_mins.append(added_value)
        sequence_mins_testing.append(min(sequence))

    video_min = min(sequence_mins)  # Find min EAR for this video
    video_mins.append(video_min)  # Store the min EAR for the video

    video_min_testing = max(sequence_mins_testing)
    video_mins_testing.append(video_min_testing)

print(video_mins_testing)
print(video_mins)

with open(r"ab_calibratied_RWB_EARs.txt", "w") as file:
    for EAR in video_mins:
        file.write(f"{EAR}\n")
