#QPixmap
import sys #it is a module 
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QIcon #GUI uses for inner functions
from PyQt5.QtGui import QPixmap
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("my cool first GUI")
        self.setGeometry(700,250,500,500)
        self.setWindowIcon(QIcon("HD-B.jpg"))
        label = QLabel(self)
        label.setGeometry(0,0,250,250)
        pixmap =QPixmap("HD-B.jpg")
        label.setPixmap(pixmap)
        label.setScaledContents(True)
        label.setGeometry((self.width()-label.width())//2,(self.height()-label.height())//2,label.width(),label.height())

def main():
    app  = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
