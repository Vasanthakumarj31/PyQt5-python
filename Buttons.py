#Pyqt5 Buttons

import sys #it is a module 
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QPushButton)
from PyQt5.QtGui import QIcon #GUI uses for inner functions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my cool first GUI")
        self.setGeometry(700,250,500,500)
        self.setWindowIcon(QIcon("HD-B.jpg"))
        self.label = QLabel("hello",self)
        self.initUI()
    def initUI(self):
        self.button = QPushButton("click me!",self)
        self.button.setGeometry(150,200,200,100)
        self.button.setStyleSheet("font-size : 30px;")
        self.button.clicked.connect(self.on_click) # signal.connect(slot)
        
        self.label.setGeometry(150,300,300,100)
        self.label.setStyleSheet("font-size : 50px;")
    
        
    def on_click(self):

        self.label.setText("GOOD BYE")
        self.label.setScaledContents(True)
        
        
def main():
        app  = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
 
    
if __name__ == "__main__":
    main()
