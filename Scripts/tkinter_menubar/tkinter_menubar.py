#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter

def wang1():
    radio.set('单身狗：汪~')

def wang2():
    radio.set('旺财：汪~')

def wang3():
    radio.set('大黄：汪~')

if __name__ == '__main__':
    # 创建窗口和信息展示框
    win = tkinter.Tk() # win从石头缝里蹦出来了
    win.title('tkinter菜单栏')
    win.geometry('300x100')
    radio = tkinter.StringVar()
    label = tkinter.Label(win,textvariable=radio,height=2,font=('Arial',24))
    label.place(x=150,y=50,anchor='center')

    # 创建菜单栏
    menubar = tkinter.Menu(win) # menubar出生了，并叫了win一声爹/娘
    win['menu'] = menubar # win答应了一声，说以后你就是我的'menu'了

    # 添加菜单
    menu_1 = tkinter.Menu(menubar, tearoff=0) # menubar有三个孩子，老大叫menu_1
    menu_2 = tkinter.Menu(menubar, tearoff=0) # 老二叫menu_2，老三太皮了就没给起名

    # menubar不想跟孩子们分家，于是把tearoff都设为了0

    menubar.add_cascade(menu=menu_1, label='菜单1') # menubar给孩子起了小名，平时叫老大菜单1
    menubar.add_cascade(menu=menu_2, label='菜单2') # 叫老二菜单2
    menubar.add_command(command=wang1, label='单身狗') # 老三整天学狗叫，村里没人跟他玩，都叫他'单身狗'

    # 菜单项目
    menu_1.add_command(command=wang2,label='旺财') # 老大没要孩子，养了两条狗，一条叫“旺财”
    menu_1.add_command(command=wang3,label='大黄') # 零一条叫“大黄”

    # 分菜单
    menu_21 = tkinter.Menu(menu_2, tearoff=0) # 老二有俩孩子，一个叫menu_21
    menu_22 = tkinter.Menu(menu_2, tearoff=0) # 另一个叫menu_22
    menu_2.add_cascade(menu=menu_21, label='分菜单1') # 老二给俩孩子起的小名分别叫“分菜单1”和“分菜单2”
    menu_2.add_separator() # 两人经常打架，于是老二在两人之间画了条线分开
    menu_2.add_cascade(menu=menu_22, label='分菜单2')

    # 单选框
    menu_21.add_radiobutton(label='大咪', variable=radio, value='大咪：喵~') # 分菜单1养了两只猫：大咪和小咪
    menu_21.add_radiobutton(label='小咪', variable=radio, value='小咪：喵~') # 他每次只撸其中一只

    # 自带图标
    icon1 = tkinter.PhotoImage(file = 'image/tkinter_menubar_1.gif') # 分菜单有俩表情包
    icon2 = tkinter.PhotoImage(file = 'image/tkinter_menubar_2.gif')
    menu_22.add_command(compound='right',label='1 ',image=icon1)
    menu_22.add_command(compound='right',label='2 ',image=icon2)

    win.mainloop()
