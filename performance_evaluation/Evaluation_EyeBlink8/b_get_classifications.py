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


#from the tag lists of list of dicts, for each list (video), retrieve a list of "1" and "0" where "1" is blink, "0" is non blink
dataset_classification = []
classification = []

for path in tag_paths:
    video_tags = read_tag_file(path)
    for frame_tag in video_tags:
        if frame_tag["blinkID"] != "-1":
            classification.append(1)
        else:
            classification.append(0)
    dataset_classification.append(classification.copy())
    classification = []

print(len((dataset_classification)))
for lst in dataset_classification:
    print(len(lst))

#write the classifcations into txt files, 1 for each video
for i, lst in enumerate(dataset_classification):
    file_name = f"classification_video{i+1}.txt"
    with open(file_name, "w") as file:
        # Write each number on a new line
        for ele in lst:
            file.write(f"{ele}\n")

    