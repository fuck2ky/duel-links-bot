# coding: utf-8
import cv2
import pyautogui
if __name__ == "__main__":


    def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
        global flag
        global X
        global Y
        if event == cv2.EVENT_LBUTTONDOWN:
            if flag == 0:
                X=x
                Y=y
                flag =1
            xy = "%d,%d" % (x, y)
            print(xy)
            print(x-X, y-Y)
            cv2.circle(img, (x, y), 5, (255, 255, 255), thickness=-1)
            cv2.imshow("image", img)

    flag = 0
    X=0
    Y=0
    img = cv2.imread(u"../image/test/100.png")
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", on_EVENT_LBUTTONDOWN)
    cv2.imshow("image", img)

    while (True):
        try:
            cv2.waitKey(10)
        except Exception:
            cv2.destroyWindow("image")
            break

    cv2.waitKey(0)
    cv2.destroyAllWindow()
