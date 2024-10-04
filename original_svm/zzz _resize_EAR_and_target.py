# Define file paths
EAR_paths = [
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\ear1.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\ear2.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\ear3.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\ear4.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\ear5.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\ear6.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\ear7.txt",
    r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\ear8.txt",
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

target_path = r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\target.txt"


# read the files
# read EAR_paths and create a nested list
EAR_lists = []
for path in EAR_paths:
    file_list = []
    with open(path, "r+") as file:
        for line in file:
            line = line.strip()
            try:
                file_list.append(float(line))
            except ValueError:
                file_list.append(line)
        EAR_lists.append(file_list)
"""print(EAR_list)"""


# read the tag files and create a nested list
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


tag_lists = []
for path in tag_paths:
    tag_lists.append(read_tag_file(path))
"""print(tag_list)
print(len(tag_list))"""

# read the target file and create a list
"""target_list = []
with open(target_path, 'r') as file:
    for line in file:
        target = list(map(int, line.split()))
        target_list.append(target)
print(target_list)
print(len(target_list))"""


# resizing the ear_list and target_list
def remove_sublist(big_list, start_idx, end_idx):
    """
    Removes a sublist from a larger list from start_idx to end_idx (inclusive).
    Parameters:
    big_list (list): The original list from which the sublist will be removed.
    start_idx (int): The starting index of the sublist to be removed.
    end_idx (int): The ending index of the sublist to be removed.
    Returns:
    list: The list with the sublist removed.
    """
    start_idx = int(start_idx)
    end_idx = int(end_idx)
    if start_idx < 0 or end_idx >= len(big_list) or start_idx > end_idx:
        raise ValueError(
            f"Invalid start or end index: start_idx={start_idx}, end_idx={end_idx}, list_length={len(big_list)}"
        )
    return big_list[:start_idx] + big_list[end_idx + 1 :]


def resize(EAR_list, tag_list):
    EAR_last_frameID = len(EAR_list - 1)
    tag_first_frameID = int(tag_list[0]["frameID"])
    tag_last_frameID = int(tag_list[len(tag_list) - 1]["frameID"])
    if tag_first_frameID != 0:
        resized_EAR_list = remove_sublist(EAR_list, 0, tag_first_frameID)
    if EAR_last_frameID > tag_last_frameID:
        resized_EAR_list2 = remove_sublist(
            resized_EAR_list, tag_last_frameID, len(EAR_list) - 1
        )
    if EAR_last_frameID < tag_last_frameID:
        resized_tag_list = remove_sublist(tag_list, EAR_last_frameID, len(tag_list) - 1)
    return resized_EAR_list2, resized_tag_list


def rewrite_EAR_file(EAR_list, index):
    """
    Writes the resized ear_list to a new file.
    """
    with open(f"resized_ear{index + 1}.txt", "w") as f:
        for ele in EAR_list:
            f.write(f"{ele}\n")


def rewrite_target_file(target_list):
    """
    Writes the targets list to the target.txt file.
    """
    with open(f"resized_target.txt", "w") as file:
        for sublist in target_list:
            line = " ".join(map(str, sublist))
            file.write(f"{line}\n")


# rewrite new EAR files based on resized EAR list and rewrite target file based on resized tag_lists
for i in range(8):
    EAR_list = EAR_lists[i]
    tag_list = tag_lists[i]
    resized_EAR_list, resized_tag_list = resize(EAR_list, tag_list)
    rewrite_EAR_file(EAR_list, i)
    # create target_list to write target file
    target_list = []
    for lst in resized_tag_list:
        target = [1 if frame["blinkID"] != "-1" else 0 for frame in lst]
        target_list.append(target)
    rewrite_target_file(target_list)
