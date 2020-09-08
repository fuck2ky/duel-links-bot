import cv2

global img
global point1, point2


# 鼠标响应函数
def Rectangular_box(event, x, y, flags, param):
    global img, point1, point2
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:  # 左键点击
        point1 = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):  # 按住左键拖曳
        cv2.rectangle(img2, point1, (x, y), (0, 0, 255), 1)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:  # 左键释放
        point2 = (x, y)
        cv2.rectangle(img2, point1, point2, (0, 0, 255), 1)
        cv2.imshow('image', img2)
        key = cv2.waitKey(2000)
        if key != ord('q'):
            img = img2
            cv2.rectangle(img2, point1, point2, (0, 0, 0), 1)
            cv2.imshow('image', img2)
            cx = int((point1[0] + point2[0]) / 2)
            cy = int((point1[1] + point2[1]) / 2)
            w = point2[0] - point1[0]
            h = point2[1] - point1[1]
            print('%d，%d，%d，%d' % (cx,cy,w,h))
        else:
            cv2.imshow('image', img)


def main():
    global img
    img = cv2.imread(u"app.jpg")
    cv2.namedWindow("image")
    cv2.setMouseCallback('image', Rectangular_box)
    cv2.imshow('image', img)
    cv2.waitKey(0)


if __name__ == '__main__':
    main()
