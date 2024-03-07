import cv2 as cv


capturarVideo = cv.VideoCapture(0)
if not capturarVideo.isOpened(): 
    print("No se encontro ninguna camara")
    exit

while True: 
    _,camara = capturarVideo.read()
    # grices = cv.cvtColor(camara,cv.COLOR_BGR2GRAY)
    # _,umbral = cv.threshold(grices, 110, 255, cv.THRESH_BINARY)
    # contornos, jerarquia = cv.findContours(umbral, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    
    # cv.drawContours(camara, contornos, -1 ,(112,48,174), 3)
    
    cv.imshow("En vivocamara", camara)
    # cv.imshow("camara gris", grices )
    # cv.imshow("camara gris", umbral )
    
    if cv.waitKey(1) == ord("q"):
        break

capturarVideo.release()
cv.destroyAllWindows