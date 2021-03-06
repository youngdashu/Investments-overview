import sys
from typing import Dict, List

import PySide6
from PySide6 import QtCore, QtGui
from PySide6.QtCore import (QPropertyAnimation)
from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QFrame, QHBoxLayout, QPushButton, \
    QDialog, QDialogButtonBox

import locale

from pageTypes import PageTypes
from src.investmentData.investment import Investment, getInvestments, getInvestmentById, deleteInvestmentById
from src.utilityQtObjectsFunctions.Note import Note
from src.utilityQtObjectsFunctions.functions import removeExcessiveBorders, saveAllInvestments, disconnectFunction, \
    connectEventFilter, setDarkerBackgroundForStaticTextEdits, clearHomePageWidgetsAndLoadNewWidgets, darkerStyleSheet, \
    setLabelStyleSheet, setTextEditAlignmentCenter
from src.utilityQtObjectsFunctions.options import Options
from src.utilityQtObjectsFunctions.resizeWindow import changeObjectFontSize
from ui_main_window import Ui_MainWindow

from unsavedDialog import UnsavedDialog
from closeProgramDialog import CloseProgramDialog
from homePageInvestment import HomePageInvestment

locale.setlocale(locale.LC_MONETARY)

SHOW_MAXIMIZED = True

labelCounter = 1

qObjectCounter = 1

tabCounter = 1

buttonCounter = 1

layoutCounter = 1

homePageInvestmentWidgetCounter = 1

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

noBorderFrameStyleSheetTemplate = """{
        border: 0px solid gray;
        border-radius: 10px;
        background: rgb(207, 206, 209);
        }"""

noDataText = "Brak danych"


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.savedIcon: QPixmap = QPixmap("icons/saved.png")
        self.unsavedIcon: QPixmap = QPixmap("icons/unsaved.png")

        self.textEditsConnected = False

        self.investments: Dict[int, Investment] = {}
        self.investmentTabs: Dict[int, QFrame] = {}
        self.isInvestmentSaved: Dict[int, bool] = {}
        self.currentInvestment: Investment = None
        self.currentInvestmentTabIconLabel: QLabel = None

        # self.ui.closeButton.clicked.connect(self.close)
        # self.ui.minimizeButton.clicked.connect(self.showMinimized())
        # self.ui.restoreButton.clicked.connect(self.restore)

        self.ui.button_save_data.clicked.connect(self.saveCurrentInvestment)

        # read only text edits
        self.readOnlyTextEdits: List[QTextEdit] = [self.ui.text_price_per_square_meter,
                                                   self.ui.text_own_contribution_percent,
                                                   self.ui.text_broker_margin_percent,
                                                   self.ui.text_notary_margin_percent,
                                                   self.ui.text_tax_percent, self.ui.text_other_costs_percent,
                                                   self.ui.text_renovation_percent, self.ui.text_entry_cost,
                                                   self.ui.text_credit,
                                                   self.ui.text_bank_contribution_percent,
                                                   self.ui.text_monthly_installment,
                                                   self.ui.text_monthly_installment_capital_part,
                                                   self.ui.text_monthly_installment_interest_part,
                                                   self.ui.text_total_credit_cost,
                                                   self.ui.text_rent_income_min_year,
                                                   self.ui.text_rent_income_max_year, self.ui.text_rent_income_max_year,
                                                   self.ui.text_income_earned_year,
                                                   self.ui.text_rent_tax_year, self.ui.text_property_tax_month,
                                                   self.ui.text_electricity_year, self.ui.text_gas_year,
                                                   self.ui.text_water_year,
                                                   self.ui.text_internet_year, self.ui.text_other_costs_year,
                                                   self.ui.text_total_costs_month, self.ui.text_total_costs_year,
                                                   self.ui.text_rent_gain_loss_month, self.ui.text_rent_gain_loss_year,
                                                   self.ui.text_invested_vs_purchase,
                                                   self.ui.text_rent_income_min_percent,
                                                   self.ui.text_rent_income_max_percent,
                                                   self.ui.text_income_earned_percent, self.ui.text_rent_tax_percent,
                                                   self.ui.text_property_tax_percent, self.ui.text_electricity_percent,
                                                   self.ui.text_gas_percent, self.ui.text_water_percent, self.ui.text_internet_percent,
                                                   self.ui.text_other_costs_percent_2]

        self.editableTextEditsNumeric: List[QTextEdit] = [self.ui.text_purchase_price,
                                                          self.ui.text_area,
                                                          self.ui.text_estimated_value,
                                                          self.ui.text_own_contribution,
                                                          self.ui.text_broker_margin,
                                                          self.ui.text_notary_margin,
                                                          self.ui.text_tax,
                                                          self.ui.text_other_costs,
                                                          self.ui.text_renovation
                                                          ]

        self.editableTextEdits: List[QTextEdit] = [self.ui.text_investment_name,
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

        self.framesToRemoveBorder = [self.ui.frame_label_and_text_investment_name,
                                     self.ui.frame_label_and_text_purchase_price,
                                     self.ui.frame_label_and_text_renovation, self.ui.frame_label_and_text_tax,
                                     self.ui.frame_label_and_text_area,
                                     self.ui.frame_label_and_text_credit, self.ui.frame_label_and_text_address_city,
                                     self.ui.frame_label_and_text_address_street,
                                     self.ui.frame_label_and_text_bank_contribution_percent,
                                     self.ui.frame_label_and_text_broker_margin,
                                     self.ui.frame_label_and_text_description,
                                     self.ui.frame_label_and_text_entry_cost,
                                     self.ui.frame_label_and_text_estimated_value,
                                     self.ui.frame_label_and_text_finish_date,
                                     self.ui.frame_label_and_text_interest_rate,
                                     self.ui.frame_label_and_text_invested_vs_purchase,
                                     self.ui.frame_label_and_text_monthly_installment,
                                     self.ui.frame_label_and_text_monthly_installment_capital_part,
                                     self.ui.frame_label_and_text_own_contribution,
                                     self.ui.frame_label_and_text_notary_margin,
                                     self.ui.frame_label_and_text_other_costs,
                                     self.ui.frame_label_and_text_repayment_period,
                                     self.ui.frame_label_and_text_text_monthly_installment_interest_part,
                                     self.ui.frame_label_and_text_credit_credit_insurance_per_month,
                                     self.ui.frame_label_and_text_total_credit_cost,
                                     self.ui.frame_rent_data_income,
                                     self.ui.frame_label_and_text_rent_income_min,
                                     self.ui.frame_label_and_text_rent_income_max,
                                     self.ui.frame_label_and_text_income_earned,
                                     self.ui.frame_rent_data_cost,
                                     self.ui.frame_label_and_text_rent_tax,
                                     self.ui.frame_label_and_text_property_tax,
                                     self.ui.frame_label_and_text_tax_electricity,
                                     self.ui.frame_label_and_text_gas,
                                     self.ui.frame_label_and_text_water,
                                     self.ui.frame_label_and_text_internet,
                                     self.ui.frame_label_and_text_other_costs_2,
                                     self.ui.frame_label_and_text_total_costs,
                                     self.ui.frame_label_and_text_rent_gain_loss,
                                     self.ui.frame_investment_assessment_data,
                                     self.ui.frame_label_and_text_own_capital_return_2,
                                     self.ui.frame_label_and_text_own_capital_return,
                                     self.ui.frame_label_and_text_total_return_time,
                                     self.ui.frame_label_and_text_return_rate_1,
                                     self.ui.frame_label_and_text_return_rate_2]

        self.labels = [self.ui.label_11, self.ui.label_68, self.ui.label_69, self.ui.label_70, self.ui.label_14,
                       self.ui.label_15, self.ui.label_16, self.ui.label_17, self.ui.label_18, self.ui.label_19,
                       self.ui.label_20, self.ui.label, self.ui.label_2, self.ui.label_3, self.ui.label_4,
                       self.ui.label_5, self.ui.label_6, self.ui.label_7, self.ui.label_8, self.ui.label_9,
                       self.ui.label_10,
                       self.ui.label_20, self.ui.label_21, self.ui.label_22, self.ui.label_23, self.ui.label_28,
                       self.ui.label_29, self.ui.label_24, self.ui.label_25, self.ui.label_37, self.ui.label_38,
                       self.ui.label_39, self.ui.label_30, self.ui.label_31, self.ui.label_32, self.ui.label_33,
                       self.ui.label_34, self.ui.label_35, self.ui.label_36, self.ui.label_47, self.ui.label_48,
                       self.ui.label_49, self.ui.label_50, self.ui.label_51, self.ui.label_52]
        self.labels = list(
            map(setLabelStyleSheet, self.labels))

        self.editableTextEditsNumeric = list(map(setTextEditAlignmentCenter, self.editableTextEditsNumeric))
        self.editableTextEdits = list(map(setTextEditAlignmentCenter, self.editableTextEdits))

        for readOnlyFrame in self.readOnlyTextEdits:
            readOnlyFrame.setReadOnly(True)

        self.readOnlyTextEdits = setDarkerBackgroundForStaticTextEdits(self.readOnlyTextEdits)

        self.notesStr: List[str] = []
        self.notes: List[Note] = []

        self.frameHeight = 40
        self.targetFrameHeight = 300
        self.slideAnimationDuration = 500

        self.ui.frame_information_data.setVisible(False)
        self.ui.frame_rent_data.setVisible(False)
        self.ui.frame_investment_assessment_data.setVisible(False)
        self.ui.frame_own_contribution_credit_inner.setVisible(False)
        self.ui.scrollArea_notes.setVisible(False)
        self.ui.frame_add_note_button.setVisible(False)

        self.decreaseFrameHeights(50)

        # animation section

        self.informationSlideAnimation = None
        self.ui.button_information.clicked.connect(self.slideInformation)
        self.creditSlideAnimation = None

        self.rentSlideAnimation = None
        self.ui.button_rent.clicked.connect(self.slideRent)
        self.investmentAssessmentSlideAnimation = None
        self.ui.button_investment_assessment.clicked.connect(self.slideInvestmentAssessment)
        self.ownContributionCreditSlideAnimation = None
        self.ui.button_own_contribution_credit.clicked.connect(self.slideOwnContributionCredit)
        self.notesSlideAnimation = None
        self.ui.button_notes.clicked.connect(self.slideNotes)

        # left buttons section
        self.ui.button_home_page.clicked.connect(lambda: self.mainMenu(PageTypes.homePage))
        self.ui.button_new_investment.clicked.connect(lambda: self.addNewInvestment())

        self.framesToRemoveBorder = removeExcessiveBorders(self.framesToRemoveBorder)

        self.ui.scrollArea_investments_home_page.setWidgetResizable(True)
        self.homePageInvestments = self.loadInvestments()
        self.ui.all_pages.setCurrentWidget(self.ui.home_page)

        self.ui.button_options.setVisible(False)

        self.editableTextEdits = list(
            map(lambda qObject: changeObjectFontSize(qObject, 17), self.editableTextEdits))
        self.editableTextEditsNumeric = list(
            map(lambda qObject: changeObjectFontSize(qObject, 17), self.editableTextEditsNumeric))
        self.readOnlyTextEdits = list(
            map(lambda qObject: changeObjectFontSize(qObject, 17), self.readOnlyTextEdits))
        self.labels = list(
            map(lambda qObject: changeObjectFontSize(qObject, 17), self.labels))
        print(self.labels)

        # self.options = Options()
        # # options
        # self.ui.button_options.clicked.connect(lambda: self.ui.all_pages.setCurrentWidget(self.ui.options_page))
        # self.ui.comboBox_precision.highlighted.connect(self.setPrecisionToInvestments)
        icon = QIcon("./icons/app_icon.png")
        self.setWindowIcon(icon)

        self.show()

    def setPrecisionToInvestments(self, index):
        self.options.setPrecision(int(self.ui.comboBox_precision.currentText()))
        self.investments = dict()

    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:

        isChanged = False
        fontSize = None
        print(self.width())
        mainCharacteristicsFrameMinHeight = None
        currentlyOpenedFrameMinHeight = None
        if self.width() > 1200 and self.ui.text_area.fontInfo().pointSize() is not 20:
            fontSize = 20
            isChanged = True
            mainCharacteristicsFrameMinHeight = 180
            currentlyOpenedFrameMinHeight = 100

        elif self.width() < 1080 and self.ui.text_area.fontInfo().pointSize() is not 15:
            fontSize = 15
            isChanged = True
            mainCharacteristicsFrameMinHeight = 120
            currentlyOpenedFrameMinHeight = 70
        else:
            fontSize = 17
            mainCharacteristicsFrameMinHeight = 140
            currentlyOpenedFrameMinHeight = 84
            if self.ui.text_area.fontInfo().pointSize() is 20:
                isChanged = True

        self.ui.label.font()

        if isChanged:
            self.ui.frame_main_characteristics.setMinimumHeight(mainCharacteristicsFrameMinHeight)
            self.ui.frame_currently_opened.setMinimumHeight(currentlyOpenedFrameMinHeight)
            self.editableTextEdits = list(
                map(lambda qObject: changeObjectFontSize(qObject, fontSize), self.editableTextEdits))
            self.editableTextEditsNumeric = list(
                map(lambda qObject: changeObjectFontSize(qObject, fontSize), self.editableTextEditsNumeric))
            self.readOnlyTextEdits = list(
                map(lambda qObject: changeObjectFontSize(qObject, fontSize), self.readOnlyTextEdits))
            self.labels = list(
                map(lambda qObject: changeObjectFontSize(qObject, fontSize), self.labels))

    def closeEvent(self, event: PySide6.QtGui.QCloseEvent) -> None:

        if all(self.isInvestmentSaved.values()):
            super(MainWindow, self).closeEvent(event)
        else:
            unsavedInvestmentsDialog = CloseProgramDialog(self)

            unsavedInvestmentsDialog.exec()
            dialogResult = unsavedInvestmentsDialog.result()
            if dialogResult == QDialog.Accepted:
                self.investments, self.isInvestmentSaved = saveAllInvestments(self.investments, self.isInvestmentSaved)
                super(MainWindow, self).closeEvent(event)
            elif dialogResult == QDialog.Rejected:
                super(MainWindow, self).closeEvent(event)
            elif dialogResult == 2:
                event.ignore()
            else:
                raise NotImplementedError

    def decreaseFrameHeights(self, minHeight):

        self.ui.frame_information.setMinimumHeight(minHeight)
        self.ui.frame_rent.setMinimumHeight(minHeight)

        self.ui.frame_own_contribution_credit.setMinimumHeight(minHeight)
        self.ui.frame_investment_assessment.setMinimumHeight(minHeight)
        self.ui.frame_notes.setMinimumHeight(minHeight)

        self.ui.frame_information.resize(self.ui.frame_information.width(), minHeight)
        self.ui.frame_rent.resize(self.ui.frame_rent.width(), minHeight)
        self.ui.frame_own_contribution_credit.resize(self.ui.frame_own_contribution_credit.width(), minHeight)
        self.ui.frame_investment_assessment.resize(self.ui.frame_investment_assessment.width(), minHeight)
        self.ui.frame_notes.resize(self.ui.frame_notes.width(), minHeight)

    def mainMenu(self, pageType: PageTypes):

        if pageType == PageTypes.homePage:
            self.homePageInvestments = clearHomePageWidgetsAndLoadNewWidgets(self.homePageInvestments, self)
            self.ui.all_pages.setCurrentWidget(self.ui.home_page)

    def slideInformation(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_information.height() < self.targetFrameHeight:
            isSlided = False
            afterAnimationHeight = 440
            actualHeight = self.frameHeight
            self.ui.frame_information_data.setVisible(True)

        else:
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 440
            self.ui.frame_information_data.setVisible(False)

        self.informationSlideAnimation = QPropertyAnimation(self.ui.frame_information,
                                                            b'minimumHeight')
        self.informationSlideAnimation.setDuration(self.slideAnimationDuration)
        self.informationSlideAnimation.setStartValue(actualHeight)
        self.informationSlideAnimation.setEndValue(afterAnimationHeight)
        self.informationSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.informationSlideAnimation.start()

    def slideRent(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_rent.height() < self.targetFrameHeight:
            isSlided = False
            afterAnimationHeight = 820
            actualHeight = self.frameHeight
            self.ui.frame_rent_data.setVisible(True)
        else:
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 820
            self.ui.frame_rent_data.setVisible(False)

        self.rentSlideAnimation = QPropertyAnimation(self.ui.frame_rent,
                                                     b'minimumHeight')
        self.rentSlideAnimation.setDuration(self.slideAnimationDuration)
        self.rentSlideAnimation.setStartValue(actualHeight)
        self.rentSlideAnimation.setEndValue(afterAnimationHeight)
        self.rentSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.rentSlideAnimation.start()

    def slideInvestmentAssessment(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_investment_assessment.height() < self.targetFrameHeight:
            isSlided = False
            afterAnimationHeight = 320
            actualHeight = self.frameHeight
            self.ui.frame_investment_assessment_data.setVisible(True)
        else:
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 320
            self.ui.frame_investment_assessment_data.setVisible(False)

        self.investmentAssessmentSlideAnimation = QPropertyAnimation(self.ui.frame_investment_assessment,
                                                                     b'minimumHeight')
        self.investmentAssessmentSlideAnimation.setDuration(self.slideAnimationDuration)
        self.investmentAssessmentSlideAnimation.setStartValue(actualHeight)
        self.investmentAssessmentSlideAnimation.setEndValue(afterAnimationHeight)
        self.investmentAssessmentSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.investmentAssessmentSlideAnimation.start()

    # noinspection DuplicatedCode
    def slideOwnContributionCredit(self):
        isSlided = False
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_own_contribution_credit.height() < self.targetFrameHeight:
            isSlided = False
            afterAnimationHeight = 600
            actualHeight = self.frameHeight
            self.ui.frame_own_contribution_credit_inner.setVisible(True)
        else:  # after slide
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 600
            self.ui.frame_own_contribution_credit_inner.setVisible(False)

        self.ownContributionCreditSlideAnimation = QPropertyAnimation(self.ui.frame_own_contribution_credit,
                                                                      b'minimumHeight')
        self.ownContributionCreditSlideAnimation.setDuration(self.slideAnimationDuration)
        self.ownContributionCreditSlideAnimation.setStartValue(actualHeight)
        self.ownContributionCreditSlideAnimation.setEndValue(afterAnimationHeight)
        self.ownContributionCreditSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.ownContributionCreditSlideAnimation.start()

    def slideNotes(self):
        afterAnimationHeight = None
        actualHeight = None
        if self.ui.frame_notes.height() < self.targetFrameHeight:
            isSlided = False
            afterAnimationHeight = 500
            actualHeight = self.frameHeight
            self.ui.scrollArea_notes.setVisible(True)
            self.ui.frame_add_note_button.setVisible(True)
        else:
            isSlided = True
            afterAnimationHeight = self.frameHeight
            actualHeight = 500
            self.ui.scrollArea_notes.setVisible(False)
            self.ui.frame_add_note_button.setVisible(False)

        self.notesSlideAnimation = QPropertyAnimation(self.ui.frame_notes,
                                                      b'minimumHeight')
        self.notesSlideAnimation.setDuration(self.slideAnimationDuration)
        self.notesSlideAnimation.setStartValue(actualHeight)
        self.notesSlideAnimation.setEndValue(afterAnimationHeight)
        self.notesSlideAnimation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.notesSlideAnimation.start()

    def addNote(self, newNoteStr=None):

        print("new note ", newNoteStr)

        if newNoteStr is not None and newNoteStr[0] is []:
            return
        newNoteTextEdit = QTextEdit(self.ui.scrollArea_notes_contents)
        font: QFont = newNoteTextEdit.font()
        font.setPointSize(19)
        newNoteTextEdit.setFont(font)
        noteIndex = None
        if newNoteStr is None:
            newNoteStr = ""
            self.currentInvestment.notes().append(newNoteStr)
            noteIndex = len(self.currentInvestment.notes()) - 1
        else:
            noteIndex = newNoteStr[1]
            newNoteStr = newNoteStr[0]
            newNoteTextEdit.setText(newNoteStr)
        newNoteTextEdit.textChanged.connect(
            lambda: self.currentInvestment.setNote(noteIndex, newNoteTextEdit.toPlainText()))
        investmentId = self.currentInvestment.id
        frame = self.investmentTabs[investmentId]
        label: QLabel = frame.findChild(QLabel)
        newNoteTextEdit.textChanged.connect(lambda: self.changeOneIcon(label, investmentId))
        newNoteTextEdit.setMinimumHeight(140)

        frameWithNote = QFrame(self.ui.scrollArea_notes_contents)
        frameWithNote.setObjectName("note_" + str(noteIndex) + "_frame")
        frameWithNoteLayout = QHBoxLayout(frameWithNote)
        frameWithNoteLayout.setObjectName("note_" + str(noteIndex) + "_layout")
        frameWithNote.setLayout(frameWithNoteLayout)
        deleteButton = QPushButton("x", frameWithNote)
        frameWithNoteLayout.addWidget(deleteButton)
        frameWithNoteLayout.addWidget(newNoteTextEdit)

        newNote = Note(newNoteStr, newNoteTextEdit, frameWithNote, deleteButton, noteIndex, self.notesStr, self.notes)

        deleteButton.clicked.connect(newNote.deleteNote)

        self.ui.scrollArea_notes_contents_layout.addWidget(frameWithNote)
        self.notesStr.append(newNote.noteStr)
        self.notes.append(newNote)

    def addNotes(self):
        print("self.notes ", self.notes)
        if len(self.notes) > 0:
            try:
                self.notes.remove(None)
            except:
                pass
            finally:
                list(map(lambda note: note.deleteNote(), self.notes))
                self.notes = []
        print(self.notes)

        print("---------------------------")
        print(self.currentInvestment)
        print(self.currentInvestment.notes())

        print(list(range(0, len(self.currentInvestment.notes()))))

        if len(self.currentInvestment.notes()) > 0:
            list(
                map(self.addNote,
                    zip(self.currentInvestment.notes(), list(range(0, len(self.currentInvestment.notes()))))))

    def removeNote(self):

        pass

    def restore(self):
        global SHOW_MAXIMIZED
        if SHOW_MAXIMIZED:
            SHOW_MAXIMIZED = False
            self.showNormal()
        else:
            SHOW_MAXIMIZED = True
            self.showFullScreen()

    def loadAndShowInvestment(self, investmentId):

        print("ID: ", investmentId, " | ", self.investments.keys())

        if investmentId in self.investments.keys():
            self.showInvestmentOnMainPage(self.investments[investmentId], self.investmentTabs[investmentId])
        else:
            investment = getInvestmentById(investmentId, self)
            self.addNewInvestment(investment)

    def addInvestmentWidgetToHomePage(self, investmentIdAndName):
        investmentId: int = int(investmentIdAndName[0])
        name = investmentIdAndName[1]
        time = investmentIdAndName[2]
        print("NAMEEEEEE ", name)
        investmentHomePageWidget = HomePageInvestment(self.ui.scrollAreaContents_investments_home_page)
        investmentHomePageWidget.buttonInvestmentName.setText(name)
        investmentHomePageWidget.buttonInvestmentName.clicked.connect(lambda: self.loadAndShowInvestment(investmentId))
        investmentHomePageWidget.buttonInvestmentTime.setText(time)
        investmentHomePageWidget.buttonInvestmentTime.clicked.connect(lambda: self.loadAndShowInvestment(investmentId))
        investmentHomePageWidget.buttonDeleteInvestment.clicked.connect(lambda:
                                                                        investmentHomePageWidget.deleteInvestmentAndWidget(
                                                                            investmentId))
        self.ui.investments_home_page_layout.addWidget(investmentHomePageWidget)
        investmentHomePageWidget.show()
        return investmentHomePageWidget

    def loadInvestments(self):
        loadedInvestments = getInvestments()
        print(loadedInvestments)
        return list(map(self.addInvestmentWidgetToHomePage, loadedInvestments))

    def closeInvestment(self, investment: Investment):

        def deleteInvestmentTab(innerId):
            investmentFrame = self.investmentTabs[innerId]
            investmentFrame.hide()
            investmentFrame.deleteLater()

        id = investment.id
        if self.isInvestmentSaved[id] is False:
            # otworz okienko i zapytaj sie o zapisanie pliku
            unsavedInvestmentDialog = UnsavedDialog(self)
            dialogResult: QDialog.DialogCode = unsavedInvestmentDialog.exec()
            if dialogResult == QDialog.Accepted:
                self.saveCurrentInvestment()
            elif dialogResult == QDialog.Rejected:
                pass
            else:
                raise NotImplementedError

        deleteInvestmentTab(id)
        del self.investments[id]
        del self.investmentTabs[id]
        del self.isInvestmentSaved[id]
        del investment

        for nextInvestment in self.investments.values():
            self.showInvestmentOnMainPage(nextInvestment, self.investmentTabs[nextInvestment.id])
            break

        if len(self.investments.values()) == 0:
            self.homePageInvestments = clearHomePageWidgetsAndLoadNewWidgets(self.homePageInvestments, self)
            self.ui.all_pages.setCurrentWidget(self.ui.home_page)

    def addNewInvestment(self, newInvestment=None):

        global tabCounter
        global buttonCounter
        global layoutCounter
        global labelCounter

        if newInvestment is None:
            newInvestment = Investment(self.ui, None)

        self.investments[newInvestment.id] = newInvestment

        self.isInvestmentSaved[newInvestment.id] = False

        # add frame to tab bar
        investmentFrame = QFrame(self.ui.scrollAreaContents_currently_opened)
        investmentFrame.setStyleSheet(frameStyleSheet)
        investmentFrame.setObjectName("Tab_" + str(tabCounter))
        investmentFrame.setMaximumHeight(50)

        fontSize = 18

        tabCounter += 1
        investmentFrameLayout = QHBoxLayout(investmentFrame)
        investmentFrameLayout.setObjectName("layout_investment_" + str(layoutCounter))
        investmentFrameLayout.setContentsMargins(4, 4, 4, 4)
        layoutCounter += 1
        closeFrameButton = QPushButton("x", investmentFrame)
        closeFrameButton.setObjectName("Close_button" + str(buttonCounter))
        font: QFont = closeFrameButton.font()
        font.setPointSize(fontSize)
        closeFrameButton.setFont(font)
        buttonCounter += 1
        closeFrameButton.setMaximumWidth(20)
        openInvestmentButton = QPushButton("Inwestycja nienazwana", investmentFrame)
        openInvestmentButton.setObjectName("investment_button" + str(buttonCounter))
        font: QFont = openInvestmentButton.font()
        font.setPointSize(fontSize)
        openInvestmentButton.setFont(font)
        buttonCounter += 1
        isSavedLabel = QLabel("", investmentFrame)
        isSavedLabel.setObjectName("isSavedLabel_" + str(labelCounter))
        labelCounter += 1
        isSavedLabel.setPixmap(self.unsavedIcon)
        isSavedLabel.setStyleSheet("#" + isSavedLabel.objectName() + """{
        border: 0px solid gray;
        border-radius: 10px;
        background: rgb(255, 255, 255);
        }""")
        isSavedLabel.setMaximumHeight(40)
        isSavedLabel.setMaximumWidth(40)

        investmentFrameLayout.addWidget(closeFrameButton)
        investmentFrameLayout.addWidget(openInvestmentButton)
        investmentFrameLayout.addWidget(isSavedLabel)

        # self.investmentTabs.append(investmentFrame)
        self.investmentTabs[newInvestment.id] = investmentFrame

        openInvestmentButton.clicked.connect(lambda: self.showInvestmentOnMainPage(newInvestment, investmentFrame))
        closeFrameButton.clicked.connect(lambda: self.closeInvestment(newInvestment))

        self.ui.scrollAreaContents_currently_opened_layout.addWidget(investmentFrame)

        self.ui.all_pages.setCurrentWidget(self.ui.investment_page)

        self.showInvestmentOnMainPage(newInvestment, investmentFrame)

    def showInvestmentOnMainPage(self, investment: Investment, frameToHighlight: QFrame):

        self.currentInvestment = investment

        for frame in self.investmentTabs.values():
            if frame is frameToHighlight:
                frame.setStyleSheet(highlightedFrameStyleSheet)
                iconLabel: QLabel = frame.findChild(QLabel)
                iconLabel.setPixmap(self.unsavedIcon)
                self.isInvestmentSaved[investment.id] = False
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
        self.ui.text_own_contribution_percent.setText(investment.ownContributionPercent())
        self.ui.text_broker_margin.setText(str(investment.brokerMargin()))
        self.ui.text_broker_margin_percent.setText(
            investment.brokerMarginPercent())
        self.ui.text_notary_margin.setText(str(investment.notaryMargin()))
        self.ui.text_notary_margin_percent.setText(
            investment.notaryMarginPercent())
        self.ui.text_tax.setText(str(investment.tax()))
        self.ui.text_tax_percent.setText(investment.taxPercent())
        self.ui.text_other_costs.setText(str(investment.otherCosts()))
        self.ui.text_other_costs_percent.setText(
            investment.otherCostsPercent())
        self.ui.text_renovation.setText(str(investment.renovationCost()))
        self.ui.text_renovation_percent.setText(
            investment.renovationCostPercent())
        self.ui.text_entry_cost.setText(str(investment.entryCost()))
        self.ui.text_invested_vs_purchase.setText(str(investment.investedVsPurchasePrice()))
        self.ui.text_credit.setText(str(investment.bankCredit()))
        self.ui.text_bank_contribution_percent.setText(str(investment.bankContributionPercent()))
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
        self.ui.text_rent_gain_loss_month.setText(str(investment.gainLossPerMonth()))
        self.ui.text_rent_gain_loss_year.setText(str(investment.gainLossPerMonth() * 12) if type(
            investment.gainLossPerMonth()) is not str else noDataText)
        self.ui.label_own_capital_return_time_months.setText(str(investment.ownCapitalReturnTimeMonths()))
        self.ui.label_own_capital_return_time_years.setText(str(investment.ownCapitalReturnTimeYears()))

        self.addNotes()

    def changeOneIcon(self, investmentFrameLabel: QLabel, currentInvestmentId: int):
        # print("changeOneIcon")
        # print(investmentFrameLabel.pixmap(), " --- ", self.savedIcon)
        if self.isInvestmentSaved[currentInvestmentId] is True:
            self.isInvestmentSaved[currentInvestmentId] = False
            # print("changing !")
            investmentFrameLabel.setPixmap(self.unsavedIcon)

    def changeSaveIconMap(self, editableTextEdit: QTextEdit):
        investmentFrameLabel = self.currentInvestmentTabIconLabel
        currentInvestmentId = self.currentInvestment.id
        editableTextEdit.textChanged.connect(self.changeOneIcon(investmentFrameLabel, currentInvestmentId))
        return editableTextEdit

    def setInvestmentNameToTab(self, investmentId):
        investmentFrame: QFrame = self.investmentTabs[investmentId]
        investmentButtons = list(investmentFrame.findChildren(QPushButton))
        investmentButton = list(filter(lambda button: "investment_button" in button.objectName(), investmentButtons))[0]
        investmentButton.setText(self.investments[investmentId].title)

    def connectSetInvestmentUnsavedToEditableTextEdit(self, editableTextEdit):
        investmentFrameLabelIcon = self.investmentTabs[self.currentInvestment.id].findChild(QLabel)
        editableTextEdit.textChanged.connect(lambda: self.setInvestmentUnsaved(investmentFrameLabelIcon))
        return editableTextEdit

    def setInvestmentUnsaved(self, investmentFrameLabel: QLabel):
        if self.isInvestmentSaved[self.currentInvestment.id] is True:
            investmentFrameLabel.setPixmap(self.unsavedIcon)
            self.isInvestmentSaved[self.currentInvestment.id] = False

    def eventFilter(self, object, event):

        # if object in self.editableTextEditsNumeric and event == QEvent.
        #
        # if textEdit.toPlainText().isdigit():
        #     return False
        return True

    def captureTextEdits(self, investment):

        if self.textEditsConnected:
            # print("odlaczam")
            self.textEditsConnected = False
            # print(self.editableTextEdits)
            self.editableTextEdits = list(
                map(disconnectFunction, self.editableTextEdits))
            self.ui.button_add_note.clicked.disconnect()

        self.textEditsConnected = True

        # self.editableTextEditsNumeric = list(map(, self.editableTextEditsNumeric))

        self.currentInvestmentTabIconLabel = self.investmentTabs[investment.id].findChild(QLabel)

        self.editableTextEdits = list(map(self.changeSaveIconMap, self.editableTextEdits))
        self.editableTextEdits = list(map(self.connectSetInvestmentUnsavedToEditableTextEdit, self.editableTextEdits))

        self.ui.text_investment_name.textChanged.connect(
            lambda: investment.setTitle(self.ui.text_investment_name.toPlainText()))
        self.ui.text_investment_name.textChanged.connect(lambda: self.setInvestmentNameToTab(investment.id))
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
        self.ui.button_add_note.clicked.connect(lambda: self.addNote())

        self.updateReadOnlyTextEdits()

    def saveCurrentInvestment(self):
        if self.currentInvestment is None:
            return
        self.currentInvestment.save()
        investmentId = self.currentInvestment.id

        frame = self.investmentTabs[investmentId]
        label: QLabel = frame.findChild(QLabel)
        label.setPixmap(self.savedIcon)

        self.isInvestmentSaved[self.currentInvestment.id] = True

    def updateTextEdit(self, textEdit: QTextEdit, functionToGetData):
        data = str(functionToGetData())
        textEdit.setText(data)

    def updateReadOnlyTextEdits(self):
        self.ui.text_purchase_price.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_price_per_square_meter,
                                        self.currentInvestment.pricePerSquareMeter))
        self.ui.text_area.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_price_per_square_meter,
                                        self.currentInvestment.pricePerSquareMeter))
        self.ui.text_own_contribution.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_entry_cost, self.currentInvestment.entryCost))
        self.ui.text_broker_margin.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_entry_cost, self.currentInvestment.entryCost))
        self.ui.text_notary_margin.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_entry_cost, self.currentInvestment.entryCost))
        self.ui.text_tax.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_entry_cost, self.currentInvestment.entryCost))
        self.ui.text_other_costs.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_entry_cost, self.currentInvestment.entryCost))
        self.ui.text_renovation.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_entry_cost, self.currentInvestment.entryCost))

        self.ui.text_credit.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_monthly_installment, self.currentInvestment.monthlyInstallment))
        self.ui.text_repayment_period.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_monthly_installment, self.currentInvestment.monthlyInstallment))
        self.ui.text_interest_rate.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_monthly_installment, self.currentInvestment.monthlyInstallment))
        self.ui.text_credit.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_monthly_installment_capital_part,
                                        self.currentInvestment.monthlyInstallmentCapitalPart))
        self.ui.text_repayment_period.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_monthly_installment_capital_part,
                                        self.currentInvestment.monthlyInstallmentCapitalPart))
        self.ui.text_credit.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_monthly_installment_interest_part,
                                        self.currentInvestment.monthlyInstallmentInterestPart))
        self.ui.text_repayment_period.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_monthly_installment_interest_part,
                                        self.currentInvestment.monthlyInstallmentInterestPart))
        self.ui.text_interest_rate.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_monthly_installment_interest_part,
                                        self.currentInvestment.monthlyInstallmentInterestPart))

        self.ui.text_monthly_installment.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_credit_cost, self.currentInvestment.totalCreditCost))
        self.ui.text_credit_credit_insurance_per_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_credit_cost, self.currentInvestment.totalCreditCost))

        self.ui.text_credit_credit_insurance_per_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_credit_cost, self.currentInvestment.totalCreditCost))

        self.ui.text_purchase_price.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_credit, self.currentInvestment.bankCredit))
        self.ui.text_own_contribution.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_credit, self.currentInvestment.bankCredit))

        self.ui.text_rent_tax_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_costs_month, self.currentInvestment.costsTotalPerMonth))
        self.ui.text_property_tax_year.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_costs_month, self.currentInvestment.costsTotalPerMonth))
        self.ui.text_electricity_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_costs_month, self.currentInvestment.costsTotalPerMonth))
        self.ui.text_gas_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_costs_month, self.currentInvestment.costsTotalPerMonth))
        self.ui.text_water_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_costs_month, self.currentInvestment.costsTotalPerMonth))
        self.ui.text_internet_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_costs_month, self.currentInvestment.costsTotalPerMonth))
        self.ui.text_other_costs_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_total_costs_month, self.currentInvestment.costsTotalPerMonth))

        self.ui.text_income_earned_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_rent_gain_loss_month, self.currentInvestment.gainLossPerMonth))
        self.ui.text_total_costs_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_rent_gain_loss_month, self.currentInvestment.gainLossPerMonth))
        self.ui.text_income_earned_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_rent_gain_loss_year, self.currentInvestment.gainLossPerYear))
        self.ui.text_total_costs_month.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_rent_gain_loss_year, self.currentInvestment.gainLossPerYear))

        self.ui.text_credit.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_bank_contribution_percent,
                                        self.currentInvestment.bankContributionPercent)
        )

        self.ui.text_own_contribution.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_own_contribution_percent,
                                        self.currentInvestment.ownContributionPercent)
        )
        self.ui.text_broker_margin.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_broker_margin_percent, self.currentInvestment.brokerMarginPercent)
        )
        self.ui.text_notary_margin.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_notary_margin_percent, self.currentInvestment.notaryMarginPercent)
        )
        self.ui.text_tax.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_tax_percent, self.currentInvestment.taxPercent)
        )
        self.ui.text_other_costs.textChanged.connect(
            lambda: self.updateTextEdit(self.ui.text_other_costs_percent, self.currentInvestment.otherCostsPercent))
        self.ui.text_renovation.textChanged.connect(lambda: self.updateTextEdit(self.ui.text_renovation_percent,
                                                                                self.currentInvestment.renovationCostPercent))

        self.ui.text_entry_cost.textChanged.connect(
            (lambda: self.updateTextEdit(self.ui.label_own_capital_return_time_months,
                                         self.currentInvestment.ownCapitalReturnTimeMonths)))
        self.ui.text_rent_gain_loss_month.textChanged.connect(
            (lambda: self.updateTextEdit(self.ui.label_own_capital_return_time_months,
                                         self.currentInvestment.ownCapitalReturnTimeMonths)))
        self.ui.text_entry_cost.textChanged.connect(
            (lambda: self.updateTextEdit(self.ui.label_own_capital_return_time_months,
                                         self.currentInvestment.totalReturnTimeMonths)))
        self.ui.text_rent_gain_loss_month.textChanged.connect(
            (lambda: self.updateTextEdit(self.ui.label_own_capital_return_time_months,
                                         self.currentInvestment.totalReturnTimeMonths)))
        self.ui.text_credit.textChanged.connect(
            (lambda: self.updateTextEdit(self.ui.label_own_capital_return_time_months,
                                         self.currentInvestment.totalReturnTimeMonths)))

        self.ui.text_entry_cost.textChanged.connect(lambda: self.updateTextEdit(self.ui.text_invested_vs_purchase,
                                                                                self.currentInvestment.investedVsPurchasePrice))

        self.ui.text_purchase_price.textChanged.connect(lambda: self.updateTextEdit(self.ui.text_invested_vs_purchase,
                                                                                    self.currentInvestment.investedVsPurchasePrice))



        self.ui.text_rent_income_min_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_rent_income_min_year, self.currentInvestment.rentIncomeMinPerYear
        ))
        self.ui.text_rent_income_max_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_rent_income_max_year, self.currentInvestment.rentIncomeMaxPerYear
        ))
        self.ui.text_income_earned_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_income_earned_year, self.currentInvestment.rentIncomeReceivedPerYear
        ))
        self.ui.text_rent_tax_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_rent_tax_year, self.currentInvestment.rentTaxPerYear
        ))
        self.ui.text_property_tax_year.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_property_tax_month, self.currentInvestment.propertyTaxPerMonth
        ))
        self.ui.text_electricity_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_electricity_year, self.currentInvestment.electricityPerYear
        ))
        self.ui.text_water_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_water_year, self.currentInvestment.waterPerYear
        ))
        self.ui.text_gas_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_gas_year, self.currentInvestment.gasPerYear
        ))
        self.ui.text_internet_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_internet_year, self.currentInvestment.internetPerYear
        ))
        self.ui.text_other_costs_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_other_costs_year, self.currentInvestment.otherPerYear
        ))
        self.ui.text_total_costs_month.textChanged.connect(lambda: self.updateTextEdit(
            self.ui.text_total_costs_year, self.currentInvestment.costsTotalPerYear
        ))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    sys.exit(app.exec())
