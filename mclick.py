import time
import cv2
import numpy
import pyautogui as ag
from context import *


class Click:
    def __init__(self):
        self.btn_dict = {}
        self.init()

    def init(self):
        self.btn_dict = btn_dict

    def click_btn(self, name, times=1, interval=0.5, wait=0):
        if wait:
            time.sleep(wait)
        print('click %s times = %s' % (name, times))
        x, y = self.btn_dict[name]
        ag.click(x, y, times, interval)
