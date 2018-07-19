from PIL import Image

import cv2

import time
import curses

import subprocess
import os
import pickle

def play_video(video_chars):
    """
    播放字符视频，
    :param video_chars: 字符画的列表，每个元素为一帧
    :return: None
    """
    import time
    import curses

    width, height = len(video_chars[0][0]), len(video_chars[0])

    stdscr = curses.initscr()
    curses.start_color()
    try:
        stdscr.resize(height, width * 2)

        for pic_i in range(len(video_chars)):
            for line_i in range(height):
                stdscr.addstr(line_i, 0, video_chars[pic_i][line_i], curses.COLOR_WHITE)
            stdscr.refresh()  

            time.sleep(1 / 60)  
    finally:
        curses.endwin()
    return

def ReadVideo():
    Size = (128, 96)
    IMG_List = []
    VidCap = cv2.VideoCapture('./BadApple.mp4')
    i = 0
    while VidCap.isOpened():
        Ret, Frame = VidCap.read()
        if Ret:
            Gray = cv2.cvtColor(Frame, cv2.COLOR_BGR2GRAY)
            Img = cv2.resize(Gray, Size, interpolation=cv2.INTER_AREA)
            IMG_List.append(Img)
        else:
            break
    VidCap.release()
    return IMG_List


def CoverChar(Img):
    AsciiC = " .,-'`:!1+*abcdefghijklmnopqrstuvwxyz<>()\/{}[]?234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ%&@#$"

    CharFrame = []
    Height, Width = img.shape

    for Row in range(Height):
        line = ""
        for Col in range(Width):
            Percent = Img[Row][Col]/255
            index = int(Percent * (len(AsciiC) - 1))
            line += AsciiC[index] + " "
        CharFrame.append(line)
    return CharFrame

    ASCPercent = Gray/255
    print(int(ASCPercent*(len(AsciiC)-1)))
    return AsciiC[int(ASCPercent*(len(AsciiC)-1))]

if os.path.isfile("./Buffer/BadApple.pickle"):
    with open("./Buffer/BadApple.pickle",'rb') as File:
        FrameChars = pickle.load(File)
else:
    imgs = ReadVideo()
    FrameChars = []
    for img in imgs:
        FrameChars.append(CoverChar(img))
    with open("./Buffer/BadApple.pickle",'wb') as File:
        pickle.dump(FrameChars,File)
input("`转换完成！按enter键开始播放")
play_video(FrameChars)
# width, height = len(FrameChars[0][0]), len(FrameChars[0])
# for pic_i in range(len(FrameChars)):
#     for line_i in range(height):
#         print(FrameChars[pic_i][line_i])
#     #time.sleep(1 / 24)  

#     subprocess.call("clear") 
