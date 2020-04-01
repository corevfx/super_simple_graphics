# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:05:09 2020

@author: Kevin Ma
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

color = QtWidgets.QColorDialog.getColor()
print("The chosen color is r:"+str(color.red())+", g:"+str(color.green())+", b:"+str(color.blue()))


sys.exit(app.exec_())