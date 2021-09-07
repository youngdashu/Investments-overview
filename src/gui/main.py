import sys
from PySide6 import QtCore, QtGui
from PySide6.QtCore import (QPropertyAnimation)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QTextEdit

from pageTypes import PageTypes
from src.investmentData.k1 import Investment
from ui_main_window import Ui_MainWindow


from functools import partial

SHOW_MAXIMIZED = True

labelCounter = 1


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.investments = []

        self.ui.closeButton.clicked.connect(self.close)
        self.ui.minimizeButton.clicked.connect(self.showMinimized())
        self.ui.restoreButton.clicked.connect(self.restore)

        # self.tables = [self.ui.tableRent, self.ui.tableCredit, self.ui.tableInformation,
        #                self.ui.tableMainCharacteristics, self.ui.tableOwnContribution,
        #                self.ui.tableInvestmentAssessment]

        self.frameHeight = 80
        self.targetFrameHeight = 300

        self.ui.frame_information_data.setVisible(False)
        self.ui.frame_rent_data.setVisible(False)
        self.ui.frame_investment_assessment_data.setVisible(False)
        self.ui.frame_own_contribution_credit_inner.setVisible(False)


        self.decreaseFrameHeights(40)

        # animation section

        # self.isMcInfoFrameSlided = False
        # self.mcInfoFrameHeight = self.ui.frame_mc_info.height()
        # self.mcInfoSlideAnimation = None

        # self.mainCharacteristicsSlideAnimation = None
        # self.ui.button_main_characteristics.clicked.connect(self.slideMcAndInfo)
        self.informationSlideAnimation = None
        self.ui.button_information.clicked.connect(self.slideInformation)
        self.creditSlideAnimation = None

        self.rentSlideAnimation = None
        self.ui.button_rent.clicked.connect(self.slideRent)
        self.investmentAssessmentSlideAnimation = None
        self.ui.button_investment_assessment.clicked.connect(self.slideInvestmentAssessment)
        self.ownContributionCreditSlideAnimation = None
        self.ui.button_own_contribution_credit.clicked.connect(self.slideOwnContributionCredit)

        # left buttons section
        self.ui.button_home_page.clicked.connect(lambda: self.mainMenu(PageTypes.homePage))

        self.ui.button_new_investment.clicked.connect(self.addNewInvestment)

        
        self.show()

    def myFunction(self):
        global labelCounter
        newLabel = QLabel("przykładowa inwestycja", self.ui.frame_currently_opened)
        newLabel.setObjectName("new investment" + str(labelCounter))
        labelCounter += 1
        self.ui.horizontalLayout_44.addWidget(newLabel)
        newLabel.show()

    def decreaseFrameHeights(self, minHeight):

        self.ui.frame_information.setMinimumHeight(minHeight)
        # self.ui.frame_main_characteristics.setMinimumHeight(self.ui.frame_main_characteristics.width(), minHeight)
        self.ui.frame_rent.setMinimumHeight(minHeight)

        self.ui.frame_own_contribution_credit.setMinimumHeight(minHeight)
        self.ui.frame_investment_assessment.setMinimumHeight(minHeight)

        self.ui.frame_information.resize(self.ui.frame_information.width(), minHeight)
        # self.ui.frame_main_characteristics.resize(self.ui.frame_main_characteristics.width(), minHeight)
        self.ui.frame_rent.resize(self.ui.frame_rent.width(), minHeight)
        self.ui.frame_own_contribution_credit.resize(self.ui.frame_own_contribution_credit.width(), minHeight)
        self.ui.frame_investment_assessment.resize(self.ui.frame_investment_assessment.width(), minHeight)

    def mainMenu(self, pageType: PageTypes):

        if pageType == PageTypes.homePage:
            self.ui.all_pages.setCurrentWidget(self.ui.home_page)

    def slideInformation(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_information.height() < self.targetFrameHeight:  # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 400
            actualHeight = self.frameHeight
            self.ui.frame_information_data.setVisible(True)

        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 400
            self.ui.frame_information_data.setVisible(False)

        self.informationSlideAnimation = QPropertyAnimation(self.ui.frame_information,
                                                            b'minimumHeight')
        self.informationSlideAnimation.setDuration(450)
        self.informationSlideAnimation.setStartValue(actualHeight)
        self.informationSlideAnimation.setEndValue(afterAnimationHeight)
        self.informationSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.informationSlideAnimation.start()



    def slideRent(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_rent.height() < self.targetFrameHeight:  # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 750
            actualHeight = self.frameHeight
            self.ui.frame_rent_data.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 750
            self.ui.frame_rent_data.setVisible(False)

        self.rentSlideAnimation = QPropertyAnimation(self.ui.frame_rent,
                                                     b'minimumHeight')
        self.rentSlideAnimation.setDuration(450)
        self.rentSlideAnimation.setStartValue(actualHeight)
        self.rentSlideAnimation.setEndValue(afterAnimationHeight)
        self.rentSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.rentSlideAnimation.start()

    def slideInvestmentAssessment(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_investment_assessment.height() < self.targetFrameHeight:  # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 400
            actualHeight = self.frameHeight
            self.ui.frame_investment_assessment_data.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 400
            self.ui.frame_investment_assessment_data.setVisible(False)

        self.investmentAssessmentSlideAnimation = QPropertyAnimation(self.ui.frame_investment_assessment,
                                                                     b'minimumHeight')
        self.investmentAssessmentSlideAnimation.setDuration(450)
        self.investmentAssessmentSlideAnimation.setStartValue(actualHeight)
        self.investmentAssessmentSlideAnimation.setEndValue(afterAnimationHeight)
        self.investmentAssessmentSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.investmentAssessmentSlideAnimation.start()

    # noinspection DuplicatedCode
    def slideOwnContributionCredit(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_own_contribution_credit.height() < self.targetFrameHeight:  # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 600
            actualHeight = self.frameHeight
            # self.ui.frame_own_contribution_data.setVisible(True)
            # self.ui.frame_credit_data.setVisible(True)
            self.ui.frame_own_contribution_credit_inner.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 600
            # self.ui.frame_own_contribution_data.setVisible(False)
            # self.ui.frame_credit_data.setVisible(False)
            self.ui.frame_own_contribution_credit_inner.setVisible(False)

        self.ownContributionCreditSlideAnimation = QPropertyAnimation(self.ui.frame_own_contribution_credit,
                                                                b'minimumHeight')
        self.ownContributionCreditSlideAnimation.setDuration(450)
        self.ownContributionCreditSlideAnimation.setStartValue(actualHeight)
        self.ownContributionCreditSlideAnimation.setEndValue(afterAnimationHeight)
        self.ownContributionCreditSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.ownContributionCreditSlideAnimation.start()

    def restore(self):
        global SHOW_MAXIMIZED
        if SHOW_MAXIMIZED:
            SHOW_MAXIMIZED = False
            self.showNormal()
        else:
            SHOW_MAXIMIZED = True
            self.showFullScreen()


    def loadInvestments(self):

        # read from file

        investments = []

        pass

    def clearInvestmentPage(self, parent):

        print(parent)

        if type(parent) is QTextEdit:
            parent.setText("")
        else:
            children = parent.getChildren(QWidget)
            for c in children:
                self.clearInvestmentPage(c)



    def addNewInvestment(self):

        newInvestment = Investment()


        self.ui.all_pages.setCurrentWidget(self.ui.investment_page)

        print("-------")

        self.clearInvestmentPage(self.ui.investment_page)

    def showInvestmentOnMainPage(self, investment: Investment):

        self.ui.text_investment_name.setText(investment.title)
        self.ui.text_purchase_price.setText(investment.purchasePrice())
        self.ui.text_area.setText(investment.area())
        self.ui.text_price_per_square_meter.setText(investment.pricePerSquareMeter())
        self.ui.text_start_date.setText(investment.startDate())
        self.ui.text_description.setText(investment.description())
        self.ui.text_address_street.setText(investment.addressStreet())
        self.ui.text_address_city.setText(investment.addressCity())
        self.ui.text_estimated_value.setText(investment.estimatedCurrentValue())
        self.ui.text_last_estimation.setText(investment.lastEstimationDate())
        self.ui.text_finish_date.setText(investment.finishDate())
        self.ui.text_own_contribution.setText(investment.ownContribution())
        self.ui.text_own_contribution_percent.setText(int((investment.ownContribution() / investment.purchasePrice()) * 100) + "%")
        self.ui.text_broker_margin.setText(investment.brokerMargin())
        self.ui.text_broker_margin_percent.setText(int((investment.brokerMargin() / investment.purchasePrice()) * 100) + "%")
        self.ui.text_notary_margin.setText(investment.notaryMargin())
        self.ui.text_broker_margin_percent.setText(int((investment.notaryMargin() / investment.purchasePrice()) * 100) + "%")
        self.ui.text_tax.setText(investment.tax())
        self.ui.text_tax_percent.setText(int((investment.tax() / investment.purchasePrice()) * 100) + "%")
        self.ui.text_other_costs.setText(investment.otherCosts())
        self.ui.text_other_costs_percent.setText(int((investment.otherCosts() / investment.purchasePrice()) * 100) + "%")
        self.ui.text_renovation.setText(investment.renovationCost())
        self.ui.text_renovation_percent.setText(int((investment.renovationCost() / investment.purchasePrice()) * 100) + "%")
        self.ui.text_entry_cost.setText(investment.entryCost())
        self.ui.text_invested_vs_purchase.setText(investment.investedVsPurchasePrice())
        self.ui.text_credit.setText(investment.bankCredit())
        self.ui.text_bank_contribution.setText(investment.bankContributionPercent() + "%")
        self.ui.text_interest_rate.setText(investment.interestRate())
        self.ui.text_repayment_period.setText(investment.repaymentPeriod())
        self.ui.text_monthly_installment.setText(investment.monthlyInstallment())
        self.ui.text_monthly_installment_capital_part.setText(investment.monthlyInstallmentCapitalPart())
        self.ui.text_monthly_installment_interest_part.setText(investment.monthlyInstallmentInterestPart())
        self.ui.text_credit_credit_insurance_per_month.setText(investment.creditInsurancePerMonth())
        self.ui.text_total_credit_cost.setText(investment.totalCreditCost())
        self.ui.
        self.ui.
        self.ui.
        self.ui.
        self.ui.
        self.ui.
        self.ui.
        self.ui.
        self.ui.
        self.ui.
        self.ui.








if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
