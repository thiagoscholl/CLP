from interface import Ui_MainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from ctypes import *
#from util import *
import sys
import threading 
import time

#libMandelbrot = CDLL("./mandelbrot_func.so")

class Window(QMainWindow, Ui_MainWindow):
	def __init__(self):
		super().__init__()
		self.setupUi(self)
		#y = threading.Thread(target=MandelbrotExe(0, 255, 0, 0, 0, 255), args=(1,))
		#y.start()
		#time.sleep(2)  
		self.pushButton.clicked.connect(self.clickHandler)
		
		x = QPixmap()
		test = x.load("imgMandelbrot.ppm")

	def clickHandler(self):
		self.label.setPixmap(QPixmap("imgMandelbrot.ppm"))


app = QApplication(sys.argv)
window = Window()
#libMandelbrot.mandelbrot(0, 0, 0, 255, 255, 255)
window.show()
sys.exit(app.exec())
