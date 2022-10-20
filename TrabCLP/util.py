from interface import Ui_MainWindow
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from ctypes import *

libMandelbrot = CDLL("./mandelbrot_func.so")

def MandelbrotExe(a, b, c, d, e, f):
    libMandelbrot.mandelbrot(a, b, c, d, e, f)

MandelbrotExe(0, 0, 0, 255, 255, 255)