import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st

from webScrap import *


class   Tarea4:
    
    def __init__(self):
        # self.abrir()
        self.ventana1=tk.Tk()
        self.ventana1.title("TAREA 3")
        self.ventana1.resizable(False, False)

        self.cuaderno1 = ttk.Notebook(self.ventana1) 
        self.consulta_por_codigo()
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()


    def consulta_por_codigo(self):
        #datos cuaderno
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Boleta de honorarios")
        #Datos pagina
        self.labelframe2=ttk.LabelFrame(self.pagina1, text="Ingrese los datos solicitados")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        #datos label1 RUT
        self.label1=ttk.Label(self.labelframe2, text="Rut:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.rut=tk.StringVar()
        #dato entrada RUT
        self.entryRut=ttk.Entry(self.labelframe2, textvariable=self.rut )
        self.entryRut.grid(column=1, row=0, padx=4, pady=4)
        #dato label2 CLAVE
        self.label2=ttk.Label(self.labelframe2, text="Clave Tributaria:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.clave=tk.StringVar()
        #dato entrada CLAVE
        self.entryClave=ttk.Entry(self.labelframe2, textvariable=self.clave)
        self.entryClave.grid(column=1, row=1, padx=4, pady=4)
        #datos label3 AGE
        self.label3=ttk.Label(self.labelframe2, text="Año de Consulta:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.age=tk.StringVar()
        #dato entrada AGE
        self.entryAge=ttk.Entry(self.labelframe2, textvariable=self.age)
        self.entryAge.grid(column=1, row=2, padx=4, pady=4)
        #Boton iniciar proceso
        self.boton1=ttk.Button(self.labelframe2, text="Iniciar Proceso", command=self.iniciarProceso)
        self.boton1.grid(column=0, row=3, padx=4, pady=4)
        #Boton limpiar
        self.boton2=ttk.Button(self.labelframe2, text="Limpiar Datos", command=self.limpiar)
        self.boton2.grid(column=1, row=3, padx=4, pady=4)


    def iniciarProceso(self):
        datoRut=self.rut.get()
        datoClave=self.clave.get()
        datoAge=self.age.get()

        if (len(datoRut)>7):
            print("Rut ingresado correctamente")
            if (len(datoClave)>0):
                print("Clave ingresada correctamente")
                if (len(datoAge)>3):
                    print("Año ingresado correctamente")
                    webScrap(datoRut,datoClave,datoAge)
                    
                    self.entryRut.delete(0, 'end')
                    self.entryClave.delete(0, 'end')
                    self.entryAge.delete(0, 'end')

                    mb.showinfo("Información", "Proceso finalizado, favor revisar carpeta Temp")
                else:
                    mb.showinfo("Información", "El Año ingresado no es valido")
            else:
                mb.showinfo("Información", "La clave ingresada no es valida")
        else:
            mb.showinfo("Información", "El Rut ingresado no es valido")

    def limpiar(self):
        self.entryRut.delete(0, 'end')
        self.entryClave.delete(0, 'end')
        self.entryAge.delete(0, 'end')
    

aplicacion1=Tarea4()