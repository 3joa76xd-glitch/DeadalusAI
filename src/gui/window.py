from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QPushButton,
    QLabel,
    QVBoxLayout
)

from modules.system import get_cpu_usage, get_ram_usage


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Daedalus AI")
        self.resize(800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.system_button = QPushButton("Estado del Sistema")

        self.output_label = QLabel(
            "Presiona el botón para consultar el sistema."
        )

        layout.addWidget(self.system_button)
        layout.addWidget(self.output_label)

        central_widget.setLayout(layout)

        self.system_button.clicked.connect(
            self.show_system_status
        )

    def show_system_status(self):

        cpu = get_cpu_usage()
        ram = get_ram_usage()

        self.output_label.setText(
            f"CPU: {cpu}%\nRAM: {ram}%"
        )