#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2
import numpy as np

#Filterクラス スーパークラス 
class Filter():
    #画像を受け取るメソッド nは1の時がグレースケール  0はRGB -1はRGBA
    def transform(self,img,n):   
        if n==1:  #グレースケールをimreadに入れることはできないためこのように画像を保持する
            self.img=img
        else:  
            self.img=cv2.imread(img)    #画像を読む
                
    #画像を返すメソッド
    def getimg(self):
        return self.img    
       
#Gammaクラス サブクラス  画像をガンマにする
class Gamma(Filter):    
    def gammado(self):  #ガンマにするメソッド
        
        #線形濃度変換
        scale=0.5
        
        # 画素値の最大値
        imax =(filterimg.getimg()).max()
    
        # ガンマ補正
        gray = imax*(filterimg.getimg()/ imax)*(1/scale)
        
        return gray  #ガンマの画像を返す
        
#Monoクラス サブクラス  画像をモノクロにする  
class Mono(Filter):
    def monodo(self):  #モノクロにするメソッド
        gray_img=cv2.cvtColor(filterimg.getimg(),cv2.COLOR_RGB2GRAY)  #受け取った家蔵をモノクロにする
        return gray_img #モノクロ画像を返す
              
#フィルターの組み合わせが出来るクラス
class CompositeFilter():
            
    def tasu(self):  #フィルターを組み合わせるメソッド
        for i in range(8):  #モノクロ、ガンマを足すことを繰り返す
            mono=Mono()  #同じクラスをもう一つインスタンス
            gamma=Gamma() #同様
            array1 = np.array(mono.monodo(), dtype=object)  #モノクロにする
            array2 = np.array(gamma.gammado(), dtype=object)  #ガンマにする
            print(array1.shape+array2.shape)  #それぞれのフィルターを足す  shapeにしないと行列の計算不可
        
#Client　
filterimg=Mono()  #Monoクラスのインスタンス化 　モノクロにする
filterimg.transform('medical_kentai_daeki.png',-1)  #Monoクラスのtransform(img)を呼ぶ  
filterimg.getimg()  #最初の画像を受け取る
imgmono=filterimg.monodo()  #モノクロ画像にする   

filterimg=Gamma()  #Gammaクラスのインスタンス化 ガンマにする
filterimg.transform(imgmono,1)  #モノクロにした画像を送る
filterimg.getimg()  #受け取る
imggamma=filterimg.gammado() #ガンマにした画像を返す

filterimg.transform('medical_kentai_daeki.png',-1)  #フィルターオブジェクト に対し、transform()を呼んでimgに代入
img=filterimg.getimg()  #取得した画像をimgに代入

gatai=CompositeFilter()  #ガンマとモノクロを組み合わせる
gatai.tasu()  #それぞれのフィルターを足すメソッド


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




