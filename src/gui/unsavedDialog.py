from PySide6.QtWidgets import QDialog

from src.gui.ui_UnsavedDialog import Ui_UnsavedDialog


class UnsavedDialog(Ui_UnsavedDialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
