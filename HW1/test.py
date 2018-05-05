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
    for k in range(300):
        for p in range(400):
            a = np.dot(np.transpose(w),np.transpose(np.array([key1data[k , p], key2data[k , p], Idata[k , p]])))
            e = Edata[k , p] - a
            w = w + (0.00001 * e * np.transpose(np.array([key1data[k , p], key2data[k , p], Idata[k , p]])))
#利用Least Mean Square演算法,求出W1,W2,W3

for k in range(300):
    for p in range(400):
        test[k , p] = (Epdata[k , p] - w[0] * key1data[k , p] - w[1] * key2data[k , p]) / w[2]
        if test[k , p] > 255:
            test[k , p] = 255
        elif test[k , p] < 0:
            test[k , p] = 0
#利用解密公式得出解密圖
            

test = np.array(test, dtype = np.uint8)
#int轉成uint8
prtest = Image.fromarray(test)
#將矩陣轉成圖片
prtest.save("解密圖片.png")


os.system("pause")
