import re
import csv
import pyautogui
import time as ti
from tkinter import messagebox
import pyperclip as clipboard

listaLimpia=[[],[]]

def ubicaFoco(): #ENFOCA EN VENTANA
    
    pyautogui.moveTo(1670,10)
    pyautogui.click()
    
def ubicaTablaEnDev(): #BUSCA EL ELEMENTO HTML QUE CONTENDRA LAS TABLAS A COPIAR
    
    with pyautogui.hold('ctrl'):
        pyautogui.press('f')
    pyautogui.write("svelte-1y89ow9")
    pyautogui.press('enter')

def obtieneTabla(): #MANIPULA MOUSE Y TECLADO DE PARA ALMACENAR EN PORTAPAPELES EL ELEMENTO HTML
    pyautogui.moveTo(1740,940)
    pyautogui.rightClick()
    with pyautogui.hold('ctrl'):
        pyautogui.press('f')
    ti.sleep(1)
    for i in range(7):
        pyautogui.press('down')
        ti.sleep(0.2)
    ti.sleep(1)
    pyautogui.press('right')
    pyautogui.press('down')
    pyautogui.press('enter')

def pagSiguiente(): #PASO A SIGUIENTE PAGINA EN EL CUADRO DE TABLAS
    pyautogui.moveTo(770,870)
    pyautogui.click()

def limpiaTexto(texto): #LIMPIA EL ELEMENTO HTML PARA QUEDARSE SOLO CON LA INFORMACION NECESARIA
    for i in range(10):
        patron = r'(.{2}):(.{12})'
        coincidencias = re.search(patron, texto)

        if coincidencias:
            resultado = coincidencias.group()
            listaLimpia[0].append(resultado)
            texto=texto[texto.find(resultado):]
        
        patron2 = r'(.{3}),(.{2})'
        coincidencias = re.search(patron2, texto)
        
        if coincidencias:
            resultado = coincidencias.group()
            listaLimpia[1].append(resultado)
            texto=texto[texto.find(resultado):]

def exportaTabla(lista,nombre): #EXPORTA TABLA CON EL NOMBRE QUE SE INDICARA EN EL INPUT DE LA VENTANA PRINCIPAL
    ruta_archivo="TABLAS/"+str(nombre)+".csv"
    tablaTranspuesta=zip(*lista)

    with open(ruta_archivo,"w",newline="") as archivo_csv:
        escritor_csv=csv.writer(archivo_csv)
        #escritor_csv.writerows(['Hora y Fecha'],['Jugada'])
 
        escritor_csv.writerows(tablaTranspuesta)

def limpiaCaracteres(nombre): #TERMINA DE TRANSFORMAR LA INFORMACION DEL ARCHIVO RECIENTEMENTE CREADO PARA SU POSTERIOR ANALISIS

    ruta_archivo="TABLAS/"+str(nombre)+".csv"
    with open(ruta_archivo, 'r') as archivo_csv:
        datos = list(csv.reader(archivo_csv))

        # Modificar los datos de la segunda columna
        for fila in datos:
            edad = fila[1]
            edad = edad.replace('"', '')  # Eliminar el caracter '%'
            edad = edad.replace('>', '')  # Eliminar el caracter ','
            fila[1] = edad

    # Guardar los cambios en el archivo CSV
    with open(ruta_archivo, 'w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(datos)

def run(nombre): #SECUENCIA DE RUTINA COMPLETA
    try:
        ubicaFoco()
        ubicaTablaEnDev()
        obtieneTabla()
        limpiaTexto(str(clipboard.paste()))
        if messagebox.askokcancel("Stake","Si ha funcionado todo correcto presiona enter, de lo contrario presiona cancelar, ubica los elementos, e inicia nuevamente"):
            pagSiguiente()
            ti.sleep(1)
            pass
        else:
            return

        for i in range(100):
            obtieneTabla()
            limpiaTexto(str(clipboard.paste()))
            pagSiguiente()
            ti.sleep(1)
    except:
        pass
    exportaTabla(listaLimpia,nombre)
    limpiaCaracteres(nombre)


