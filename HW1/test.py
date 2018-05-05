import os 
from PIL import Image
import numpy as np

E = Image.open("E.png")
Eprime = Image.open("Eprime.png")
I = Image.open("I.png")
key1 = Image.open("key1.png")
key2 = Image.open("key2.png")
#讀取圖片

Edata = np.array(E)
Epdata = np.array(Eprime)
Idata = np.array(I)
key1data = np.array(key1)
key2data = np.array(key2)
#設定圖片為二維陣列

w = np.array([1,1,1])
#初始化weight

epoch = 1
test = np.zeros((300,400),int)
#設定要輸出的矩陣大小

for epoch in range(2):
    for i in range(300):
        for j in range(400):
            a = np.dot(np.transpose(w),np.transpose(np.array([key1data[i , j], key2data[i , j], Idata[i , j]])))
            e = Edata[i , j] - a
            w = w + (0.00001 * e * np.transpose(np.array([key1data[i , j], key2data[i , j], Idata[i , j]])))
#利用Least Mean Square演算法,求出W1,W2,W3

for i in range(300):
    for j in range(400):
        test[i , j] = (Epdata[i , j] - w[0] * key1data[i , j] - w[1] * key2data[i , j]) / w[2]
        if test[i , j] > 255:
            test[i , j] = 255
        elif test[i , j] < 0:
            test[i , j] = 0
#利用解密公式得出解密圖
            

test = np.array(test, dtype = np.uint8)
#int轉成uint8
prtest = Image.fromarray(test)
#將矩陣轉成圖片
prtest.save("解密圖片.png")


os.system("pause")
