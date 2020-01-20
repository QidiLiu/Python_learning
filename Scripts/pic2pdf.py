import glob
import fitz
import os

'''
代码来源↓↓↓

版权声明：本文为CSDN博主「XnCSD」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/XnCSD/article/details/80849996
'''

def pic2pdf():
    doc = fitz.open()
    for img in sorted(glob.glob("C:/Users/adi03/Desktop/img/*")):  # 读取图片，确保按文件名排序
        print(img)
        imgdoc = fitz.open(img)                 # 打开图片
        pdfbytes = imgdoc.convertToPDF()        # 使用图片创建单页的 PDF
        imgpdf = fitz.open("pdf", pdfbytes)
        doc.insertPDF(imgpdf)                   # 将当前页插入文档
    #if os.path.exists("C:/Users/adi03/Desktop/backup/allimages.pdf"):
        #os.remove("C:/Users/adi03/Desktop/backup/allimages.pdf")
    doc.save("C:/Users/adi03/Desktop/allimages_test.pdf")                   # 保存pdf文件
    doc.close()

if __name__ == '__main__':
    pic2pdf()
