from PIL import ImageGrab
import winsound,time
def getpic():
    im = ImageGrab.grab((0,0,1920,1080))
    #print(im.size)
    im.save('template/target1.png','png')
if __name__ == '__main__':
    getpic()
