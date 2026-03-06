from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget, QTextEdit

class Output(QDockWidget):
    def __init__(self, parent=None):
        super().__init__('Output Panel', parent)
        self.setAllowedAreas(Qt.DockWidgetArea.BottomDockWidgetArea | Qt.DockWidgetArea.TopDockWidgetArea)
        self.setObjectName("output_panel")

        self.output_text = QTextEdit()
        self.output_text.setReadOnly(True)
        self.output_text.setPlaceholderText('Output will appear here...')

        self.setWidget(self.output_text)
