from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget

class CVPythonView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._init_ui()

    def _init_ui(self):
        layout = QVBoxLayout(self)

        label = QLabel('CV Python')
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
