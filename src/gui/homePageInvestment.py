from PySide6.QtWidgets import QWidget, QDialog

from src.gui.deleteInvestmentDialog import DeleteInvestmentDialog
from src.gui.ui_home_page_investment import Ui_InvestmentHomePageWidget
from src.investmentData.investment import deleteInvestmentById


class HomePageInvestment(Ui_InvestmentHomePageWidget, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

    def destroy(self, destroyWindow: bool = True, destroySubWindows: bool = True) -> None:
        self.setVisible(False)
        self.MainFrame.destroy(True, True)
        del self

    def deleteInvestmentAndWidget(self, investmentId):
        dialog = DeleteInvestmentDialog()
        response = dialog.exec()
        if response == QDialog.Accepted:
            deleteInvestmentById(investmentId)
            self.destroy()
