from tools import *
from tkinter import *
from tkinter import ttk
from tkinter.font import *
from tkinter import messagebox

def iniciar(): #ABRE VENTANA HIJA PARA ASIGNARLE UN NOMBRE A LA SESION Y EJECUTA EL RUN()
    ventana_emergente = Toplevel(root)
    ventana_emergente.title("Ventana emergente")
    
    def obtener_texto():
        texto_ingresado = input_text.get()
        ventana_emergente.destroy()
        run(texto_ingresado)
    
    input_label = Label(ventana_emergente, text="Por favor, indique el nombre de la sesión:")
    input_label.pack(pady=10)
    
    input_text = Entry(ventana_emergente)
    input_text.pack(pady=5)
    
    ok_button = Button(ventana_emergente, text="OK", command=obtener_texto)
    ok_button.pack(pady=10)

def salir():
    root.destroy()

root = Tk()
root.title("Stake")
root.geometry("430x300")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

frame = Frame(root)
frame.grid(row=0, column=0, sticky="nsew")
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

instrucciones_texto = """Instrucciones:

- Abrir Chrome: ventana izquierda, pantalla completa
- Ir a página de stake // Casino // Crash // AUTO // HISTORIAL
- Abrir menú de dev (f12) ULTIMO
- Ubicar navegador y menú en 1410 x 1007 px
- DEJAR TODA LA VISTA HTML
- PRESIONA INICIAR"""

Label(frame, text=instrucciones_texto, justify="left").grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

Button(frame, text="Iniciar", command=iniciar).grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
Button(frame, text="Salir", command=salir).grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

frame.grid_rowconfigure(1, weight=1)
frame.grid_rowconfigure(2, weight=1)
frame.grid_columnconfigure(0, weight=1)

root.mainloop()