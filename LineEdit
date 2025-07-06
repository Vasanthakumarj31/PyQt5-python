import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QLineEdit,
    QPushButton, QWidget, QVBoxLayout, QHBoxLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Say Hello")
        self.setGeometry(700, 250, 500, 300)

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Enter your name")

        self.button1 = QPushButton("Click Me")
        self.button1.setObjectName("Button1")
        self.button1.clicked.connect(self.say_hello)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.line_edit)
        vbox.addLayout(hbox)

        central_widget = QWidget()
        central_widget.setLayout(vbox)
        self.setCentralWidget(central_widget)

        self.setStyleSheet("""
            QPushButton {
                font-size: 24px;
                padding: 10px 30px;
                border: 2px solid #444;
                border-radius: 8px;
                background-color: #87cefa;
            }
            QPushButton:hover {
                background-color: #00bfff;
                color: white;
            }
            QLineEdit {
                font-size: 18px;
                padding: 8px;
            }
        """)

    def say_hello(self):
        name = self.line_edit.text().strip()
        if name:
            print(f"Hello {name}")
        else:
            print("Please enter your name first!")

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
