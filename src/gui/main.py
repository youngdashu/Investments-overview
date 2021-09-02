import sys
from PySide6 import QtCore, QtGui
from PySide6.QtCore import (QPropertyAnimation)
from PySide6.QtGui import (QColor)
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

from pageTypes import PageTypes
from ui_main_window import Ui_MainWindow

from functools import partial

SHOW_MAXIMIZED = True

labelCounter = 1

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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
        self.ui.frame_credit_data.setVisible(False)
        self.ui.frame_investment_assessment_data.setVisible(False)
        self.ui.frame_own_contribution_data.setVisible(False)

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
        self.ui.button_credit.clicked.connect(self.slideCredit)
        self.rentSlideAnimation = None
        self.ui.button_rent.clicked.connect(self.slideRent)
        self.investmentAssessmentSlideAnimation = None
        self.ui.button_investment_assessment.clicked.connect(self.slideInvestmentAssessment)
        self.ownContributionSlideAnimation = None
        self.ui.button_own_contribution.clicked.connect(self.slideOwnContribution)

        # left buttons section
        self.ui.button_home_page.clicked.connect(lambda : self.mainMenu(PageTypes.homePage))

        self.ui.button_new_investment.clicked.connect(self.myFunction)

        self.showFullScreen()
        self.show()

    def myFunction(self):
        global labelCounter
        newLabel = QLabel("przykładowa inwestycja", self.ui.frame_currently_opened)
        newLabel.setObjectName("new investment" + str(labelCounter))
        labelCounter += 1
        self.ui.horizontalLayout_44.addWidget(newLabel)
        newLabel.show()


    def decreaseFrameHeights(self, minHeight):

        self.ui.frame_information.setMinimumHeight( minHeight)
        # self.ui.frame_main_characteristics.setMinimumHeight(self.ui.frame_main_characteristics.width(), minHeight)
        self.ui.frame_rent.setMinimumHeight( minHeight)
        self.ui.frame_credit.setMinimumHeight(minHeight)
        self.ui.frame_own_contribution.setMinimumHeight( minHeight)
        self.ui.frame_investment_assessment.setMinimumHeight( minHeight)

        self.ui.frame_information.resize(self.ui.frame_information.width(), minHeight)
        # self.ui.frame_main_characteristics.resize(self.ui.frame_main_characteristics.width(), minHeight)
        self.ui.frame_rent.resize(self.ui.frame_rent.width(), minHeight)
        self.ui.frame_credit.resize(self.ui.frame_credit.width(), minHeight)
        self.ui.frame_own_contribution.resize(self.ui.frame_own_contribution.width(), minHeight)
        self.ui.frame_investment_assessment.resize(self.ui.frame_investment_assessment.width(), minHeight)


    def mainMenu(self, pageType: PageTypes):

        if pageType == PageTypes.homePage:
            self.ui.all_pages.setCurrentWidget(self.ui.home_page)


    def slideInformation(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_information.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
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


    def slideCredit(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_credit.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 560
            actualHeight = self.frameHeight
            self.ui.frame_credit_data.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 560
            self.ui.frame_credit_data.setVisible(False)

        self.creditSlideAnimation = QPropertyAnimation(self.ui.frame_credit,
                                                       b'minimumHeight')
        self.creditSlideAnimation.setDuration(450)
        self.creditSlideAnimation.setStartValue(actualHeight)
        self.creditSlideAnimation.setEndValue(afterAnimationHeight)
        self.creditSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.creditSlideAnimation.start()

    def slideRent(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_rent.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
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
        if self.ui.frame_investment_assessment.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
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

    def slideOwnContribution(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_own_contribution.height() < self.targetFrameHeight: # == self.frameHeight:  # height before slide
            isSlided = False
            afterAnimationHeight = 500
            actualHeight = self.frameHeight
            self.ui.frame_own_contribution_data.setVisible(True)
        else:  # self.ui.frame_main_characteristics.height() == 300: # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 500
            self.ui.frame_own_contribution_data.setVisible(False)

        self.ownContributionSlideAnimation = QPropertyAnimation(self.ui.frame_own_contribution,
                                                                    b'minimumHeight')
        self.ownContributionSlideAnimation.setDuration(450)
        self.ownContributionSlideAnimation.setStartValue(actualHeight)
        self.ownContributionSlideAnimation.setEndValue(afterAnimationHeight)
        self.ownContributionSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.ownContributionSlideAnimation.start()

    def restore(self):
        global SHOW_MAXIMIZED
        if SHOW_MAXIMIZED:
            SHOW_MAXIMIZED = False
            self.showNormal()
        else:
            SHOW_MAXIMIZED = True
            self.showFullScreen()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
