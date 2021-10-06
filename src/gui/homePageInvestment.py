from PySide6.QtWidgets import QWidget

from src.gui.ui_home_page_investment import Ui_InvestmentHomePageWidget


class HomePageInvestment(Ui_InvestmentHomePageWidget, QWidget):
    def __init__(self, parent=None):
        # super(HomePageInvestment, self).__init__()
        super().__init__(parent)
        self.setupUi(self)

    def destroy(self, destroyWindow: bool = True, destroySubWindows: bool = True) -> None:
        self.MainFrame.destroy(True, True)
        self.setVisible(False)
        del self
