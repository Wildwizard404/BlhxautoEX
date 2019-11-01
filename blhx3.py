import time
import random
import winsound
import win32api,win32gui,win32con
from ctypes import *
from PIL import ImageGrab
import winsound,time
import mubanpipei
import getpic
stateflag = [0]# 记录地图点击数量
def clickLeftCur():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN|win32con.MOUSEEVENTF_LEFTUP, 0, 0)
def getCurPos():
    return win32gui.GetCursorPos()
def moveCurPos(x,y):
    windll.user32.SetCursorPos(x, y)
def mouse_randmove():
    windll.user32.SetCursorPos(960, 540)    #鼠标移动到  
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)    #左键按下
    time.sleep(0.2)
    x = 960+random.randint(200,300)*(-1)**random.randint(1,3)
    y = 540+random.randint(200,300)*(-1)**random.randint(1,2)
    mw = int(x * 65535 / 1920) 
    mh = int(y * 65535 / 1080)
    win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE + win32con.MOUSEEVENTF_MOVE, mw, mh, 0, 0)    
    time.sleep(0.2)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
bossflag = 0
def randomClick(index):
    rx = random.randint(index[0],index[2])
    ry = random.randint(index[1],index[3])
    moveCurPos(rx,ry)
    clickLeftCur()
time.sleep(3)
winsound.Beep(600,500)
winsound.Beep(600,500)
ftimes = [15,0,0]
def win():
    moveCurPos(1000,150)
    clickLeftCur()
    time.sleep(0.5)
    clickLeftCur()
    time.sleep(0.5)
    clickLeftCur()
    time.sleep(0.5)
    clickLeftCur()
    time.sleep(0.5)
    clickLeftCur()
    time.sleep(0.5)
    clickLeftCur()
    time.sleep(0.5)
    #moveCurPos(1540,910)
    #clickLeftCur()
    randomClick((1454,872,1643,886))
while 1:
    getpic.getpic()
    if mubanpipei.template_demo("junhe") != (0,0):#进入关卡
        if ftimes[0]>0:
            ftimes[0] = ftimes[0] -1
            moveCurPos(1707,463)
        elif ftimes[1]>0:
            ftimes[1] = ftimes[1]-1
            moveCurPos(1795,613)
        elif ftimes[2]>0:
            ftimes[2] = ftimes[2]-1
            moveCurPos(1738,771)
        else:
            exit()
        clickLeftCur()
        time.sleep(2)
        randomClick((1420,800,1670,870))
        time.sleep(2)
        randomClick((1620,860,1840,890))
        winsound.Beep(400,500)
        print("进入关卡")
        gettime = time.time()
        while 1:
            getpic.getpic()
            if mubanpipei.template_demo("shengli") != (0,0) or time.time()-gettime > 140:
                win()
                break       
    elif mubanpipei.template_demo("task") != (0,0):#紧急委托
        moveCurPos(965,715)
        clickLeftCur()
        time.sleep(2)
    elif mubanpipei.template_demo("yingyuan") != (0,0):#应援
        moveCurPos(765,715)
        clickLeftCur()
        time.sleep(2)

#winsound.Beep(600,500)
#winsound.Beep(600,500)
#winsound.Beep(600,500)
    
