from PIL import Image
from os import listdir
import PIL.ImageOps

'批量图片颜色反转'

path = ('C:/Users/adi03/Downloads/')
out_path = ('C:/Users/adi03/Desktop/backup/')
f = listdir(path)

for i in f:
    if i=='0.jpg': # 莫名其妙的Bug。文件夹里明明没0.jpg，第一个读的偏偏是个0.jpg
        continue
    img = Image.open(path+i)
    inv_img = PIL.ImageOps.invert(img)
    if(int(i.split('.')[0])<10): # 这里的判断语句只考虑了10000页以内（不含10000页的情况）
        new_i = '000' + i
    elif(int(i.split('.')[0])<100):
        new_i = '00' + i
    elif(int(i.split('.')[0])<1000):
        new_i = '0' + i
    else:
        new_i = i
    inv_img.save(out_path+new_i)
