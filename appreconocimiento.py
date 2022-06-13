import sys
import numpy as np
import cv2 as cv
import tflite_runtime.interpreter as tflite

def obtenerLetras(imagen):
    col = 0
    i = 0
    lista = []
    for i in range(11):
        letra = imagen[4:90 , col+3:col+40]
        lista.append(letra)
        col+=42
    return lista

def preproc(imagen):
    imagegray = cv.cvtColor(  imagen, cv.COLOR_BGR2GRAY)
    (thresh, imagebw) = cv.threshold(imagegray, 127, 255, cv.THRESH_BINARY)
    imageN= cv.resize(cv.subtract(255, imagebw), (28,28), interpolation = cv.INTER_LINEAR)/255
    imageN= np.array(imageN, dtype= np.float32)
    imageproc=imageN.reshape(1,28,28,1)
    return imageproc

def predictlist (list1, list2, label):
    for i in list1:
        imageproc= preproc(i)
        interpreter.set_tensor(input_details[0]['index'], imageproc)
        interpreter.invoke()
        predicted1 = interpreter.get_tensor(output_details[0]['index'])
        predicted=np.argmax(predicted1)
        list2.append(label[predicted-1])
    return list2


#Toma de fotos
camera = cv.VideoCapture(0)
return_value, image = camera.read()
cv.imwrite('opencv.png', image)
del(camera)


image = image[132:385 , 5:470]

Nombre = image[2:42 , 0:465]
listaNombre = obtenerLetras(Nombre)

Apellido1 = image[107:145 , 0:465]
listaApellido1 = obtenerLetras(Apellido1)

Apellido2 = image[212:247 , 2:465]
listaApellido2 = obtenerLetras(Apellido2)

f= open('Letras.txt', 'r+')
f.truncate(0)
f.close

predictNombre=[]
predictApellido1=[]
predictApellido2=[]

#Cargar modelo
interpreter=tflite.Interpreter(model_path="/usr/bin/converted_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

#Definir labels
label=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

predictlist(listaNombre, predictNombre, label)
predictlist(listaApellido1, predictApellido1, label)
predictlist(listaApellido2, predictApellido2, label)

open('Letras.txt','a').write('\n \n' + 'Nombre:' + '\n')
for i in predictNombre:
    open('Letras.txt','a').write(i)
open('Letras.txt','a').write('\n \n' + 'Apellido1:' + '\n')
for i in predictApellido1:
    open('Letras.txt','a').write(i)
open('Letras.txt','a').write('\n \n' +'Apellido2:' + '\n')
for i in predictApellido2:
    open('Letras.txt','a').write(i)

print( predictNombre, predictApellido1,predictApellido2)  

