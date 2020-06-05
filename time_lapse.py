"""
Time-lapse project

About: A program that speeds up long videos. Uses OpenCV
and some other supporting libraries that make life eaiser.

Author: Grayson Hadley
"""

import cv2 as cv
import os 
from tkinter import Tk
from tkinter import filedialog
import datetime

__speed__ = 6                   # Selects every nth frame for the timelapse
__fileExtention__ = ".avi"      # Output filetype
__codec__ = "DIVX"              # Output codec

def get_Video_Dimentions(video):
    """ Get width and height of video """
    width = int(video.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv.CAP_PROP_FRAME_HEIGHT))
    return width, height

def is_Long_Enough(video):
    """ Check if video is 6sec or longer """
    fps = video.get(cv.CAP_PROP_FPS)
    numFrames = video.get(cv.CAP_PROP_FRAME_COUNT)

    if((numFrames / fps) >= 6):
        return True
    else:
        return False

def process_Video(cap, out):
    """ Gets every 6th frame and saves it """
    count = 0

    while(cap.isOpened()):
        ret, frame = cap.read()

        if(ret == True):
            if(count % __speed__ == 0):
                out.write(frame)

            if(cv.waitKey(1) & 0xFF == ord('q')):
                break

            count += 1
        else:
            break

def main():
    """ Main function """

    # Makes each file output name unique
    nowStr = datetime.datetime.now()
    output_filename = "time_lapse"
    output_filename += nowStr.strftime("%m_%d_%Y_%H_%M_%S")
    output_filename += __fileExtention__

    # Open file in Windows
    dir_path = os.path.dirname(os.path.realpath(__file__))
    Tk().withdraw()
    filename = filedialog.askopenfilename(initialdir = dir_path)   

    # Open video and get some info
    cap = cv.VideoCapture(filename)
    fps = int(cap.get(cv.CAP_PROP_FPS))
    dimentions = get_Video_Dimentions(cap)

    # Codec and save file object
    fourcc = cv.VideoWriter_fourcc(*__codec__)
    out = cv.VideoWriter(output_filename, fourcc, fps, dimentions)

    if(is_Long_Enough(cap)):
        process_Video(cap, out)
        cap.release()
        out.release()
        cv.destroyAllWindows()
    else:
        print("ERROR: Video not 6 seconds or longer")

if __name__ == "__main__":
    main()