#Pyqt5 checkboxs
import sys #it is a module 
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,QCheckBox)
from PyQt5.QtCore import Qt #GUI uses for inner functions

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my cool first GUI")
        self.setGeometry(700,250,500,500)
        self.checkbox = QCheckBox("Do you like food",self)
        self.initUI()
    def initUI(self):
        self.checkbox.setGeometry(10,0,500,100)
        self.checkbox.setStyleSheet("font-size : 30px;"
                                    "font-family:arial;")
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed) #signal.connect(slot)

    def checkbox_changed(self,state):
        if state == Qt.Checked:
            print("you like food")
        else:
            print("you do not like food")
        
def main():
        app  = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())
       
    
if __name__ == "__main__":
    main()
