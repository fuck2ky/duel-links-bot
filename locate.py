import time
import cv2
import numpy
import pyautogui as ag
from context import *


class Location:
    def __init__(self):
        self.region_dict = {}
        self.init()

    def init(self):
        self.region_dict = region_dict

    def locate_img(self, img, region, timeout=1, click=False):
        # timeout 重试次数
        try:
            img_center = ag.locateCenterOnScreen(img, region=self.region_dict[region], confidence=0.8, grayscale=True)
        except ag.ImageNotFoundException:
            print('%s not find in %s' % (img, region))
            timeout -= 1
            if timeout == 0:
                return False
            else:
                time.sleep(1)
                return self.locate_img(img, region, timeout, click)
        if not img_center:
            print('%s not find in %s' % (img, region))
            timeout -= 1
            if timeout == 0:
                return False
            else:
                time.sleep(1)
                return self.locate_img(img, region, timeout, click)
        if click:
            x, y = img_center
            ag.click(x, y)
            print('%s find in %s and click!pos = %d,%d' % (img, region, x, y))
        else:
            print('%s find in %s' % (img, region))
        return True

    def middle(self):
        im1 = ag.screenshot()
        img = cv2.cvtColor(numpy.asarray(im1), cv2.COLOR_RGB2BGR)
        region = 'middle'
        x = self.region_dict[region][0]
        y = self.region_dict[region][1]
        w = self.region_dict[region][2]
        h = self.region_dict[region][3]
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.imshow('image', img)
        cv2.waitKey(0)
