import cv2
from tkinter import Scale

image = cv2.imread("resim.png")

# Gri tonlamaya çevir
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img)
# Bulanıklaştır
blur = cv2.GaussianBlur(invert, (17, 17), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)

# Çıktıyı kaydet
cv2.imwrite("ciktiresmi5.png", sketch)
