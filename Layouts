#PyQt5 layouts
import sys #it is a module 
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QWidget,QVBoxLayout,QGridLayout)
from PyQt5.QtGui import QIcon #GUI uses for inner functions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my cool first GUI")
        self.setGeometry(700,250,500,500)
        self.setWindowIcon(QIcon("HD-B.jpg"))
        self.initUI()
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        label1 = QLabel("#1",self)
        label2 = QLabel("#2",self)
        label3 = QLabel("#3",self)
        label4 = QLabel("#4",self)
        label5 = QLabel("#5",self)
        label1.setStyleSheet("background-color : blue;")
        label2.setStyleSheet("background-color : red;")
        label3.setStyleSheet("background-color : yellow;")
        label4.setStyleSheet("background-color : green;")
        label5.setStyleSheet("background-color : orange;")
        
       # vbox = QVBoxLayout()
       # vbox.addWidget(label1)
       # vbox.addWidget(label2)
       # vbox.addWidget(label3)
       # vbox.addWidget(label5)
        
      #  central_widget.setLayout(vbox)
        
        grid = QGridLayout()
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,0,1)
        grid.addWidget(label3,0,2)
        grid.addWidget(label4,1,1)
        grid.addWidget(label5,1,2)
        
        central_widget.setLayout(grid)
 
def main():
    app  = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
 
    
if __name__ == "__main__":
    main()
