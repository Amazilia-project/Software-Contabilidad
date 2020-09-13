# -*- coding: utf-8 -*-
# Zona de librerias
from tkinter import ttk # Interfaz grafica
from tkinter import * # Todos los demas componentes
from tkinter import messagebox as Messagebox # Popups
import sqlite3 # Modulo de conexion

class Login:

	def limpiar_text(self):
		# Funcion para limpiar cajas de textox
		self.name.delete(0, 'end')
		self.pas.delete(0, 'end')
		self.name.focus()


	def informacion(self):
		self.infor_wind = Toplevel()	# Popup = Toplevel()
		self.infor_wind.title("Información Relevante")

		ttk.Button(self.infor_wind, text = "Salir", command = self.infor_wind.destroy).pack(padx=10, pady=10)
		
		self.infor_wind.transient(self.wind)	# Desabilitar el boton de minimizar infor_wind  
		self.infor_wind.grab_set()	# La interacción de la ventana principal "wind" es deshabilitada 
		self.wind.wait_window(self.infor_wind)	# Detener la ventana principal wind


	def __init__(self, window):
		# Funcion principal para inicializar
		self.wind = window
		self.wind.title("Amazilia Python")
		self.wind.resizable(0, 0)
		#self.wind.geometry ("390x264")
		#self.wind.iconbitmap('./image/.ico')

		# Centrar ventana
		window_width = 390
		window_height = 264

		screen_width = self.wind.winfo_screenwidth()	# winfo() es para obtener informacion de la ventana actual
		screen_height = self.wind.winfo_screenheight()	

		x_coordenada = int((screen_width/2) - (window_width/2))
		y_coordenada = int((screen_height/2) - (window_height/2))

		self.wind.geometry("{}x{}+{}+{}".format(window_width, window_height, x_coordenada, y_coordenada))


		# Contenedor 1 (Frame 1) de marcos
		frame = LabelFrame(self.wind, text = " Login (Autenticación) ", font = ("Time New Roman",12))
		frame.grid(row = 0, column = 0, columnspan = 3, padx=30, pady=20, ipady=5)

		# Entrada del nombre de usuario
		Label(frame, text = "Usuario        :", font = ("Helvetica",12)).grid(row = 1, column = 0, sticky="w", pady = 7)
		self.name = Entry(frame, font = ("Helvetica",12))
		self.name.focus() # Para centrar el selecionador
		self.name.grid(row = 1, column = 1)

		# Entrada de la contraseña
		Label(frame, text = "Contraseña :", font = ("Helvetica",12)).grid(row = 2, column = 0, sticky="w", pady = 7)
		self.pas = Entry(frame, font = ("Helvetica",12))
		self.pas.grid(row = 2, column = 1)
		self.pas.config(show = "*")


		# Estilo de botones
		style = ttk.Style() 
		style.configure('TButton', font = ("Helvetica", 12))
		#style.configure('TButton', width=10) # Tamaño del boton

		# Boton de ingresar
		ttk.Button(frame, text = "Ingresar", styl = 'TButton').grid(row = 3, column = 1)



		# Contenedor 2 (Frame2) de marcos
		frame2 = LabelFrame(self.wind, text = " Operaciones ", font = ("Time New Roman",12))
		frame2.grid(row = 4, column = 0, columnspan = 3, padx = 15, ipady = 3)

		# Botones de operaciones
		ttk.Button(frame2, text = "Información",style = 'TButton', command = self.informacion).grid(row = 5, column = 1, pady=5, padx = 5)
		ttk.Button(frame2, text = "Reset",style = 'TButton', command = self.limpiar_text).grid(row = 5, column = 2, pady = 5, padx = 5)
		ttk.Button(frame2, text = "Exit",style = 'TButton', command = self.wind.quit).grid(row = 5, column = 3, pady = 5, padx = 5)

		# Espacio en blanco
		self.espacio = Label(text = "")
		self.espacio.grid(row = 6, column = 0, columnspan = 2, sticky = W + E)



# Configuración de la raíz
if __name__ == '__main__':
    window = Tk()
    application = Login(window)
    window.mainloop()