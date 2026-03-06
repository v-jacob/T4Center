from PySide6.QtWidgets import QWidget, QTabWidget, QVBoxLayout, QLabel
from app.views.cv_python import CVPythonView
from app.views.device_monitor import DeviceMonitorView

class Central(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Layout
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Header
        self.header = QLabel()
        self.header.setObjectName("central_header")

        # Pages
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.TabPosition.South)
        tabs.setMovable(True)
        tabs.addTab(CVPythonView(), 'CV Python')
        tabs.addTab(DeviceMonitorView(), 'Device Monitor')

        # Set header to selected tab
        tabs.currentChanged.connect(lambda i: self.header.setText(tabs.tabText(i)))
        self.header.setText(tabs.tabText(0))

        layout.addWidget(self.header)
        layout.addWidget(tabs)
