##### 機器學習導論 HW1 #
--------------------------
<ol>
  <li>利用PIL (pillow)來讀取影像檔</li>
  <li>將影像檔案讀取的陣列移轉到numpy來處理</li>
  <li>用Least Mean Square演算法求出W</li>
  <li>用公式(Eprime - w1k1 -w2k2 ) / w3 = 圖片解密</li>
</ol>


  <li>w = 0.24914331  0.6613819  0.08923953</li>
  <li>α = 0.00001</li>

#### 轉換前 #
![Alt text](https://github.com/Yukino0103/ML2018_410421254/blob/master/HW1/Eprime.png)

#### 轉換後 #
![Alt text](https://github.com/Yukino0103/ML2018_410421254/blob/master/HW1/%E8%A7%A3%E5%AF%86%E5%9C%96%E7%89%87.png)



#### 難點 #
![Alt text](https://github.com/Yukino0103/ML2018_410421254/blob/master/HW1/temp.jpg)
其實演算法中while的條件我有點不明白,所以我沒有用到while中一些的條件,嘗試後也能跑出圖片,但我明白自已的程式是有缺憾的,對演算法不太熟練,感覺只是對著那個步驟寫出code

#### 學習 #
Pythonm不太熟練,因此感覺讀取圖片的code不太好,因為後來發現Python圖像庫有很多種可以用,如opencv , PIL , matplotlib.image , scipy.misc , skimage , 應該找一個直接讀取圖片的二維陣列的,我也學會了Github的基本功能
  <li>參考網站:</li>
http://chu246.blogspot.tw/2017/12/python-numpy.html

https://blog.csdn.net/u012609509/article/details/70230204

https://blog.csdn.net/u012762410/article/details/78912667

https://blog.csdn.net/qq_26948675/article/details/54318917

https://www.ywlib.com/archives/37.html

https://wolfsonliu.github.io/archive/python-xue-xi-bi-ji-numpy.html

