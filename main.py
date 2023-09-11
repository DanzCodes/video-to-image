"""
    With this code u can get the first frame of a video and convert it to any image format

    Instructions:
    1. Put your video in the 'in' folder
    2. Change VIDEO_INPUT to your file name (don't forget add the extension)
    3. You can change OUTPUT_IMAGE but it isn't obligatory
    4. Run code
    5. You code will be in the 'out' folder ;)
"""

import cv2 as cv

VIDEO_INPUT = "test.mp4" #add your video file name here
OUTPUT_IMAGE = "test.jpg" #this will be the file save

def main():
    video = cv.VideoCapture(f'./in/{VIDEO_INPUT}')

    if video.isOpened():
        success, frame = video.read()
        if success is None: return print("Error reading video")

        savedImage = cv.imwrite(f"./out/{OUTPUT_IMAGE}", frame)

        if not savedImage: return print("Error saving image, try again")

        video.release()
        return True
    else:
        return print("Video not loaded")

main()