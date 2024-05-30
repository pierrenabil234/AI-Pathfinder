from PyQt5 import QtCore, QtGui, QtWidgets
import networkx as nx
from PyQt5.QtCore import Qt
import sys
import random
import numpy as np
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QPainter, QPolygon, QVector2D
import matrix_graph
import bfs
import dfs
import AStar
import AStar_euclidean_distance
import AStar_manhattan_distance
import greedy_manhattan_distance
import greedy_euclidean_distance
class Main2(QtWidgets.QMainWindow):
    
    def __init__(Window):
        super().__init__()
        Window.matrix_size=0
        Window.cell_size=0
        Window.rnd_cell_size=0
        Window.cell_numbers=0
        Window.rectangles = []
        Window.rnd_rect=[]
        Window.AllMatrix=[]
        Window.input=QtWidgets.QLineEdit(Window)
        Window.buttomMatSize=QtWidgets.QPushButton('Draw', Window)
        Window.input.move((Window.width()//2) +180,1)
        Window.buttomMatSize.move((Window.width()//2) +180,31)
        Window.buttomMatSize.clicked.connect(Window.Mat)
        #Window.exisit_rect=QtCore.QRect(0,0,0,0)
        Window.exisit_rect=[]
        Window.matrix=[]
        Window.start=QtCore.QRect(0,0,0,0)
        Window.End=[]
        Window.right_click=False
        Window.S_key=False
        Window.E_key=False
        Window.D_key=False
        Window.rnd_matrix=[]
        Window.rnd_start=[]
        Window.rnd_end=[]
        Window.rnd_walls=[]
        Window.start_node=(-1,-1)
        Window.end_node=[]
        Window.visited_path=[]
        Window.optimal_path=[]
        Window.visited_and_shown=[]
        Window.show_optimal=[]
        Window.vis=[]
        Window.add_x=0
        #window.heur_matrix=[]
        Window.ct=0
        Window.timer = QtCore.QTimer(Window)
        Window.path_rec=0
        Window.timer.timeout.connect(Window.timer_callback)
        Window.animation_index=1
        Window.initUI()
        #initalize all variables + widgets
        Window.istart=-1
        Window.jstart=-1
        
    def initUI(Window):
        Window.resize(900, 900)
        Window.move(600, 50)
        Window.setWindowTitle("Maze")
        Window.combo = QtWidgets.QComboBox(Window)
        Window.combo.addItem("BFS")
        Window.combo.addItem("DFS")
        Window.combo.addItem("A*_manhattan")
        Window.combo.addItem("A*_euclidean")
        Window.combo.addItem("greedy_manhattan")
        Window.combo.addItem("greedy_euclidean")
        Window.Searchbutton = QtWidgets.QPushButton("Run Search", Window)
        Window.Searchbutton.clicked.connect(Window.run_search)
        Window.Searchbutton.move((Window.width()//2) +300, 31)
        Window.combo.move((Window.width()//2) +300, 1)
        # Window.drawButton = QtWidgets.QPushButton('Generate', Window)
        # Window.drawButton.move((Window.width()//2) +200, 25)
        # Window.endButton.clicked.connect(Window.generate_random)
        Window.endButton = QtWidgets.QPushButton('end', Window)
        Window.endButton.move((Window.width()//2) +179, 31)
        Window.endButton.clicked.connect(Window.end_and_send)
        Window.drawButton = QtWidgets.QPushButton('Generate', Window)
        Window.drawButton.move((Window.width()//2) +179, 1)
        Window.drawButton.clicked.connect(Window.generate_random)
        #create buttons

    def end_and_send(Window):
        #Window.rnd_cell_size=Window.cell_size
        if Window.istart == -1 and Window.jstart == -1 and not Window.End:
            msgBox = QMessageBox()
            msgBox.setText('no start node and any end nodes')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.exec_()
        elif Window.istart == -1 and Window.jstart == -1:
            msgBox = QMessageBox()
            msgBox.setText('no start node ')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.exec_()
        elif not Window.End:
            msgBox = QMessageBox()
            msgBox.setText('no any end nodes')
            msgBox.setIcon(QMessageBox.Information)
            msgBox.exec_()
            

        else:
            Window.G,Window.start_node,Window.end_node=matrix_graph.matrix(Window.matrix)
            Window.G,Window.start_node,Window.end_node=matrix_graph.matrix(Window.AllMatrix)
        #heur

    def run_search(Window):
        Window.visited_and_shown=[]
        Window.vis=[]
        Window.animation_index=1
        Window.optimal_path=[]
        Window.visited_path=[]
        Window.show_optimal=[]
        if(Window.combo.currentText()=="BFS"):
            Window.optimal_path,Window.visited_path= bfs.BFS(Window.G,Window.start_node,Window.end_node)
            #print(f"Visted path={Window.visited_path}")
        
        elif(Window.combo.currentText()=="DFS"):
            Window.visited_path,Window.optimal_path = dfs.DFS(Window.G,Window.start_node,Window.end_node)
            print(f"Path={Window.optimal_path} ")
            
        elif(Window.combo.currentText()=="greedy_manhattan"):
            Window.optimal_path,Window.visited_path=greedy_manhattan_distance.greedy_manhattan(Window.AllMatrix,Window.G,Window.start_node,Window.end_node)
                        
        elif(Window.combo.currentText()=="greedy_euclidean"):
            Window.optimal_path,Window.visited_path=greedy_euclidean_distance.greedy_euclidean(Window.AllMatrix,Window.G,Window.start_node,Window.end_node)
             
        elif(Window.combo.currentText()=="A*_manhattan"):
            Window.optimal_path,Window.visited_path=AStar_manhattan_distance.Astar_manhattan(Window.AllMatrix,Window.G,Window.start_node,Window.end_node)
            #print("Solve using A* Algorithm by Manhattan")
                        
        elif(Window.combo.currentText()=="A*_euclidean"):
            Window.optimal_path,Window.visited_path=AStar_euclidean_distance.Astar_euclidean(Window.AllMatrix,Window.G,Window.start_node,Window.end_node)

            #print("Solve using A* Algorithm by euclidean")
             
        



    def Mat(window):
       if window.input.text !=" ":
        window.matrix_size=int(window.input.text())
        if window.matrix_size>0:
            window.cell_numbers=window.matrix_size
            n=int(window.matrix_size)
            window.rnd_matrix=[]
            window.AllMatrix=[]
            window.rnd_start=[]
            window.rnd_end=[]
            window.rnd_walls=[]
            window.rnd_rect=[]
            window.rectangles=[]#empty the rectangles list
            window.start=QtCore.QRect(0,0,0,0)#empty the start-nodes var
            window.End=[]#empty the end-nodes list
            window.drawRandomMatrix()#call the draw function for manuall drawing
            window.matrix=np.zeros((n,n))#create a matrix of size n*n full of zeros lib used is numpy 
            window.AllMatrix=np.zeros((n,n))
            #window.heur_matrix=np.zeros((n,n))
        #print(window.matrix)
       
    def generate_random(Window):
        Window.rnd_rect=[]
        Window.rnd_start=[]
        Window.rnd_end=[]
        Window.rnd_walls=[]
        Window.rnd_matrix=[]
        Window.AllMatrix=[]
        Window.rectangles=[]
        Window.exisit_rect=[]
        Window.End=[]
        Window.visited_and_shown=[]
        Window.vis=[]
        Window.animation_index=1
        Window.optimal_path=[]
        Window.visited_path=[]
        Window.show_optimal=[]
        Window.ct=0
        Window.add_x=55
        Window.start=QtCore.QRect(0,0,0,0)
        #empty all lists so that when button is clicked again it does not draw on top of each other
        n=random.randint(5,50)#random size of matrix/grid/maze
        Window.rnd_matrix=np.zeros((n,n))#create a matrix of size n*n full of zeros lib used is numpy 
        #window.heur_matrix=np.zeros((n,n))
        Window.AllMatrix=np.zeros((n,n))
        Window.rnd_cell_size=(Window.width() -55)//(n) #so that all cells are shown...work in progress
        x=random.randint(1,n-1)#random x axis for start node
        y=random.randint(1,n-1)#random y axis for start node
        Window.rnd_matrix[x][y]=2#place the start node as 2 in the matrix as sown in maze
        Window.AllMatrix[x][y]=2
        x*=Window.rnd_cell_size#multiply the x by cell size so the start node is drawn is in place
        y=y * Window.rnd_cell_size + 55#multiply the y by cell size so the start node is drawn is in place
        Window.rnd_start.append((x,y,Window.rnd_cell_size,Window.rnd_cell_size))#append all elemts in start_node list
        #print(f"rnd_start={Window.rnd_start}")
        num_of_end=random.randint(1,n)#number of goal nodes from 1 to n
        for i in range(0,num_of_end):
            x=random.randint(0,n-1)
            y=random.randint(0,n-1)
            if Window.rnd_matrix[x][y]==0:#it will add the goal nodes to any other cell that has not been changed
                Window.rnd_matrix[x][y]=3
                Window.AllMatrix[x][y]=3

                x*=Window.rnd_cell_size
                y= y * Window.rnd_cell_size + 55
                Window.rnd_end.append((x,y,Window.rnd_cell_size,Window.rnd_cell_size))
                #place the goal nodes in the matrix as 3
        for i in range(0,n):
            for j in range(0,n):
                x=i*Window.rnd_cell_size
                y=j*Window.rnd_cell_size+55
                z=random.randint(0,1)
                rect=QtCore.QRect(x,y,Window.rnd_cell_size,Window.rnd_cell_size)
                Window.rnd_rect.append(rect)
                if z==1 and Window.rnd_matrix[i][j]==0:
                    Window.rnd_walls.append((x,y,Window.rnd_cell_size,Window.rnd_cell_size))
                    Window.rnd_matrix[i][j]=1
                    Window.AllMatrix[i][j]=1
        #create the grid and draw the random walls as well as placing them in the matrix as 1
        Window.rnd_matrix=Window.rnd_matrix.transpose()
        Window.AllMatrix=Window.AllMatrix.transpose()
        #idk why but the matrix was reversed(columns became rows and vice versa so we used this function to fix it)
        #this bug only appeared in the rnd_matrix
        #Window.G,Window.start_node,Window.end_node=Martrix_to_graph.matrix_to_graph(Window.rnd_matrix)
        Window.G,Window.start_node,Window.end_node=matrix_graph.matrix(Window.rnd_matrix)
        Window.G,Window.start_node,Window.end_node=matrix_graph.matrix(Window.AllMatrix)

        
        
        #heur

        Window.repaint()
        #print(Window.rnd_matrix)
        Window.update()
        #calls paint function to draw updates

    def drawRandomMatrix(Window):
        Window.visited_and_shown=[]
        Window.vis=[]
        Window.animation_index=1
        Window.optimal_path=[]
        Window.visited_path=[]
        Window.show_optimal=[]
        Window.cell_size = (Window.width()-55) //  (Window.matrix_size)
        Window.rnd_cell_size=(Window.width()-55) //  (Window.matrix_size)
        Window.add_x=55
        Window.exisit_rect=[]
        for i in range(0, Window.matrix_size):
            for j in range(0, Window.matrix_size):
                x = i * Window.cell_size
                y = j * Window.cell_size+55

                rect = QtCore.QRect(x, y, Window.cell_size, Window.cell_size)
                Window.rectangles.append(rect)
        Window.update()
        #print(Window.rnd_matrix)
        Window.matrix_size=0
        #creates the maze with size n=Window.matrix size
        #NOTE Window. is the same as this. in c#
    
    def mousePressEvent(Window, event):
        x, y, i, j = 0, 55, 0, 0
        if event.button() == Qt.LeftButton:
            for i in range(0, Window.cell_numbers):
                x = 0
                for j in range(0, Window.cell_numbers):
                    if event.x() >= x and event.x() < x + Window.cell_size and event.y() >= y and event.y() < y + Window.cell_size:
                        if Window.S_key==True:
                            
                            if Window.istart>=0 and Window.jstart>=0:
                                Window.matrix[Window.istart][Window.jstart]=0
                                Window.AllMatrix[Window.istart][Window.jstart]=0
                                
                            Window.start=(x,y,Window.cell_size,Window.cell_size)
                            Window.S_key=False
                            Window.matrix[i][j]=2
                            Window.AllMatrix[i][j]=2
                            Window.istart=i
                            Window.jstart=j
                            Window.repaint()
                           
                        elif Window.E_key==True:
                            if len(Window.End)<Window.cell_numbers:
                                Window.End.append((x,y,Window.cell_size,Window.cell_size))
                                Window.matrix[i][j]=3
                                Window.AllMatrix[i][j]=3
                                Window.repaint()
                            Window.E_key=False
                        
                        elif Window.D_key==True:
                            if Window.matrix[i][j] == 3:
                                for end in Window.End:
                                    X,Y,C_S,CS=end
                                    #if x >= X and x <= X + CS and y >= Y and y <= Y + CS:
                                    if X==x and Y==y:
                                        print("OK")
                                        Window.End.remove(end)
                                        break
                                    else:
                                        print("No")
                                Window.matrix[i][j] = 0
                                Window.AllMatrix[i][j] = 0
                                Window.repaint()
                                print(Window.matrix)
                            elif Window.matrix[i][j]==1:
                                for Wall in Window.exisit_rect:
                                    X,Y,C_S,CS=Wall
                                    #if x >= X and x <= X + CS and y >= Y and y <= Y + CS:
                                    if X==x and Y==y:
                                        print("OK")
                                        Window.exisit_rect.remove(Wall)
                                        break
                                    else:
                                        print("No")
                                Window.matrix[i][j] = 0
                                Window.AllMatrix[i][j] = 0
                                Window.repaint()
                                print(Window.matrix)
                            Window.D_key = False

                           

                        elif Window.E_key==False and Window.S_key==False and Window.D_key==False and Window.matrix[i][j]==0:
                            Window.exisit_rect.append((x,y,Window.cell_size,Window.cell_size))
                            #paint.fillRect(Window.exisit_rect,Qt.black)
                            Window.matrix[i][j]=1
                            Window.AllMatrix[i][j]=1
                            #print(Window.matrix)
                            Window.repaint()
                    x += Window.cell_size
                y += Window.cell_size
        
            #This code is the same as the tiles code in multimedia
            #The only addition is that it places 1,2,3 as walls,start and goal in the maze
            #To draw wall just left click
            #To draw start node (only one) press the 'S' button once then left click
            #To draw end node/goal node (n amount same as dimensions of maze) click 'E' button once then left click
               
    def keyPressEvent(Window, event):
        if event.key() == Qt.Key_S:
            Window.S_key=True
        if event.key()== Qt.Key_E:
            Window.E_key=True
        if event.key()== Qt.Key_D:
            Window.D_key=True
     #To signal 'S' and/or 'E' have been pressed

    def KeyReleaseEvent(Window,event):
        if event.key() == Qt.Key_S:
            Window.S_key=False
        if event.key()== Qt.Key_E:
            Window.E_key=False
        if event.key()== Qt.Key_D:
            Window.D_key=False
        #To signal that 'S' and/or 'E' are no longer being pressed
          

    def paintEvent(Window, event):
        painter = QtGui.QPainter(Window)
        if  len(Window.visited_and_shown)==1 and len(Window.optimal_path)>0:
            if Window.ct>1:
                for rec in Window.optimal_path[1:]:
                    x,y=rec[0],rec[1]
                    Window.show_optimal.append((y*Window.rnd_cell_size,x*Window.rnd_cell_size+Window.add_x,Window.rnd_cell_size,Window.rnd_cell_size))
                    for x in Window.show_optimal:
                        painter.fillRect(QtCore.QRect(*x),Qt.red)
                    
            Window.ct+=1
          
            
            
        for rect in Window.rectangles:
            painter.drawRect(rect)
            # To draw grid/maze(user drawn)

        for rect in Window.rnd_rect:
            painter.drawRect(rect)
            # To draw grid/maze(pc generated)

        for rect in Window.exisit_rect:
            painter.fillRect(QtCore.QRect(*rect),Qt.black)
            # To draw walls(user drawn)

        if Window.start:
            painter.fillRect(QtCore.QRect(*Window.start),Qt.yellow)
            # To draw goal(user drawn)

        for rect in Window.End:
            painter.fillRect(QtCore.QRect(*rect),Qt.blue)
            # To draw end(user drawn)

        for rect in Window.rnd_walls:
            painter.fillRect(QtCore.QRect(*rect),Qt.black)
            # To draw walls(pc generated)

        for rect in Window.rnd_end:
            painter.fillRect(QtCore.QRect(*rect),Qt.blue)
            # To draw goal(pc generated)

        for rect in Window.rnd_start:
            painter.fillRect(QtCore.QRect(*rect),Qt.yellow)
            # To draw start(pc generated)

        for rec in Window.visited_and_shown[1:]:
            x,y,w,h=rec[0],rec[1],rec[2],rec[3]
            Window.vis.append((x*w,y*h+Window.add_x,Window.rnd_cell_size,Window.rnd_cell_size))
            Window.visited_and_shown.pop(0)
            for x in Window.vis:
                painter.fillRect(QtCore.QRect(*x),Qt.gray)
                if len(Window.vis)==0:
                    print(f"vis optimsl ")

        if Window.visited_path and Window.animation_index < len(Window.visited_path) - 1:
            if Window.animation_index+1==len(Window.visited_path)-1:
                print(Window.optimal_path)
            Window.timer.start(100)
            x, y = Window.visited_path[Window.animation_index]
            rect = QtCore.QRect(y * Window.rnd_cell_size, x * Window.rnd_cell_size+Window.add_x, Window.rnd_cell_size, Window.rnd_cell_size)
            Window.visited_and_shown.append((y,x,Window.rnd_cell_size,Window.rnd_cell_size))
            if len(Window.visited_and_shown)==0:
                print("op")
            painter.fillRect(rect, Qt.red)

    def timer_callback(Window):
            Window.animation_index += 1
            Window.update()


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    Mazemain = Main2()
    Mazemain.show()
    
    sys.exit(app.exec_())
    #To start/end app
