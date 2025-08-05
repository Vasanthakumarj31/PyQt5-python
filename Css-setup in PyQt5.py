import sys 
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLineEdit,QPushButton,QWidget,QHBoxLayout)
from PyQt5.QtCore import Qt #GUI uses for inner functions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my cool first GUI")
        self.setGeometry(700,250,500,500)
        self.line_edit = QLineEdit(self)
        self.button1 = QPushButton("#1",self)
        self.button2 = QPushButton("#2",self)
        self.button3 = QPushButton("#3",self)
        self.initUI()
        
    def initUI(self):   
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3) 
        self.button1.setObjectName("Button1")
        self.button2.setObjectName("Button2")
        self.button3.setObjectName("Button3")
        central_widget.setLayout(hbox)       
        self.setStyleSheet("""
                           
                           QPushButton{
                               font-size : 40px;
                               font-family : Arial;
                               padding : 15px 75px;
                               margin : 25px;
                               border : 3px solid;
                               border-radius : 15px;
                           }
                           QPushButton#Button1{
                               background-color:blue;
                           }
                            QPushButton#Button2{
                               background-color:lightblue;
                           }
                            QPushButton#Button3{
                               background-color:lightgreen;
                           }
                            QPushButton#Button1:hover{
                               background-color:lightblue;
                           }
                            QPushButton#Button2:hover{
                               background-color:blue;
                           }
                            QPushButton#Button3:hover{
                               background-color:green;
                           }
                           """)
        
        
    
def main():
        app  = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
       
    
if __name__ == "__main__":
    main()
