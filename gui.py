from tkinter import *
from tkinter import ttk, END
import tkinter as tk
import pandas
from db import db
class GUI:
	def __init__(self):
		self.root = Tk()
		self.frm = ttk.Frame(self.root, padding=10)
		self.frm.grid()
	def setCallbacks(self, callback0, callback1, callback2, callback3, callback4, callback5):
		btn = ttk.Button(self.frm, text="Producto más vendido", command=callback0)
		btn.grid(column=0, row=0, padx=10)

		btn = ttk.Button(self.frm, text="Pedidos 3 meses", command=callback1)
		btn.grid(column=0, row=1, padx=10)

		btn = ttk.Button(self.frm, text="Clientes que han comprado el más vendido", command=callback2)
		btn.grid(column=0, row=2, padx=30)

		btn = ttk.Button(self.frm, text="Empleados con más ventas", command=callback3)
		btn.grid(column=0, row=3, padx=10)

		btn = ttk.Button(self.frm, text="Productos y clientes frecuentes", command=callback4)
		btn.grid(column=0, row=4, padx=10)
		
		btn = ttk.Button(self.frm, text = "Limpiar", command =callback5)
		btn.grid(column=0, row=5, padx=10)

	def setListbox(self):
		self.listbox = tk.Listbox(self.frm, height=15, width=40)
		ttk.Label(self.frm, text="").grid(column=3, row=0)
		self.listbox.grid(column=0, row=20)
	def show(self):
		self.root.mainloop()
	def limpiar(self):
		self.listbox.delete(0,self.listbox.size())
gui = GUI()