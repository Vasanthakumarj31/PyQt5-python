#PyQt5 introduction
#it is used for GUI frame works
import sys #it is a module 
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon #GUI uses for inner functions
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt #QtCore helps for postioning
from PyQt5.QtGui import QPixmap
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my cool first GUI")
        self.setGeometry(700,250,500,500)
        self.setWindowIcon(QIcon("HD-B.jpg"))
        label = QLabel("hello",self)
        label.setFont(QFont("Arial",50))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color : blue;"
                            "background-color : yellow;"
                            "font-weight : bold;"
                            "font-style : italic;"
                            "text-decoration : underline;")
        #label.setAlignment(Qt.AlignTop) #vertically top
        #label.setAlignment(Qt.AlignBottom) # vertically bottom
        #abel.setAlignment(Qt.AlignVCenter) # vertically bottom
        #label.setAlignment(Qt.AlignRight) # Horizontally bottom
        #label.setAlignment(Qt.AlignHCenter) # Horizontally bottom
        #label.setAlignment(Qt.AlignLeft) #Horizontally left
        #label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) #center and Bottom
        label.setAlignment(Qt.AlignCenter) #both herzionally and vertically
        
def main():
    app  = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
