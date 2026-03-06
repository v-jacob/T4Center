import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFileSystemWatcher
from app.window import MainWindow

STYLE_PATH = "style.qss"

def load_style(app):
    with open(STYLE_PATH) as f:
        app.setStyleSheet(f.read())

def main():
    app = QApplication(sys.argv)

    load_style(app)
    watcher = QFileSystemWatcher([STYLE_PATH])
    watcher.fileChanged.connect(lambda: load_style(app))

    wind = MainWindow()
    wind.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
