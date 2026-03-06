from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QIcon
from app.central import Central
from app.file_explorer import FileExplorer
from app.device import DeviceConfig
from app.output import Output
from app.status_bar import StatusBar

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("T4Center")
        self.setWindowIcon(QIcon('img/icon.png'))
        self.resize(1200, 800)
        self.showMaximized()

        # Widgets
        central = Central(self)
        self.setCentralWidget(central)

        # File Explorer
        file_explorer = FileExplorer(self)
        self.addDockWidget(Qt.DockWidgetArea(0x1), file_explorer)

        # Device Config
        device_config = DeviceConfig(self)
        self.addDockWidget(Qt.DockWidgetArea(0x2), device_config)

        # Output
        output = Output(self)
        self.addDockWidget(Qt.DockWidgetArea(0x8), output)
        self.resizeDocks([output], [150], Qt.Orientation.Vertical)

        # Status Bar
        self.setStatusBar(StatusBar(self))
