import cv2
imagenn = cv2.imread("img1.png")
grices= cv2.cvtColor(imagenn,cv2.COLOR_BGR2GRAY)

# mostrar: 
cv2.imshow("Imagen color: ",imagenn)
cv2.imshow("imagen blanco y negro: ", grices)
cv2.waitKey(0)
cv2.destroyAllWindows()


