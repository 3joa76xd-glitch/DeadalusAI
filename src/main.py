import sys
from modules.system import get_cpu_usage, get_ram_usage

print(f"CPU: {get_cpu_usage()}%")
print(f"RAM: {get_ram_usage()}%")

from PySide6.QtWidgets import QApplication

from gui.window import MainWindow


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())