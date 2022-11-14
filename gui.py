from tkinter import *
from tkinter import ttk
import db
class GUI:
	def __init__(self):
		self.root = Tk()
		self.frm = ttk.Frame(root, padding=10)
		self.frm.grid(self)
	def setCallbacks(callback0, callback1, callback2, callback3, callback4):
		btn = ttk.Button(self.frm, text="Producto más vendido", command=callback0)
		btn.grid(column=0, row=0, padx=10)

		btn = ttk.Button(self.frm, text="Pedidos 3 meses", command=callback1)
		btn.grid(column=0, row=1, padx=10)

		btn = ttk.Button(self.frm, text="Clientes que han comprado el más vendido", command=callback2)
		btn.grid(column=0, row=2, padx=10)

		btn = ttk.Button(self.frm, text="Empleados con más ventas", command=callback3)
		btn.grid(column=0, row=3, padx=10)

		btn = ttk.Button(self.frm, text="Productos y clientes frecuentes", command=callback4)
		btn.grid(column=0, row=4, padx=10)
	def setListbox(self, tables : list, showTable):
		self.var = StringVar()
		ttk.Combobox(frm, values=tables, textvariable=self.var).grid(column=1, row=0)
		btn = ttk.Button(self.frm, text="Mostrar tabla", command=showTable)
		btn.grid(column=1, row=1, padx=10)
		self.listbox = tk.Listbox(self.frm,100)