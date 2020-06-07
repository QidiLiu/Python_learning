
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'QidiLiu'

import tkinter as tk

ft_1 = ('Arial', 16, 'bold') # 集中设置font

root = tk.Tk()
root.title('title of window')

#↓↓ if screen's size is needed ↓↓
#w = root.winfo_screenwidth()
#h = root.winfo_screenheight()
#root.geometry(f'{round(w/2)}x{round(h/2)}')

fr_1 = tk.Frame(root)
fr_1.grid(row=0, column=0) # grid布局详解：https://www.cnblogs.com/ruo-li-suo-yi/p/7425307.html
fr_2 = tk.Frame(root)
fr_2.grid(row=0, column=1)
fr_3 = tk.Frame(root)
fr_3.grid(row=0, column=2)
fr_4 = tk.Frame(root)
fr_4.grid(row=0, column=3)
fr_5 = tk.Frame(root)
fr_5.grid(row=0, column=4)
fr_6 = tk.Frame(root)
fr_6.grid(row=0, column=5)
fr_7 = tk.Frame(root)
fr_7.grid(row=0, column=6)
fr_8 = tk.Frame(root)
fr_8.grid(row=0, column=7)

font_list = [
'System', 
'Terminal',
'Fixedsys',
'Modern',
'Roman',
'Script',
'Courier',
'MS Serif',
'MS Sans Serif',
'Small Fonts',
'Marlett',
'Arial',
'Arabic Transparent',
'Arial Baltic',
'Arial CE',
'Arial CYR',
'Arial Greek',
'Arial TUR',
'Arial Black',
'Bahnschrift Light',
'Bahnschrift SemiLight',
'Bahnschrift',
'Bahnschrift SemiBold',
'Bahnschrift Light SemiCondensed',
'Bahnschrift SemiLight SemiConde',
'Bahnschrift SemiCondensed',
'Bahnschrift SemiBold SemiConden',
'Bahnschrift Light Condensed',
'Bahnschrift SemiLight Condensed',
'Bahnschrift Condensed',
'Bahnschrift SemiBold Condensed',
'Calibri',
'Calibri Light',
'Cambria',
'Cambria Math',
'Candara',
'Candara Light',
'Comic Sans MS',
'Consolas',
'Constantia',
'Corbel',
'Corbel Light',
'Courier New',
'Courier New Baltic',
'Courier New CE',
'Courier New CYR',
'Courier New Greek',
'Courier New TUR',
'Ebrima',
'Franklin Gothic Medium',
'Gabriola',
'Gadugi',
'Georgia',
'Impact',
'Ink Free',
'Javanese Text',
'Leelawadee UI',
'Leelawadee UI Semilight',
'Lucida Console',
'Lucida Sans Unicode',
'Malgun Gothic',
'@Malgun Gothic',
'Malgun Gothic Semilight',
'@Malgun Gothic Semilight',
'Microsoft Himalaya',
'Microsoft JhengHei',
'@Microsoft JhengHei',
'Microsoft JhengHei UI',
'@Microsoft JhengHei UI',
'Microsoft JhengHei Light',
'@Microsoft JhengHei Light',
'Microsoft JhengHei UI Light',
'@Microsoft JhengHei UI Light',
'Microsoft New Tai Lue',
'Microsoft PhagsPa',
'Microsoft Sans Serif',
'Microsoft Tai Le',
'Microsoft YaHei',
'@Microsoft YaHei',
'Microsoft YaHei UI',
'@Microsoft YaHei UI',
'Microsoft YaHei Light',
'@Microsoft YaHei Light',
'Microsoft YaHei UI Light',
'@Microsoft YaHei UI Light',
'Microsoft Yi Baiti',
'MingLiU-ExtB',
'@MingLiU-ExtB',
'PMingLiU-ExtB',
'@PMingLiU-ExtB',
'MingLiU_HKSCS-ExtB',
'@MingLiU_HKSCS-ExtB',
'Mongolian Baiti',
'MS Gothic',
'@MS Gothic',
'MS UI Gothic',
'@MS UI Gothic',
'MS PGothic',
'@MS PGothic',
'MV Boli',
'Myanmar Text',
'Nirmala UI',
'Nirmala UI Semilight',
'Palatino Linotype',
'Segoe MDL2 Assets',
'Segoe Print',
'Segoe Script',
'Segoe UI',
'Segoe UI Black',
'Segoe UI Emoji',
'Segoe UI Historic',
'Segoe UI Light',
'Segoe UI Semibold',
'Segoe UI Semilight',
'Segoe UI Symbol',
'SimSun',
'@SimSun',
'NSimSun',
'@NSimSun',
'SimSun-ExtB',
'@SimSun-ExtB',
'Sitka Small',
'Sitka Text',
'Sitka Subheading',
'Sitka Heading',
'Sitka Display',
'Sitka Banner',
'Sylfaen',
'Symbol',
'Tahoma',
'Times New Roman',
'Times New Roman Baltic',
'Times New Roman CE',
'Times New Roman CYR',
'Times New Roman Greek',
'Times New Roman TUR',
'Trebuchet MS',
'Verdana',
'Webdings',
'Wingdings',
'Yu Gothic',
'@Yu Gothic',
'Yu Gothic UI',
'@Yu Gothic UI',
'Yu Gothic UI Semibold',
'@Yu Gothic UI Semibold',
'Yu Gothic Light',
'@Yu Gothic Light',
'Yu Gothic UI Light',
'@Yu Gothic UI Light',
'Yu Gothic Medium',
'@Yu Gothic Medium',
'Yu Gothic UI Semilight',
'@Yu Gothic UI Semilight',
'HoloLens MDL2 Assets',
'BIZ UDGothic',
'@BIZ UDGothic',
'BIZ UDPGothic',
'@BIZ UDPGothic',
'BIZ UDMincho Medium',
'@BIZ UDMincho Medium',
'BIZ UDPMincho Medium',
'@BIZ UDPMincho Medium',
'Meiryo',
'@Meiryo',
'Meiryo UI',
'@Meiryo UI',
'MS Mincho',
'@MS Mincho',
'MS PMincho',
'@MS PMincho',
'UD Digi Kyokasho N-B',
'@UD Digi Kyokasho N-B',
'UD Digi Kyokasho NP-B',
'@UD Digi Kyokasho NP-B',
'UD Digi Kyokasho NK-B',
'@UD Digi Kyokasho NK-B',
'UD Digi Kyokasho N-R',
'@UD Digi Kyokasho N-R',
'UD Digi Kyokasho NP-R',
'@UD Digi Kyokasho NP-R',
'UD Digi Kyokasho NK-R',
'@UD Digi Kyokasho NK-R',
'Yu Mincho',
'@Yu Mincho',
'Yu Mincho Demibold',
'@Yu Mincho Demibold',
'Yu Mincho Light',
'@Yu Mincho Light',
'DengXian',
'@DengXian',
'DengXian Light',
'@DengXian Light',
'FangSong',
'@FangSong',
'KaiTi',
'@KaiTi',
'SimHei',
'@SimHei',
'Ubuntu',
'Raleway',
'Ubuntu Condensed',
'Ubuntu Light'
]
n = 0
for f in font_list:
    n += 1
    if n<=25:
        tk.Label(fr_1, text=f+'给阿姨倒杯卡布奇诺', font=(f, 12)).pack()
    elif n<=50:
        tk.Label(fr_2, text=f+'给阿姨倒杯卡布奇诺', font=(f, 12)).pack()
    elif n<=75:
        tk.Label(fr_3, text=f+'给阿姨倒杯卡布奇诺', font=(f, 12)).pack()
    elif n<=100:
        tk.Label(fr_4, text=f+'给阿姨倒杯卡布奇诺', font=(f, 12)).pack()
    elif n<=125:
        tk.Label(fr_5, text=f+'给阿姨倒杯卡布奇诺', font=(f, 12)).pack()
    elif n<=150:
        tk.Label(fr_6, text=f+'给阿姨倒杯卡布奇诺', font=(f, 12)).pack()
    elif n<=175:
        tk.Label(fr_7, text=f+'给阿姨倒杯卡布奇诺', font=(f, 12)).pack()
    else:
        tk.Label(fr_8, text=f+'给阿姨倒杯卡布奇诺', font=(f, 12)).pack()

root.mainloop()