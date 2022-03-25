import datetime
import threading
import time

import numpy
from PIL import ImageGrab
#标志位
from pynput import keyboard

flag = False
def video_record():
    name = time.strftime("%Y-%m-%d %H:%M:%S")
    # 获取当前屏幕

    k = numpy.zeros((200, 200), numpy.uint8)
    p = ImageGrab.grab()
    #获取当前屏幕尺寸
    a,b = p.size
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter('%s.avi' % name, fourcc, 20, (a, b))
    while 1:
        im = ImageGrab.grab()
        imm = cv2.cvtColor(numpy.array(im), cv2.COLOR_RGB2BGR)
        video.write(imm)
        cv2.imshow('imm', k)
        if flag==True:
            print('结束')
            break
    video.release()

    print(a,b)
def on_press(key):
    global  flag
    if key ==keyboard.Key.esc:
        flag =True
        print('停止录制')
        return False
if __name__ == '__main__':
    import cv2
#     addr = r'F:\Users\admin\PycharmProjects\untitled\practice\test_pytest_my\img\img11.jpeg'
#     #读一张图片
#     # 完整读入图片
#     # img = cv2.imread(r'F:\Users\admin\PycharmProjects\untitled\practice\test_pytest_my\img\img11.jpeg',cv2.IMREAD_UNCHANGED)
#     # 默认参数，读入一副彩色图片，忽略alpha通道
#     # img = cv2.imread(r'F:\Users\admin\PycharmProjects\untitled\practice\test_pytest_my\img\img11.jpeg',cv2.IMREAD_COLOR)
#     # 读灰色图片
#     img = cv2.imread(addr,cv2.IMREAD_GRAYSCALE)
#     # 它针对特定的格式：对于JPEG
#     cv2.imwrite(addr, img, [int(cv2.IMWRITE_PNG_COMPRESSION), 1])
#     #使用image将图片展示出来
#     cv2.imshow('image',img)
#
#     #参数为0表示无限等待。不调用waitKey的话，窗口会一闪而逝，看不到显示的图片。单位为毫秒
#     cv2.waitKey(0)
#     #摧毁所有窗口
#     # cv2.destroyAllWindows()
#     cv2.destroyWindow(img)#销毁指定窗口
# #
    th = threading.Thread(target=video_record)
    th.start()
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
