from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget, QTreeWidget

class FileExplorer(QDockWidget):
    def __init__(self, parent=None):
        super().__init__('File Explorer', parent)
        self.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)

        self.file_tree = QTreeWidget()
        self.file_tree.setHeaderLabel("Name")

        self.setWidget(self.file_tree)
