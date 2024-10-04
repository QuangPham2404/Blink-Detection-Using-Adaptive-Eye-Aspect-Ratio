# first find the number of blink sequences and their lengths in the dataset

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


# helper function to extract tag file to tag list
def read_tag_file(path):
    tags = (
        []
    )  # a list in which stored n dictionaries for n lines (each line is info about a frame) in the tag file; each dict contains the tag_features of 1 line in the file
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
            i = 0
            tag = (
                {}
            )  # a dict with len(tag_features) key-value pairs, storing the features of each frame
            for ele in line:
                tag[tag_features[i]] = ele
                i += 1
                if i == len(tag_features) - 1:
                    tag[tag_features[i]] = "None"
                    i = 0
            tags.append(tag)
    return tags


# get tag_lists
tag_lists = [] # tag_lists = [[{frame_0_of_first_video}, ...], [{frame_0_of_second_video}, ...], ...]
for path in tag_paths:
    tag_lists.append((read_tag_file(path)))


#get blink sequence frameIDs and blink sequence length
blink_sequences_list = []
blink_sequence_index = 0
for video_index, video_tag in enumerate(tag_lists):
    video_index += 1 #video index starts at 1
    video_blink_sequence = []
    blink_sequence = []
    for frame_tag in video_tag:
        if frame_tag["blinkID"] != "-1":
            blink_sequence.append(frame_tag["frameID"])
        else:
            if blink_sequence:
                blink_sequence_length = len(blink_sequence)
                blink_sequence_dict = {"index": blink_sequence_index, "frames":blink_sequence, "length":blink_sequence_length, "video":video_index}
                video_blink_sequence.append(blink_sequence_dict)
                blink_sequence_index += 1
                blink_sequence = []

    # Handle the case where a blink sequence ends at the last frame of the video
    if blink_sequence:
        blink_sequence_length = len(blink_sequence)
        blink_sequence_dict = {"index": blink_sequence_index, "frames": blink_sequence, "length": blink_sequence_length, "video": video_index}
        video_blink_sequence.append(blink_sequence_dict)
        blink_sequence_index += 1

    blink_sequences_list.append(video_blink_sequence)

print(blink_sequences_list)