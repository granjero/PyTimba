import cv2
import numpy as np
import time
from espeak import espeak as es


#toma una imagen de la webcam 
cam = cv2.VideoCapture(1)
ret, imagen = cam.read()
cv2.imshow("m",imagen)
cam.release()

"""
#lee una imagen
imagen = cv2.imread('webcam.jpg')
"""

#hace una copia de la imagen en copia
copia = imagen.copy()
#copia = imagen[:800,:800,:] #esta linea viene de test.py

#saca la media de la imagen para sacar el thereshold minimo para la funcion Canny
teresjold = cv2.mean(copia)

teresjoldMin = teresjold[1] - teresjold[1] * 0.1


#pasa a blanco y negro la imagen q
#grises = cv2.cvtColor(copia, cv2.COLOR_BGR2GRAY)


#blurea la imagen para que los bordes sean mas redondos
#blureado = cv2.medianBlur(copia,5)
blureado = cv2.blur(copia, (5,5))

#saca los bordes de la imagen
edges = cv2.Canny(blureado, teresjoldMin, 200)


#pasa a dos bits la imagen de grises
#ret, dosbit = cv2.threshold(copia,150,255,cv2.THRESH_BINARY)
#blureado = cv2.blur(dosbit, (15,15))


#usa la imagen de dos bit para encontrar circulos
#circulos = cv2.HoughCircles(dosbit, cv2.cv.CV_HOUGH_GRADIENT, 10, 300) #no anda

circulos = cv2.HoughCircles(
				edges
				,cv2.cv.CV_HOUGH_GRADIENT
				,1
				,30
				,param1      = 255
				,param2      = 15
				,minRadius   = 10
				,maxRadius   = 50
				)


#si encuentra circulos les hace un centro naranja y dibuja el perimetro
if circulos is not None:
    # convert the (x, y) coordinates and radius of the circles to integers
	circulos = np.round(circulos[0, :]).astype("int")

    # loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circulos:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(copia, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(copia, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
		
if circulos is not None:
	print(len(circulos))

es.set_voice("es-la")
es.synth("La suma de la cara de los dados es: ")
es.synth(str(len(circulos)))
while es.is_playing():
	pass

"""	
engine = pyttsx.init()
engine.say(len(circulos))
engine.runAndWait()	
"""

	

#escribe los archivos jpg
cv2.imwrite('orignal.jpg', imagen)
cv2.imwrite('bordes.jpg', edges)
cv2.imwrite('circulos.jpg', copia)
cv2.imwrite('blur.jpg', blureado)

