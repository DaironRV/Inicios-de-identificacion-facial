import cv2
imagenn = cv2.imread("img1.png")
grices = cv2.cvtColor(imagenn,cv2.COLOR_BGR2GRAY)
_,umbral = cv2.threshold(grices, 143, 255, cv2.THRESH_BINARY)
# cv2.findContours
contornos, jerarquia = cv2.findContours(umbral, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(imagenn, contornos, -1 ,(112,48,174), 3)

# mostrar: 
cv2.imshow("Imagen color: ",imagenn)
# cv2.imshow("imagen blanco y negro: ", grices)
# cv2.imshow("este es el umbral: ", umbral)
cv2.waitKey(0)
cv2.destroyAllWindows()


