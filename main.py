import functions
from gui import gui
gui.setCallbacks(functions.fn1, functions.fn2, functions.fn3, functions.fn4, functions.fn5)
gui.setListbox(functions.tables(), showTable)
gui.show()