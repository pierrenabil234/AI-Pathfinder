from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
from PyQt5.QtCore import Qt
import sys
import random
import numpy as np
import bfs
import time
def animate(Self,rec):
    painter=QtGui.QPainter(Self)
    if rec:
        print(f"rec={rec}")
        painter.fillRect(QtCore.QRect(*rec),Qt.red)
            # To draw goal(user drawn)