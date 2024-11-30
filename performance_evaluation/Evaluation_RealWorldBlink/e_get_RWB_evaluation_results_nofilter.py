'''
Program to retrieve the blinkID from the result.txt files
Example: result_Quang_calibrated.txt --> TEST.txt
'''

#load the results paths
result_paths_list = [[r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_bao_0.18_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_bao_0.2_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_bao_0.3_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_bao_calibrated_nofilter.txt"],
                 [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_nhien_0.18_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_nhien_0.2_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_nhien_0.3_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_nhien_calibrated_nofilter.txt"],
                 [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_quang_0.18_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_quang_0.2_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_quang_0.3_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_quang_calibrated_nofilter.txt"],
                 [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Fadahd_0.18_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Fadahd_0.2_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Fadahd_0.3_nofilter.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Fadahd_calibrated_nofilter.txt"],
                 [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Minh_0.18_nofilter.txt",
                  r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Minh_0.2_nofilter.txt",
                  r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Minh_0.3_nofilter.txt",
                  r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Minh_calibrated_nofilter.txt"],
                  [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_FaMohm_0.18_nofilter.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_FaMohm_0.2_nofilter.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_FaMohm_0.3_nofilter.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_FaMohm_calibrated_nofilter.txt"],
                   [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Huy_0.18_nofilter.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Huy_0.2_nofilter.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Huy_0.3_nofilter.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Huy_calibrated_nofilter.txt"]]

#load the blink tag paths
blink_tag_paths = [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\blinktags\blinktag_Bao.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\blinktags\blinktag_Nhien.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\blinktags\blinktag_Quang.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\blinktags\blinktag_FaDahd.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\blinktags\blinktag_Minh.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\blinktags\blinktag_FaMohm.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\blinktags\blinktag_Huy.txt"]

#load the tag paths
tag_paths = [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\bao_output_video2.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\nhien_output_video2.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\quang_output_video1.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\fadahd_output_video.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\minh_output_video1.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\famohm_output_video1.tag",
             r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\tags\huy_output_video.tag"]

#function to read the tag and return a nested list
def read_file(file_path):
    nested_list = []
    with open(file_path, 'r') as file:
        for line in file:
            # Remove extra spaces and newline characters
            clean_line = line.strip()
            
            # Split the line into individual numbers or ranges, then process them
            if clean_line.isdigit():
                # If it's a single number, append it directly as an integer
                nested_list.append(int(clean_line))
            elif clean_line.startswith('[') and clean_line.endswith(']'):
                # Convert ranges into lists of integers
                # Remove square brackets and split by commas
                numbers = [int(x.strip()) for x in clean_line[1:-1].split(',')]
                nested_list.append(numbers)
    return nested_list

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

# function to get the evaluation statistics
def get_evaluation_statistics(result_file_path, tag_path, ground_truth_blink_count, total_sample):
    ZeroDivisionError_flag = False
    '''
    Approach: for each line (except the first line) based on the frameID compare it with the blink tag file to retrieve the blink ID of each element
    Then we have a list of blinkIDs, we proceed to turn that into a set
    Any blinkID that matches the blinkID in the tags are TP
    Any blinkID in the return list that is "-1" then those are FP
    Any blinkID that is missing from the blinkID in the tags are FN
    '''
    #convert the path to list
    result_file_list = read_file(result_file_path)
    blink_tag_list = read_tag_file(tag_path)

    #remove the first element in the result_file_list because it is the blink count
    removed = result_file_list.pop(0)

    #proceed to get the blinkID of the frameID in each line, return result_blinkID_lists to be written to TEST.txt
    result_blinkID_lists = []
    for line in result_file_list:
        result_blinkID_list = []
        for element in line:
            result_blinkID_list.append(int(blink_tag_list[element]["blinkID"]))
        result_blinkID_lists.append(result_blinkID_list)

    # from the result_blinkID_lists get the set of each element. If the set include 1 element and is not "-1" then it is an accurately detected blink (TP).
    # if a set consists of more than 1 element then it is a mistake and therefore must be analyzed to see which mistake is made. If there are more than
    # 1 blinkID in the set, it is possible that the algorithm failed to detect rapid blinks
    # If the set is 1 element and the element is "-1" then it is a falsely detected blink (FP)
    # Any blinkID in 1 element sets that is missing, they are collected as FN
    result_blinkID_sets = []
    for result_blinkID_list in result_blinkID_lists:
        result_blinkID_set = set(result_blinkID_list)
        result_blinkID_sets.append(result_blinkID_set)

    results = []

    #collect the TP and FP
    TP = 0
    FP = 0
    for result_blinkID_set in result_blinkID_sets:
        if len(result_blinkID_set) >= 1 and any(ele != -1 for ele in result_blinkID_set):
            TP += 1
        if len(result_blinkID_set) == 1 and -1 in result_blinkID_set:
            FP += 1
    results.append(TP)
    results.append(FP)
    
    #collect the FN
    blinkID_list_from_set = []
    for result_blinkID_set in result_blinkID_sets:
        for ele in result_blinkID_list:
            if ele not in blinkID_list_from_set:
                blinkID_list_from_set.append(ele)
    
    ground_truth_blinkIDs = set(range(0, ground_truth_blink_count + 1))  # Expected blinkIDs
    detected_blinkIDs = {ele for blinkID_set in result_blinkID_sets for ele in blinkID_set if ele != -1}
    FN_list = ground_truth_blinkIDs - detected_blinkIDs
    FN = len(FN_list)
    results.append(FN)

    # collect the TN
    TN = total_sample - TP - FP - FN
    results.append(TN)  # Ensure TN is appended here

    #calculate precision, recall, and F1 score
    try:
        precision =  round(TP/(TP+FP), 2)
    except ZeroDivisionError:
        precision = "ZeroDivisionError"
        ZeroDivisionError_flag = True
    try:
        recall = round(TP/(TP+FN), 2)
    except ZeroDivisionError:
        recall = "ZeroDivisionError"
        ZeroDivisionError_flag = True
    if not ZeroDivisionError_flag:
        try:
            F1 = round(2*precision*recall/(precision+recall), 2)
        except ZeroDivisionError:
            F1 = "ZeroDivisionError"
    else:
        F1 = "Error"
    results.append(precision)
    results.append(recall)
    results.append(F1)

    #cacluate accuracy
    accurarcy = round((TP+TN)/(TP+TN+FP+FN), 2)
    results.append(accurarcy)
    
    return result_blinkID_lists, result_blinkID_sets, results

for index, result_paths in enumerate(result_paths_list):
    if index == 0:
        tag_path = tag_paths[0]
        ground_truth_blink_count = 37
        total_sample = 3011
    elif index == 1:
        tag_path = tag_paths[1]
        ground_truth_blink_count = 47
        total_sample = 5558
    elif index == 2:
        tag_path = tag_paths[2]
        ground_truth_blink_count = 67
        total_sample = 3576
    elif index == 3:
        tag_path = tag_paths[3]
        ground_truth_blink_count = 71
        total_sample = 8141
    elif index == 4:
        tag_path = tag_paths[4]
        ground_truth_blink_count = 33
        total_sample = 3023
    elif index == 5:
        tag_path = tag_paths[5]
        ground_truth_blink_count = 34
        total_sample = 4990
    else:
        tag_path = tag_paths[6]
        ground_truth_blink_count = 20
        total_sample = 3600
    for result_path in result_paths:
        result_blinkID_lists, result_blinkID_sets, results = get_evaluation_statistics(result_file_path=result_path, 
                                                                                       tag_path=tag_path, 
                                                                                       ground_truth_blink_count=ground_truth_blink_count, 
                                                                                       total_sample = total_sample)
        '''print(result_blinkID_sets)
        print("")
        for index, lst in enumerate(result_blinkID_lists):
            with open(f"TEST_list.txt", "a") as file:
                file.write(str(lst) + "\n")
        for index, lst in enumerate(result_blinkID_sets):
            with open(f"TEST_set.txt", "a") as file:
                file.write(str(lst) + "\n")'''
        print(results)
    print()
