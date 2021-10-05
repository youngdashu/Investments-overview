from PySide6.QtWidgets import QDialog, QDialogButtonBox, QPushButton

from ui_closeProgramDialog import Ui_Dialog


class CloseProgramDialog(Ui_Dialog, QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        cancelButton: QPushButton = QPushButton("Anuluj", self.frame)
        cancelButton.clicked.connect(self.cancel)

    def cancel(self):
        self.done(2)