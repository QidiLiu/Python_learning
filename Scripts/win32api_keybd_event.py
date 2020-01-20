#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import win32api # 该库是对win32api的封装
import win32con # 该库给出了win32各常量，我试了下不用这个库其实也能运行
import threading
import time

PROGRAM_STATUS = True

def blingbling(): # 模拟每隔一秒按一次大写锁定键的进程
    while PROGRAM_STATUS:
        win32api.keybd_event(20,0,0,0) # 按下大写锁定键
        win32api.keybd_event(20,0,win32con.KEYEVENTF_KEYUP,0) # 松开大写锁定键
        time.sleep(1) # 延时1秒

def sim_a(): # 模拟键盘输入a
    while PROGRAM_STATUS:
        win32api.keybd_event(65,0,0,0) # 按下A键
        win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0) # 松开A键
        win32api.keybd_event(13,0,0,0) # 按下回车键
        win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0) # 松开回车键
        time.sleep(1) # 延时1秒

def main(): # 多进程安排一哈
    threading.Thread(target=blingbling).start()
    threading.Thread(target=sim_a).start()

if __name__ == "__main__":
    main()
    while PROGRAM_STATUS:
        a = input('当前模拟输入的字母A/a：')