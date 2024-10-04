import mediapipe as mp
import cv2
import numpy as np
from scipy.spatial import distance as dist #this library allows us to calculate the euclcidean distance between two points based on their x y coords
import time
import os

#load calibration videos
#helper function to load the file paths from a directory and store them in a list
def get_all_file_paths(directory):
    """
    Retrieve all file paths in a folder and its subfolders.

    Parameters:
    directory (str): The path of the directory to search.

    Returns:
    list: A list containing the full paths of all the files in the folder.
    """
    file_paths = []  # List to store all file paths

    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Create the full file path and append it to the list
            full_path = os.path.join(root, file)
            file_paths.append(full_path)
    
    return file_paths

#create the file paths lists
calibration_videos = []
EyeBlink8_video0 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_0")
EyeBlink8_video1 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_1")
EyeBlink8_video2 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_2")
EyeBlink8_video3 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_3")
EyeBlink8_video4 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_4")
EyeBlink8_video5 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_5")
EyeBlink8_video6 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_6")
EyeBlink8_video7 = get_all_file_paths(r"C:\Users\STVN\Desktop\PYTHON\Thuc_tap_BK\blink_notification\performace_assessment\Evaluation_EyeBlink8\individual_EyeBlink8\EyeBlink8_7")
calibration_videos = EyeBlink8_video0 + EyeBlink8_video1 + EyeBlink8_video2 + EyeBlink8_video3 + EyeBlink8_video4 + EyeBlink8_video5 + EyeBlink8_video6 + EyeBlink8_video7

print(calibration_videos)