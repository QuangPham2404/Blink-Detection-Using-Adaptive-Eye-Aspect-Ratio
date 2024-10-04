import os
import shutil


#create the folders to store the videos
folder_path = [r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\EyeBlink8_0",
               r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\EyeBlink8_1",
               r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\EyeBlink8_2",
               r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\EyeBlink8_3",
               r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\EyeBlink8_4",
               r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\EyeBlink8_5",
               r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\EyeBlink8_6",
               r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\EyeBlink8_7"]


#collect the videos paths and store them in calibration_files list
def find_calibration_files(directory, skip_files):
    """
    Collect the paths of all files that start with 'calibration_' in a designated directory.

    Parameters:
    directory (str): The path of the directory to search in.

    Returns:
    list: A list of full paths of the matching files, or a message if none are found.
    """
    calibration_files = []  # List to store the paths of found files
    
    # Iterate through all the files and subdirectories in the designated directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.startswith("calibration") and file.endswith(".mp4"):
                if file not in skip_files:
                    # Add the full path to the list if the file starts with "calibration_"
                    calibration_files.append(os.path.join(root, file))
    
    if calibration_files:
        return calibration_files  # Return the list of found files
    else:
        return f"No files starting with 'calibration' found in directory '{directory}'."

directory_path = r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8"  # Update this path to test
skip_files = ["calibration_video_EAR0.mp4",
              "calibration_video_EAR1.mp4",
              "calibration_video_EAR2.mp4",
              "calibration_video_EAR3.mp4",
              "calibration_video_EAR4.mp4",
              "calibration_video_EAR5.mp4",
              "calibration_video_EAR6.mp4",
              "calibration_video_EAR7.mp4"]

calibration_files = find_calibration_files(directory_path, skip_files)
print(calibration_files)
print(len(calibration_files))


#function to move files in to designated folders
def move_file_to_folder(file_path, destination_folder):
    """
    Move a file to a designated folder.

    Parameters:
    file_path (str): The full path of the file to move.
    destination_folder (str): The path of the folder where the file should be moved.

    Returns:
    str: A message indicating whether the move was successful or if there was an error.
    """
    try:
        # Ensure the destination folder exists
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Move the file to the destination folder
        shutil.move(file_path, destination_folder)
        return f"File '{file_path}' has been moved to '{destination_folder}'."
    except Exception as e:
        return f"Error moving file '{file_path}': {str(e)}"
    
for path in calibration_files:
    if "video0" in path:
        results = move_file_to_folder(path, folder_path[0])
    elif "video1" in path:
        results = move_file_to_folder(path, folder_path[1])
    elif "video2" in path:
        results = move_file_to_folder(path, folder_path[2])
    elif "video3" in path:
        results = move_file_to_folder(path, folder_path[3])
    elif "video4" in path:
        results = move_file_to_folder(path, folder_path[4])
    elif "video5" in path:
        results = move_file_to_folder(path, folder_path[5])
    elif "video6" in path:
        results = move_file_to_folder(path, folder_path[6])
    elif "video7" in path:
        results = move_file_to_folder(path, folder_path[7])