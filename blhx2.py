import time
import random
import winsound
import win32api,win32gui,win32con
from ctypes import *
from PIL import ImageGrab
import winsound,time
import mubanpipei
import getpic
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
    x = 960+random.randint(200,300)*(-1)**random.randint(2,4)
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
def getenemy():
    if mubanpipei.template_demo("map") == (0,0):
        return (1600,870)
    global bossflag
    getpic.getpic()
    xy = mubanpipei.template_demo("boss")
    if xy != (0,0):
        if bossflag == 0:
            moveCurPos(1500,940)
            clickLeftCur()
        bossflag = 1
        return xy
    elif bossflag == 1:
        mouse_randmove()
        return getenemy()
    el = mubanpipei.template_demo("elite")
    if  el!= (0,0):
        return (el[0],el[1]+80)
    el = mubanpipei.template_demo("elite2")
    if  el!= (0,0):
        return (el[0],el[1]+80)
    el = mubanpipei.template_demo("elite3")
    if  el!= (0,0):
        return (el[0],el[1]+80)
    el = mubanpipei.template_demo("elite4")
    if  el!= (0,0):
        return (el[0],el[1]+80)
    xys = [mubanpipei.template_demo("hangkong"),mubanpipei.template_demo("yunshu"),mubanpipei.template_demo("zhencha"),mubanpipei.template_demo("zhuli")]
    for i in xys:
        if i != (0,0):
            return i
    mouse_randmove()
    return getenemy()
time.sleep(3)
winsound.Beep(600,500)
winsound.Beep(600,500)
while 1:
    getpic.getpic()
    if mubanpipei.template_demo("worldmap2") != (0,0):#进入关卡
        #moveCurPos(1430,770)
        #clickLeftCur()
        randomClick((1267,412,1483,459))
        time.sleep(2)
        #moveCurPos(1380,700)
        #clickLeftCur()
        randomClick((1277,695,1494,754))
        time.sleep(2)
        #moveCurPos(1550,850)
        #clickLeftCur()
        randomClick((1425,805,1662,866))
        time.sleep(5)
        bossflag = 0
        winsound.Beep(600,500)
    elif mubanpipei.template_demo("fuji") != (0,0):#被伏击
        winsound.Beep(1000,500)
        moveCurPos(1530,665)
        clickLeftCur()
        time.sleep(3)
    elif mubanpipei.template_demo("chujiqueren") != (0,0):#确认交战
        winsound.Beep(900,500)
        #moveCurPos(1600,870)
        #clickLeftCur()
        randomClick((1520,850,1718,909))
        time.sleep(30)
    elif mubanpipei.template_demo("shengli") != (0,0):#确认胜利
        moveCurPos(1000,150)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        #moveCurPos(1540,910)
        #clickLeftCur()
        randomClick((1454,879,1643,940))
        time.sleep(5)
    elif mubanpipei.template_demo("map") != (0,0):#地图内，寻找敌人
        winsound.Beep(700,500)
        x,y = getenemy()
        winsound.Beep(700,500)
        moveCurPos(x,y)
        clickLeftCur()
        time.sleep(5)#试图交战
    elif mubanpipei.template_demo("err1") != (0,0):#结算卡住
        moveCurPos(1000,150)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        clickLeftCur()
        time.sleep(2)
        moveCurPos(1540,910)
        clickLeftCur()
        time.sleep(5)
    elif mubanpipei.template_demo("task") != (0,0):#紧急委托
        moveCurPos(965,715)
        clickLeftCur()
        time.sleep(2)


#winsound.Beep(600,500)
#winsound.Beep(600,500)
#winsound.Beep(600,500)
    