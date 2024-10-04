import os

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

def read_tag_file(path):
    tags = []
    tag_features = [
        "frameID", "blinkID", "NF", "LE_FC", "LE_NV", "RE_FC", "RE_NV",
        "F_X", "F_Y", "F_W", "F_H", "LE_LX", "LE_LY", "LE_RX", "LE_RY",
        "RE_LX", "RE_LY", "RE_RX", "RE_RY", "endln",
    ]
    with open(path, "r") as tag_file:
        for line in tag_file:
            elements = line.strip().split(":")
            tag = {feature: elements[i] if i < len(elements) else "None"
                   for i, feature in enumerate(tag_features)}
            tags.append(tag)
    return tags

# get tag_lists
tag_lists = [read_tag_file(path) for path in tag_paths]

# get blink sequence frameIDs and blink sequence length
blink_sequences_list = []
blink_sequence_index = 0
for video_index, video_tag in enumerate(tag_lists):
    video_blink_sequences = []
    blink_sequence = []
    for frame_tag in video_tag:
        if frame_tag["blinkID"] != "-1":
            blink_sequence.append(frame_tag["frameID"])
        else:
            if blink_sequence:
                blink_sequence_dict = {
                    "index": blink_sequence_index,
                    "frames": blink_sequence,
                    "length": len(blink_sequence),
                    "video": video_index
                }
                video_blink_sequences.append(blink_sequence_dict)
                blink_sequence_index += 1
                blink_sequence = []

    # Handle the case where a blink sequence ends at the last frame of the video
    if blink_sequence:
        blink_sequence_dict = {
            "index": blink_sequence_index,
            "frames": blink_sequence,
            "length": len(blink_sequence),
            "video": video_index
        }
        video_blink_sequences.append(blink_sequence_dict)
        blink_sequence_index += 1

    blink_sequences_list.append(video_blink_sequences)

# Print results
total_sequences = sum(len(video_sequences) for video_sequences in blink_sequences_list)
print(f"Total number of blink sequences: {total_sequences}")
print("Blink sequence lengths:")
for video_index, video_sequences in enumerate(blink_sequences_list):
    print(f"Video {video_index}:")
    for seq in video_sequences:
        print(f"  Sequence {seq['index']}: {seq['length']} frames")



