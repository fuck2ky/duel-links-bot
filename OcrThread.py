import cv2
import numpy as np
import pytesseract
import pyautogui as ag
from context import *
import numpy as np
import threading
import log

log = log.Logger('duel.log', level='debug')


class OcrThread(threading.Thread):
    def __init__(self, name, region=None, color=None):
        threading.Thread.__init__(self, name=name)
        self.region = region
        self.color = color
        self.txt = ''
        self.thread_stop_flag = False
        self.resize_num = 8

    def stop(self):
        self.thread_stop_flag = True

    def img_filter(self, img):
        img = cv2.GaussianBlur(img, (7, 7), 0)
        if self.color is not None:
            img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            color_low = np.array(self.color[0:3])
            color_high = np.array(self.color[3:])
            img = cv2.inRange(img_hsv, color_low, color_high)
            _, th = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY_INV)
            return th
        else:
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            _, th = cv2.threshold(gray, 10, 255, cv2.THRESH_BINARY_INV)
        return th

    def run(self):
        while True:
            if self.thread_stop_flag:
                break
            img = cv2.cvtColor(np.asarray(ag.screenshot()), cv2.COLOR_RGB2BGR)
            if self.region:
                img = img[self.region[1]:self.region[3], self.region[0]:self.region[2]]
                img = cv2.resize(img, (int(img.shape[1] * self.resize_num), int(img.shape[0] * self.resize_num)))
            th = self.img_filter(img)
            cv2.imwrite('./image/test/thread-1.jpg', th)
            self.txt = pytesseract.image_to_string(th, config='--psm 7', lang='chi_sim')
        log.logger.warning('end thread')


if __name__ == '__main__':
    c = (18, 0, 160, 36, 255, 255)
    o = OcrThread('test', (1517, 197, 1665, 232), c)
    o.start()
    log.logger.warning('start thread')
    while True:
        print(o.txt)
