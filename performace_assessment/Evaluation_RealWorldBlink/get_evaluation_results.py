#load the results paths
result_paths = [[r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_results\result_Quang_calibrated.txt",
                       r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_results\result_Quang_0.3.txt"]]

#load the blink tag paths
blink_tag_paths = [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\quang_blinktag.txt"]

#load the tag paths
tag_paths = [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_RealWorldBlink\RealWorldBlink_avi\quang_output_video1.tag"]

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

#function to compare the videos and return the required data
def get_evaluation_statistics_0(EARThresh1, EARThresh2, EARThresh3, EARThresh4, model1, model2, blink_tag):
    '''
    input: max 6 nested lists: 5 results from evaluation models (EARTHresh1 to EARThresh4 is model EARThresh with 0.18 to 0.3), 1 from the blink tag.
    structure of each file to be converted to nested list: line 1: number of blinks, line 2 to line n: lists of blink sequence frame indexes
    nested list after feeding to read_file function: a nested list, element 1 is line 1 which is the number of blinks, the next elements are lists of blink sequence frameID

    output: true postives, false postitives, true negatives, false negatives
    '''
    # get the true positives - when the model accurately identify a blink sample as a blink
    i = 1 # set i = 1 because element 0 in each list is the number of blink, we do not need this
    while i <= len(blink_tag):
        ...


# function to get the evaluation statistics
def get_evaluation_statistics(result_file_path, tag_path):
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

    #proceed to get the blinkID of the frameID in each line
    result_blinkID_lists = []
    for line in result_file_list:
        result_blinkID_list = []
        for element in line:
            result_blinkID_list.append(blink_tag_list[element]["blinkID"])
        result_blinkID_lists.append((result_blinkID_list))
    
    return result_blinkID_lists

result_blinkID_lists = get_evaluation_statistics(result_file_path=result_paths[0][0], tag_path=tag_paths[0])
for index, lst in enumerate(result_blinkID_lists):
    with open(f"TEST.txt", "a") as file:
        file.write(str(lst) + "\n")

