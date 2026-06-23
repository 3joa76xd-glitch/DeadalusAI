from PySide6.QtWidgets import QMainWindow, QLabel
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daedalus AI")
        self.resize(800, 600)

        label = QLabel("Daedalus AI v0.0.1")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)