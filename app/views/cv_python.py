from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QLabel, QHBoxLayout, QVBoxLayout, QWidget, QComboBox, QToolButton, QPushButton
from PySide6.QtGui import QIcon

class CVPythonView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.content = QHBoxLayout(self)
        self.content.setContentsMargins(0, 0, 0, 0)
        self.content.setSpacing(0)

        self.content.addWidget(self._cv_control())
        self.content.addWidget(self._cv_preview(), stretch=1)

    def _cv_control(self):
        control = QWidget()
        control.setObjectName("cv_control")
        control.setFixedWidth(240)

        layout = QVBoxLayout(control)
        layout.addWidget(QLabel("Computer Vision Script (.py)"))
        layout.addLayout(self._script_row())
        layout.addLayout(self._button_row())
        layout.addStretch()

        return control

    def _script_row(self):
        row = QHBoxLayout()
        self.script_combo = QComboBox()
        self.script_combo.setPlaceholderText("Select a script...")

        folder = self._icon_button("img/folder.png")
        delete = self._icon_button("img/delete.png")

        row.addWidget(self.script_combo, stretch=1)
        row.addWidget(folder)
        row.addWidget(delete)

        return row

    def _button_row(self):
        row = QHBoxLayout()
        self.run_btn = QPushButton("Run")
        self.end_btn = QPushButton("End")

        row.addWidget(self.run_btn)
        row.addWidget(self.end_btn)

        return row

    def _icon_button(self, icon_path):
        btn = QToolButton()
        btn.setIconSize(QSize(18, 18))
        btn.setIcon(QIcon(icon_path))

        return btn

    def _cv_preview(self):
        preview = QLabel("Live preview will appear here.")
        preview.setObjectName("cv_preview")
        preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        return preview




