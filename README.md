# EmbebidosP3
App Inicializacion se encarga de la inicializacion de la aplicacion de reconocimiento atravez de una conexion SSH y la copia de los datos resultantes del analisis de letras. La aplicacion se ejecuta en el cmd.

Los archivos de jupyter notebook (extension ipynb) fueron codigos de prueba para los modulos de extraccion y prediccion de letras, correspondientes a Edicion_img para la extraccion de imagenes y Letras para la prediccion. 

ConversionTF-Lite: realiza una conversion de una red neuronal ya entrenada con tensorflow para que utilice tensorflow-lite. Para esto se utiliza el model.h5 extraido de la red neuronal de reconocimiento de emociones ya entrenada utilizando la base de datos emnist para letras escritas, se vuelve a armar la red neuronal con los pesos del modelo y se utilizan las funciones de conversion TF-lite para generar el modelo convertido converted_model.tflite.

App Reconocimiento: Esta aplicacion se encarga de utilizar el modelo pre entrenado y convertido a tflite converted_model.tflite, junto al modulo de vision por computador OpenCV para reconocer letras escritas a mano atravez de una camara web y escribirlas en un archivo de texto Letras.txt.

El folder de recetas incluye las recetas generadas para la creacion de la imagen minimal incluyendo las recetas de meta-appreconocimiento, para incluir el appreconocimiento, converted_model y el localconf y bblayers general de la imagen que incluye los modulos a instalar en la imagen y los metas de donde buscar esos modulos.
