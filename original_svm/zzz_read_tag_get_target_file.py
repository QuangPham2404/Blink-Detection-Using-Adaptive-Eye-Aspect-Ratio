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


# create data list
paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\1\26122013_223310_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\2\26122013_224532_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\3\26122013_230103_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\4\26122013_230654_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\8\27122013_151644_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\9\27122013_152435_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\10\27122013_153916_cam.tag",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\eyeblink8\11\27122013_154548_cam.tag",
]


def write_to_file(list):
    with open(r"zzz_target.txt", "w") as file:
        for sublist in list:
            line = " ".join(map(str, sublist))
            file.write(f"{line}\n")


data = (
    []
)  # data is the list that store 8 tag lists retrieve from read_tag_file function for 8 tag files
targets = (
    []
)  # store 8 list of binaries value 1/0 to indicate blink or no blink in 8 videos
for index, path in enumerate(paths):
    data.append(read_tag_file(path))
    target = []  # the target list for 1 video
    for frame in read_tag_file(path):
        if frame["blinkID"] == "-1":
            target.append(0)
        else:
            target.append(1)
    targets.append(target)
# write the targets list to a file
write_to_file(targets)


"""def count_ones(input_list):
    count = 0
    for item in input_list:
        if item == 1:
            count += 1
    return count

print(data[0])
print("")
print(targets[0])
print("")
print(len(targets[0]))
print("")
print(count_ones(targets[0]))"""
