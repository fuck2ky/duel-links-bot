import time
import pyautogui as ag
import threading

TITLE = 'Yu-Gi-Oh! DUEL LINKS'


class Window(threading.Thread):
    def __init__(self, interval):
        threading.Thread.__init__(self)
        self.interval = interval
        self.win = None
        self.__callback = None
        self.th_flag = False
        self.position = None
        self.__init_window()

    def __init_window(self):
        timeout = 0
        while True:
            self.win = ag.getActiveWindow()
            if self.win and self.win.title == TITLE:
                print('find duel links exe')
                return 0
            else:
                print('please open duel links or active!')
            timeout += 1
            time.sleep(1)
            if timeout == 10:
                return 1

    def start_window_watch(self, callback):
        self.__callback = callback
        self.th_flag = True

    def stop_window_watch(self):
        self.th_flag = False

    def run(self):
        while self.th_flag:
            if self.win.isActive:
                if not self.position or self.position != (self.win.left, self.win.top):
                    self.position = (self.win.left, self.win.top)
                    self.__callback(self.position)
            else:
                self.__callback(None)
                self.position = None
                print('duel links game is not active!')
            time.sleep(self.interval)
        self.position = None

