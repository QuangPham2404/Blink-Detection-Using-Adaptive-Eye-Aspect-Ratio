#load the tag file paths
tag_paths = [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\quang_output_video1.tag"]


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

print(read_tag_file(tag_paths[0]))
'''print(tag_lists)'''


#retrieve the blink frames in lists of blink sequences
blink_frameID_lists = []
for tag_list in tag_lists:
    # Create a blink_ID_list specific to each tag_list
    blink_ID_list = []
    for frame in tag_list:
        if frame["blinkID"] != "-1" and frame["blinkID"] not in blink_ID_list:
            blink_ID_list.append(frame["blinkID"])
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

print(blink_frameID_lists)

for index, lst in enumerate(blink_frameID_lists):
    if index == 0:
        name = "Quang"
    with open(f"blinktag_{name}.txt", "w") as file:
        file.write(str(len(lst)) + "\n")
        for line in lst:
            file.write(str(line) + "\n")