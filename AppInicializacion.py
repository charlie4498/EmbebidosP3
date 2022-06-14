import pyttsx3
import subprocess
import tkinter as tk
import time
import sys 


def Iniciar():

    subprocess.run('ssh root@192.168.2.25 python3 /usr/bin/appreconocimiento', shell=True)

    time.sleep(10) 
    
    subprocess.run('scp root@192.168.2.25:/usr/bin/Letras.txt /Users/ejcs2/Desktop', shell=True)

def Escuchar():
    s = pyttsx3.init()  
    data1 = open ('Letras.txt','r')
    data = data1.read()
    s.say(data)  
    s.runAndWait()

def Salir():
    window.destroy()
    sys.exit("Terminado")

window = tk.Tk()
window.geometry('400x153')
mensaje = tk.Label(text="Aplicación de reconocimiento de letras")
mensaje.pack()

boton = tk.Button(text="Iniciar la aplicación", command = Iniciar)
boton.place(x=145, y=30)

boton2 = tk.Button(text="Escuchar", command = Escuchar)
boton2.place(x=170, y=70)

boton3 = tk.Button(text= "Salir", command = Salir)
boton3.place(x=180, y=110)

window.mainloop()
