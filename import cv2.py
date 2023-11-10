import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("C:\\Users\\omery\\OneDrive\\Resimler\\sabiha.jpeg",cv2.IMREAD_GRAYSCALE)
if resim is not None:
    hist = cv2.calcHist([resim],[0],None,[256],[0,256])

    plt.hist(resim.ravel(),256,[0,256])
    plt.xlabel('Piksel Değeri')
    plt.ylabel('Piksel Sayisi')
    plt.title('Gri Resim Histogrami')
    plt.show()
else:
    print("Resim yüklenemedi veya bulunamadi.")