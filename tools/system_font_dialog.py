# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:16:29 2020

@author: Kevin Ma
"""

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

app = QtWidgets.QApplication(sys.argv)

font = QtWidgets.QFontDialog.getFont()


sys.exit(app.exec_())