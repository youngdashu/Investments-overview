from PySide6.QtWidgets import QDialog

from ui_delete_investment_dialog import Ui_Dialog

class DeleteInvestmentDialog(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)