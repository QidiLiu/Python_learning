from os import listdir, rename

'批量重命名'

path = ('C:/Users/adi03/Desktop/backup/')
f = listdir(path)
n = 0

for i in f:
    old_name = path + f[n] # 记录旧文件名
    new_name = path + str(n) + '.jpg' # 新文件名
    rename(old_name, new_name) # 重命名
    n += 1
