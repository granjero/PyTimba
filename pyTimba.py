import cv2
import numpy as np

#lee la imagen
img = cv2.imread('C:\Python27\Scripts\PyTimba-master\webcam.jpg',0)

#hace una copia de la imagen
copia = img.copy()

#saca los bordes de la imagen con la funcion canny
edges = cv2.Canny(copia,100,200)

#muesta la imagen original y espera una tecla para seguir
cv2.imshow("m",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

#calcula la cantidad de circulos
circulos = cv2.HoughCircles(
    edges
    ,cv2.cv.CV_HOUGH_GRADIENT
    ,1
    ,40 #distancia minima entre  
    ,param1      = 255
    ,param2      = 15
    ,minRadius   = 10 #ajustar estos valores 
    ,maxRadius   = 40 #ajustar estos valores
    )

if circulos is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
    circulos = np.round(circulos[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
    for (x, y, r) in circulos:
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv2.circle(edges, (x, y), r, (255, 255, 255), 4)
        cv2.rectangle(edges, (x - 5, y - 5), (x + 5, y + 5), (255, 255, 255), -1)
			
if circulos is not None:
    print(len(circulos))

#muesta la imagen edges y espera una tecla para seguir
cv2.imshow("m",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
