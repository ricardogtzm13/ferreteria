import pandas, sqlalchemy, matplotlib
from db import db
from gui import gui
def fn1():
	global db
	pass
def fn2():
	global db
	pass
def fn3():
	global db
	pass
def fn4():
	global db
	pass
def fn5():
	global db
	pass
def tables():
	global db
	df = db.execute("SHOW TABLES")
	return df['Tables_in_ferreteria'].tolist()
def showTable():
	global gui
	df = db.execute("SELECT * FROM {}".format(gui.var.get()))