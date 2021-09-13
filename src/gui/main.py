import sys
from PySide6 import QtCore, QtGui
from PySide6.QtCore import (QPropertyAnimation)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QTextEdit, QFrame, QHBoxLayout, QPushButton

from pageTypes import PageTypes
from src.investmentData.k1 import Investment
from ui_main_window import Ui_MainWindow

from functools import partial

SHOW_MAXIMIZED = True

labelCounter = 1

qObjectCounter = 1

tabCounter = 1

buttonCounter = 1

layoutCounter = 1

frameStyleSheet = """QFrame{
        border: 1px solid gray;
        border-radius: 10px;
        background: rgb(207, 206, 209);
        }"""

highlightedFrameStyleSheet = """QFrame{
        border: 1px solid gray;
        border-radius: 10px;
        background: rgb(255, 255, 255);
        }"""

noDataText = "Brak danych"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.textEditsConnected = False

        self.investments = []
        self.investmentTabs = []

        self.ui.closeButton.clicked.connect(self.close)
        self.ui.minimizeButton.clicked.connect(self.showMinimized())
        self.ui.restoreButton.clicked.connect(self.restore)

        # self.tables = [self.ui.tableRent, self.ui.tableCredit, self.ui.tableInformation,
        #                self.ui.tableMainCharacteristics, self.ui.tableOwnContribution,
        #                self.ui.tableInvestmentAssessment]

        # read only text edits
        self.readOnlyTextEdits = [self.ui.text_price_per_square_meter, self.ui.text_own_contribution_percent,
                                  self.ui.text_broker_margin_percent, self.ui.text_notary_margin_percent,
                                  self.ui.text_tax_percent, self.ui.text_other_costs_percent,
                                  self.ui.text_renovation_percent, self.ui.text_entry_cost, self.ui.text_credit,
                                  self.ui.text_bank_contribution, self.ui.text_monthly_installment,
                                  self.ui.text_monthly_installment_capital_part,
                                  self.ui.text_monthly_installment_interest_part, self.ui.text_total_credit_cost,
                                  self.ui.text_rent_income_min_year,
                                  self.ui.text_rent_income_max_year, self.ui.text_rent_income_max_year,
                                  self.ui.text_income_earned_year,
                                  self.ui.text_rent_tax_year, self.ui.text_property_tax_month,
                                  self.ui.text_electricity_year, self.ui.text_gas_year, self.ui.text_water_year,
                                  self.ui.text_internet_year, self.ui.text_other_costs_year,
                                  self.ui.text_total_costs_month, self.ui.text_total_costs_year,
                                  self.ui.text_rent_gain_loss_month, self.ui.text_rent_gain_loss_year]

        self.editableTextEdits = [self.ui.text_investment_name,
                                  self.ui.text_purchase_price,
                                  self.ui.text_area,
                                  self.ui.text_start_date,
                                  self.ui.text_description,
                                  self.ui.text_address_street,
                                  self.ui.text_address_city,
                                  self.ui.text_estimated_value,
                                  self.ui.text_last_estimation,
                                  self.ui.text_finish_date,
                                  self.ui.text_own_contribution,
                                  self.ui.text_broker_margin,
                                  self.ui.text_notary_margin,
                                  self.ui.text_tax,
                                  self.ui.text_other_costs,
                                  self.ui.text_renovation,
                                  self.ui.text_interest_rate,
                                  self.ui.text_repayment_period,
                                  self.ui.text_credit_credit_insurance_per_month,
                                  self.ui.text_rent_income_min_month,
                                  self.ui.text_rent_income_max_month,
                                  self.ui.text_income_earned_month,
                                  self.ui.text_rent_tax_month,
                                  self.ui.text_property_tax_year,
                                  self.ui.text_electricity_month,
                                  self.ui.text_gas_month,
                                  self.ui.text_water_month,
                                  self.ui.text_internet_month,
                                  self.ui.text_other_costs_month]

        for readOnlyFrame in self.readOnlyTextEdits:
            readOnlyFrame.setReadOnly(True)

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

        self.ui.all_pages.setCurrentWidget(self.ui.home_page)

        self.show()

    # def myFunction(self):
    #     global labelCounter
    #     newLabel = QLabel("przykładowa inwestycja", self.ui.frame_currently_opened)
    #     newLabel.setObjectName("new investment" + str(labelCounter))
    #     labelCounter += 1
    #     self.ui.horizontalLayout_44.addWidget(newLabel)
    #     newLabel.show()

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

    # def clearInvestmentPage(self, parent):
    #
    #     print(parent)
    #
    #     if type(parent) is QTextEdit:
    #         parent.setText("")
    #         print("Clear")
    #     else:
    #         children = []
    #         try:
    #             children = parent.getChildren(QWidget)
    #         except:
    #             pass
    #         for c in children:
    #             self.clearInvestmentPage(c)

    def addNewInvestment(self):

        global tabCounter
        global buttonCounter
        global layoutCounter

        newInvestment = Investment()
        self.investments.append(newInvestment)

        for inv in self.investments:
            print("! ", inv)

        print(newInvestment)

        # add frame to tab bar
        investmentFrame = QFrame(self.ui.scrollAreaContents_currently_opened)
        investmentFrame.setStyleSheet(frameStyleSheet)
        investmentFrame.setObjectName("Tab_" + str(tabCounter))
        tabCounter += 1
        investmentFrameLayout = QHBoxLayout(investmentFrame)
        investmentFrameLayout.setObjectName("layout_investment_" + str(layoutCounter))
        layoutCounter += 1
        closeFrameButton = QPushButton("x", investmentFrame)
        closeFrameButton.setObjectName("Close_button" + str(buttonCounter))
        buttonCounter += 1
        closeFrameButton.setMaximumWidth(20)
        openInvestmentButton = QPushButton("Inwestycja nienazwana", investmentFrame)
        openInvestmentButton.setObjectName("investment_button" + str(buttonCounter))
        buttonCounter += 1

        investmentFrameLayout.addWidget(closeFrameButton)
        investmentFrameLayout.addWidget(openInvestmentButton)

        self.investmentTabs.append(investmentFrame)

        openInvestmentButton.clicked.connect(lambda: self.showInvestmentOnMainPage(newInvestment, investmentFrame))

        self.ui.scrollAreaContents_currently_opened_layout.addWidget(investmentFrame)

        self.ui.all_pages.setCurrentWidget(self.ui.investment_page)

        # self.ui.text_investment_name.setText("Test" + str(labelCounter))

        self.showInvestmentOnMainPage(newInvestment, investmentFrame)

    def showInvestmentOnMainPage(self, investment: Investment, frameToHighlight: QFrame):

        for frame in self.investmentTabs:
            if frame is frameToHighlight:
                frame.setStyleSheet(highlightedFrameStyleSheet)
            else:
                frame.setStyleSheet(frameStyleSheet)

        self.ui.all_pages.setCurrentWidget(self.ui.investment_page)

        self.captureTextEdits(investment)

        self.ui.text_investment_name.setText(investment.title)
        self.ui.text_purchase_price.setText(str(investment.purchasePrice()))
        self.ui.text_area.setText(str(investment.area()))
        self.ui.text_price_per_square_meter.setText(str(investment.pricePerSquareMeter()))
        self.ui.text_start_date.setText(str(investment.startDate()))
        self.ui.text_description.setText(str(investment.description()))
        self.ui.text_address_street.setText(str(investment.addressStreet()))
        self.ui.text_address_city.setText(str(investment.addressCity()))
        self.ui.text_estimated_value.setText(str(investment.estimatedCurrentValue()))
        self.ui.text_last_estimation.setText(str(investment.lastEstimationDate()))
        self.ui.text_finish_date.setText(str(investment.finishDate()))
        self.ui.text_own_contribution.setText(str(investment.ownContribution()))
        ownContributionText = str(int((investment.ownContribution() / investment.purchasePrice()) * 100)) + "%" if type(
            investment.ownContribution()) is not str and type(investment.purchasePrice()) is not str else noDataText
        self.ui.text_own_contribution_percent.setText(ownContributionText)
        self.ui.text_broker_margin.setText(str(investment.brokerMargin()))
        self.ui.text_broker_margin_percent.setText(
            str(int((investment.brokerMargin() / investment.purchasePrice()) * 100)) + "%" if type(
                investment.brokerMargin()) is not str and type(investment.purchasePrice()) is not str else noDataText)
        self.ui.text_notary_margin.setText(str(investment.notaryMargin()))
        self.ui.text_notary_margin_percent.setText(
            str(int((investment.notaryMargin() / investment.purchasePrice()) * 100)) + "%" if type(
                investment.notaryMargin()) is not str and type(investment.purchasePrice()) is not str else noDataText)
        self.ui.text_tax.setText(str(investment.tax()))
        self.ui.text_tax_percent.setText(str(int((investment.tax() / investment.purchasePrice()) * 100)) + "%" if type(
            investment.tax()) is not str and type(investment.purchasePrice()) is not str else noDataText)
        self.ui.text_other_costs.setText(str(investment.otherCosts()))
        self.ui.text_other_costs_percent.setText(
            str(int((investment.otherCosts() / investment.purchasePrice()) * 100)) + "%" if type(
                investment.otherCosts()) is not str and type(investment.purchasePrice()) is not str else noDataText)
        self.ui.text_renovation.setText(str(investment.renovationCost()))
        self.ui.text_renovation_percent.setText(
            str(int((investment.renovationCost() / investment.purchasePrice()) * 100)) + "%" if type(
                investment.renovationCost()) is not str and type(investment.purchasePrice()) is not str else noDataText)
        self.ui.text_entry_cost.setText(str(investment.entryCost()))
        self.ui.text_invested_vs_purchase.setText(str(investment.investedVsPurchasePrice()))
        self.ui.text_credit.setText(str(investment.bankCredit()))
        self.ui.text_bank_contribution.setText(str(investment.bankContributionPercent()) + "%")
        self.ui.text_interest_rate.setText(str(investment.interestRate()))
        self.ui.text_repayment_period.setText(str(investment.repaymentPeriod()))
        self.ui.text_monthly_installment.setText(str(investment.monthlyInstallment()))
        self.ui.text_monthly_installment_capital_part.setText(str(investment.monthlyInstallmentCapitalPart()))
        self.ui.text_monthly_installment_interest_part.setText(str(investment.monthlyInstallmentInterestPart()))
        self.ui.text_credit_credit_insurance_per_month.setText(str(investment.creditInsurancePerMonth()))
        self.ui.text_total_credit_cost.setText(str(investment.totalCreditCost()))
        self.ui.text_rent_income_min_month.setText(str(investment.rentIncomeMinPerMonth()))
        self.ui.text_rent_income_min_year.setText(str(investment.rentIncomeMinPerMonth() * 12) if type(
            investment.rentIncomeMinPerMonth()) is not str else noDataText)
        # self.ui.text_rent_income_min_percent
        self.ui.text_rent_income_max_month.setText(str(investment.rentIncomeMaxPerMonth()))
        self.ui.text_rent_income_max_year.setText(str(investment.rentIncomeMaxPerMonth() * 12) if type(
            investment.rentIncomeMaxPerMonth()) is not str else noDataText)
        # self.ui.text_rent_income_max_percent
        self.ui.text_income_earned_month.setText(str(investment.incomeReceivedPerMonth()))
        self.ui.text_income_earned_year.setText(str(investment.incomeReceivedPerMonth() * 12) if type(
            investment.incomeReceivedPerMonth()) is not str else noDataText)
        # self.ui.text_income_earned_percent
        self.ui.text_rent_tax_month.setText(str(investment.rentTaxPerMonth()))
        self.ui.text_rent_tax_year.setText(
            str(investment.rentTaxPerMonth() * 12) if type(investment.rentTaxPerMonth()) is not str else noDataText)
        self.ui.text_property_tax_month.setText(str(investment.propertyTaxPerYear() / 12) if type(
            investment.propertyTaxPerYear()) is not str else noDataText)
        self.ui.text_property_tax_year.setText(str(investment.propertyTaxPerYear()))
        self.ui.text_electricity_month.setText(str(investment.electricityPerMonth()))
        self.ui.text_electricity_year.setText(str(investment.electricityPerMonth() * 12) if type(
            investment.electricityPerMonth()) is not str else noDataText)
        self.ui.text_gas_month.setText(str(investment.gasPerMonth()))
        self.ui.text_gas_year.setText(
            str(investment.gasPerMonth() * 12) if type(investment.gasPerMonth()) is not str else noDataText)
        self.ui.text_water_month.setText(str(investment.waterPerMonth()))
        self.ui.text_water_year.setText(
            str(investment.waterPerMonth() * 12) if type(investment.waterPerMonth()) is not str else noDataText)
        self.ui.text_internet_month.setText(str(investment.internetPerMonth()))
        self.ui.text_internet_year.setText(
            str(investment.internetPerMonth() * 12) if type(investment.internetPerMonth()) is not str else noDataText)
        self.ui.text_other_costs_month.setText(str(investment.otherPerMonth()))
        self.ui.text_other_costs_year.setText(
            str(investment.otherPerMonth() * 12) if type(investment.otherPerMonth()) is not str else noDataText)
        self.ui.text_total_costs_month.setText(str(investment.costsTotalPerMonth()))
        self.ui.text_total_costs_year.setText(str(investment.costsTotalPerMonth() * 12) if type(
            investment.costsTotalPerMonth()) is not str else noDataText)
        self.ui.text_rent_gain_loss_month.setText(str(investment.incomeOrLossPerMonth()))
        self.ui.text_rent_gain_loss_year.setText(str(investment.incomeOrLossPerMonth() * 12) if type(
            investment.incomeOrLossPerMonth()) is not str else noDataText)
        self.ui.label_own_capital_return_time_months.setText(str(investment.ownCapitalReturnTimeMonths()))
        self.ui.label_own_capital_return_time_years.setText(str(investment.ownCapitalReturnTimeYears()))

    def captureTextEdits(self, investment):

        if self.textEditsConnected:
            print("odlaczam")
            self.textEditsConnected = False
            # map(lambda editableTextEdit: editableTextEdit.textChanged.disconnect(), self.editableTextEdits)

            self.ui.text_investment_name.textChanged.disconnect()
            self.ui.text_purchase_price.textChanged.disconnect()
            self.ui.text_area.textChanged.disconnect()
            self.ui.text_start_date.textChanged.disconnect()
            self.ui.text_description.textChanged.disconnect()
            self.ui.text_address_street.textChanged.disconnect()
            self.ui.text_address_city.textChanged.disconnect()
            self.ui.text_estimated_value.textChanged.disconnect()
            self.ui.text_last_estimation.textChanged.disconnect()
            self.ui.text_finish_date.textChanged.disconnect()
            self.ui.text_own_contribution.textChanged.disconnect()
            self.ui.text_broker_margin.textChanged.disconnect()
            self.ui.text_notary_margin.textChanged.disconnect()
            self.ui.text_tax.textChanged.disconnect()
            self.ui.text_other_costs.textChanged.disconnect()
            self.ui.text_renovation.textChanged.disconnect()
            self.ui.text_interest_rate.textChanged.disconnect()
            self.ui.text_repayment_period.textChanged.disconnect()
            self.ui.text_credit_credit_insurance_per_month.textChanged.disconnect()
            self.ui.text_rent_income_min_month.textChanged.disconnect()
            self.ui.text_rent_income_max_month.textChanged.disconnect()
            self.ui.text_income_earned_month.textChanged.disconnect()
            self.ui.text_rent_tax_month.textChanged.disconnect()
            self.ui.text_property_tax_year.textChanged.disconnect()
            self.ui.text_electricity_month.textChanged.disconnect()
            self.ui.text_gas_month.textChanged.disconnect()
            self.ui.text_water_month.textChanged.disconnect()
            self.ui.text_internet_month.textChanged.disconnect()
            self.ui.text_other_costs_month.textChanged.disconnect()

        self.textEditsConnected = True

        self.ui.text_investment_name.textChanged.connect(
            lambda: investment.setTitle(self.ui.text_investment_name.toPlainText()))
        self.ui.text_purchase_price.textChanged.connect(
            lambda: investment.setPurchasePrice(self.ui.text_purchase_price.toPlainText()))
        self.ui.text_area.textChanged.connect(lambda: investment.setArea(self.ui.text_area.toPlainText()))
        self.ui.text_start_date.textChanged.connect(
            lambda: investment.setStartDate(self.ui.text_start_date.toPlainText()))
        self.ui.text_description.textChanged.connect(
            lambda: investment.setDescription(self.ui.text_description.toPlainText()))
        self.ui.text_address_street.textChanged.connect(
            lambda: investment.setAddressStreet(self.ui.text_address_street.toPlainText()))
        self.ui.text_address_city.textChanged.connect(
            lambda: investment.setAddressCity(self.ui.text_address_city.toPlainText()))
        self.ui.text_estimated_value.textChanged.connect(
            lambda: investment.setEstimatedCurrentValue(self.ui.text_estimated_value.toPlainText()))
        self.ui.text_last_estimation.textChanged.connect(
            lambda: investment.setLastEstimationDate(self.ui.text_last_estimation.toPlainText()))
        self.ui.text_finish_date.textChanged.connect(
            lambda: investment.setFinishDate(self.ui.text_finish_date.toPlainText()))
        self.ui.text_own_contribution.textChanged.connect(
            lambda: investment.setOwnContribution(self.ui.text_own_contribution.toPlainText()))
        self.ui.text_broker_margin.textChanged.connect(
            lambda: investment.setBrokerMargin(self.ui.text_broker_margin.toPlainText()))
        self.ui.text_notary_margin.textChanged.connect(
            lambda: investment.setNotaryMargin(self.ui.text_notary_margin.toPlainText()))
        self.ui.text_tax.textChanged.connect(lambda: investment.setTax(self.ui.text_tax.toPlainText()))
        self.ui.text_other_costs.textChanged.connect(
            lambda: investment.setOtherCosts(self.ui.text_other_costs.toPlainText()))
        self.ui.text_renovation.textChanged.connect(
            lambda: investment.setRenovationCost(self.ui.text_renovation.toPlainText()))
        self.ui.text_interest_rate.textChanged.connect(
            lambda: investment.setInterestRate(self.ui.text_interest_rate.toPlainText()))
        self.ui.text_repayment_period.textChanged.connect(
            lambda: investment.setRepaymentPeriod(self.ui.text_repayment_period.toPlainText()))
        self.ui.text_credit_credit_insurance_per_month.textChanged.connect(
            lambda: investment.setCreditInsurancePerMonth(self.ui.text_credit_credit_insurance_per_month.toPlainText()))
        self.ui.text_rent_income_min_month.textChanged.connect(
            lambda: investment.setRentIncomeMinPerMonth(self.ui.text_rent_income_min_month.toPlainText()))
        self.ui.text_rent_income_max_month.textChanged.connect(
            lambda: investment.setRentIncomeMaxPerMonth(self.ui.text_rent_income_max_month.toPlainText()))
        self.ui.text_income_earned_month.textChanged.connect(
            lambda: investment.setIncomeReceivedPerMonth(self.ui.text_income_earned_month.toPlainText()))
        self.ui.text_rent_tax_month.textChanged.connect(
            lambda: investment.setRentTaxPerMonth(self.ui.text_rent_tax_month.toPlainText()))
        self.ui.text_property_tax_year.textChanged.connect(
            lambda: investment.setPropertyTaxPerYear(self.ui.text_property_tax_year.toPlainText()))
        self.ui.text_electricity_month.textChanged.connect(
            lambda: investment.setElectricityPerMonth(self.ui.text_electricity_month.toPlainText()))
        self.ui.text_gas_month.textChanged.connect(
            lambda: investment.setGasPerMonth(self.ui.text_gas_month.toPlainText()))
        self.ui.text_water_month.textChanged.connect(
            lambda: investment.setWaterPerMonth(self.ui.text_water_month.toPlainText()))
        self.ui.text_internet_month.textChanged.connect(
            lambda: investment.setInternetPerMonth(self.ui.text_internet_month.toPlainText()))
        self.ui.text_other_costs_month.textChanged.connect(
            lambda: investment.setOtherPerMonth(self.ui.text_other_costs_month.toPlainText()))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
