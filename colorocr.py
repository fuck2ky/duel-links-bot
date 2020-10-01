import cv2
import numpy as np
import pytesseract
import pyautogui as ag
from context import *
import numpy as np


class Ocr:
    def __init__(self, color=(18, 0, 160, 36, 255, 255)):
        self.color = color

    def do(self, c=None, img=None, region=None, words='', orway=False):
        if c is not None:
            self.color = c
        if img is None:
            img = cv2.cvtColor(np.asarray(ag.screenshot()), cv2.COLOR_RGB2BGR)

        if region:
            img = img[region[1]:region[3], region[0]:region[2]]
            img = cv2.resize(img, (int(img.shape[1] * 4), int(img.shape[0] * 4)))

        frameBGR = cv2.GaussianBlur(img, (7, 7), 0)

        frameHSV = cv2.cvtColor(frameBGR, cv2.COLOR_BGR2HSV)
        colorLow = np.array(self.color[0:3])
        colorHigh = np.array(self.color[3:])
        mask = cv2.inRange(frameHSV, colorLow, colorHigh)

        _, th = cv2.threshold(mask, 10, 255, cv2.THRESH_BINARY_INV)

        code = pytesseract.image_to_string(th, config='--psm 7', lang='chi_sim')
        if code == '':
            print('not find words')
            return False
        if not words:
            return code
        else:
            for i in words_dict[words]:
                if i not in code:
                    if not orway:
                        print(str(words_dict[words]) + ' is  not in' + str(code))
                        return False
                elif orway:
                    print(str(words_dict[words]) + ' is in' + str(code))
                    return True

        if orway:
            return False
        print(str(words_dict[words]) + ' is in ' + str(code))
        return True


if __name__ == '__main__':
    o = Ocr()
    c = (83, 0, 10, 255, 255, 176)
    o.color = c
    res = o.do(img=cv2.imread('./image/test/9.jpg'))
    print(res)
