'''
Program to retrieve the blinkID from the result.txt files
Example: result_Quang_calibrated.txt --> TEST.txt
'''

#load the results paths
result_paths_list = [[r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_bao_0.18.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_bao_0.2.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_bao_0.3.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_bao_calibrated.txt"],
                 [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_nhien_0.18.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_nhien_0.2.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_nhien_0.3.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_nhien_calibrated.txt"],
                 [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_quang_0.18.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_quang_0.2.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_quang_0.3.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_quang_calibrated.txt"],
                 [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Fadahd_0.18.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Fadahd_0.2.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Fadahd_0.3.txt",
                 r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Fadahd_calibrated.txt"],
                 [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Minh_0.18.txt",
                  r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Minh_0.2.txt",
                  r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Minh_0.3.txt",
                  r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Minh_calibrated.txt"],
                  [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_FaMohm_0.18.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_FaMohm_0.2.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_FaMohm_0.3.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_FaMohm_calibrated.txt"],
                   [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Huy_0.18.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Huy_0.2.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Huy_0.3.txt",
                   r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\result_Huy_calibrated.txt"]]

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
    possible_positive_sets = []
    for index, result_blinkID_set in enumerate(result_blinkID_sets):
        if len(result_blinkID_set) >= 1 and any(ele != -1 for ele in result_blinkID_set):
            possible_positive_sets.append(result_blinkID_set) #possible_postive_sets contains repeated blinkID sets, which needs to be removed
        elif len(result_blinkID_set) == 1 and -1 in result_blinkID_set:
            FP += 1

    #count the true number of TP
    def count_unique_non_negative_one_sets(set_list):
        """
        Counts the number of unique sets in a list, excluding sets containing only `-1`.

        Parameters:
        set_list (list): A list of sets.

        Returns:
        int: The count of unique non-{-1} sets.
        """
        # Initialize a set to store unique non-{-1} sets
        unique_sets = set()

        # Iterate over the list of sets
        for s in set_list:
            # Exclude sets containing only `-1`
            if s != {-1}:
                unique_sets.add(frozenset(s))  # Convert set to frozenset for immutability

        # Return the count of unique sets
        return len(unique_sets)
    
    TP = (count_unique_non_negative_one_sets(possible_positive_sets))
    results.append(TP)
    results.append(FP)
    
    #collect the FN and TN
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


        #create list to store metrics for positive class and negative class
    pos_results = []
    neg_results = []


    #calculate precision, recall, and F1 score for positive class
    try:
        pos_precision =  round(TP/(TP+FP), 2)
    except ZeroDivisionError:
        pos_precision = "ZeroDivisionError"
        ZeroDivisionError_flag = True
    try:
        pos_recall = round(TP/(TP+FN), 2)
    except ZeroDivisionError:
        pos_recall = "ZeroDivisionError"
        ZeroDivisionError_flag = True
    if not ZeroDivisionError_flag:
        try:
            pos_F1 = round(2*pos_precision*pos_recall/(pos_precision+pos_recall), 2)
        except ZeroDivisionError:
            pos_F1 = "ZeroDivisionError"
    else:
        pos_F1 = "Error"
    pos_results.append(pos_precision)
    pos_results.append(pos_recall)
    pos_results.append(pos_F1)
    results.append(pos_results)

    #calculate precision, recall, and F1 score for negative class
    try:
        neg_precision =  round(TN/(TN+FP), 2)
    except ZeroDivisionError:
        neg_precision = "ZeroDivisionError"
        ZeroDivisionError_flag = True
    try:
        neg_recall = round(TN/(TN+FN), 2)
    except ZeroDivisionError:
        neg_recall = "ZeroDivisionError"
        ZeroDivisionError_flag = True
    if not ZeroDivisionError_flag:
        try:
            neg_F1 = round(2*neg_precision*neg_recall/(neg_precision+neg_recall), 2)
        except ZeroDivisionError:
            neg_F1 = "ZeroDivisionError"
    else:
        neg_F1 = "Error"
    neg_results.append(neg_precision)
    neg_results.append(neg_recall)
    neg_results.append(neg_F1)
    results.append(neg_results)

    '''#calculate macro average
    macro_results = []
    #for positive class
    macro_precision = round((pos_precision+neg_precision)/2,2)
    macro_recall = round((pos_recall+neg_recall)/2,2)
    macro_F1 = round((pos_F1+neg_F1)/2,2)
    macro_results.append(macro_precision)
    macro_results.append(macro_recall)
    macro_results.append(macro_F1)
    results.append(macro_results)

    #calculate weight average
    weight_results = []
    weight_precision = round(((pos_precision*pos_sample)+(neg_precision*neg_sample))/total_sample, 2)
    weight_recall = round(((pos_recall*pos_sample)+(neg_recall*neg_sample))/total_sample, 2)
    weight_F1 = round(((pos_F1*pos_sample)+(neg_F1*neg_sample))/total_sample, 2)
    weight_results.append(weight_precision)
    weight_results.append(weight_recall)
    weight_results.append(weight_F1)
    results.append(weight_results)

    #calculate AUC score
    ZeroDivisionError_flag = False
    AUC = []
    try:
        #calculate ROC AUC
        TPR = TP/(TP+FN)
        FPR = FP/(FP+TN)
    except ZeroDivisionError:
        ZeroDivisionError_flag = True

    if not ZeroDivisionError_flag:
        ROC_AUC = round(TPR*FPR*(1/2),2)
    else:
        ROC_AUC = "ZeroDivisionError"
    AUC.append(ROC_AUC)
    ZeroDivisionError_flag = False #reset

    #calculate PR AUC
    try:
        precision = TP/(TP+FP)
        recall = TP/(TP+FN)
    except ZeroDivisionError:
        ZeroDivisionError_flag = True
    
    if not ZeroDivisionError_flag:
        PR_AUC = round(precision*recall*(1/2),2)
    else:
        PR_AUC = "ZeroDivisonError"
    
    AUC.append(PR_AUC)
    ZeroDivisionError_flag = False #reset

    results.append(AUC)'''
    
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

