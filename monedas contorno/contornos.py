import cv2
imagenn = cv2.imread("img1.png")
grices= cv2.cvtColor(imagenn,cv2.COLOR_BGR2GRAY)

# mostrar: 
cv2.imshow("Está es tu imagen: ",grices)
cv2.
cv2.waitKey(0)
cv2.destroyAllWindows()


