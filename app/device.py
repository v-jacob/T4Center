from PySide6.QtCore import Qt
from PySide6.QtWidgets import QDockWidget, QWidget, QLabel, QVBoxLayout

class DeviceConfig(QDockWidget):
    def __init__(self, parent=None):
        super().__init__('Device Configuration', parent)
        self.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea | Qt.DockWidgetArea.RightDockWidgetArea)
        self.setMinimumWidth(250)
        self.setObjectName("device_config")

        place_holder = QWidget()
        layout = QVBoxLayout(place_holder)
        label = QLabel("Device configuration.")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.setWidget(place_holder)
