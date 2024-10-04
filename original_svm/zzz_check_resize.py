target_path = r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_target.txt"

EAR_paths = [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_ear1.txt",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_ear2.txt",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_ear3.txt",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_ear4.txt",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_ear5.txt",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_ear6.txt",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_ear7.txt",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\svm\resized_ear8.txt"]

# Reading target.txt to retrieve the nested list of 8 lists
targets = []
with open(target_path, 'r') as file:
    for line in file:
        target = list(map(int, line.split()))
        targets.append(target)

# Reading ear[index].txt file and creating a nested list of 8 lists
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
print(EAR_lists)

for i in range(8):
    target = targets[i]
    EAR_list = EAR_lists[i]
    if len(target) == len(EAR_list):
        print(f"ear{i+1} resized successfully!")
        print("")
    else:
        print(f"ear{i+1} resized unsuccessfully")
        if len(target) > len(EAR_list):
            print(f"target > ear by {len(target) - len(EAR_list)}")
        if len(target) < len(EAR_list):
            print(f"ear > target by {len(EAR_list) - len(target)}")
        print("")