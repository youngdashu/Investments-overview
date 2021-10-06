from typing import List, Dict

from PySide6.QtWidgets import QFrame, QTextEdit, QPlainTextEdit, QLineEdit

from src.gui.homePageInvestment import HomePageInvestment
from src.investmentData.investment import Investment, getInvestments

noBorderFrameStyleSheetTemplate = """{
        border: 0px solid gray;
        border-radius: 10px;
        background: rgb(207, 206, 209);
        }"""

wrongTextEditStyleSheet = """QTextEdit{
    background: rgb(184, 99, 101);
}
"""

correctTextEditStyleSheet = """QTextEdit{
    background: rgb(207, 206, 209);
    }
"""

darkerStyleSheet = """QTextEdit{
    background: rgb(197, 196, 199);
}
"""


def setProperStyleSheet(frame: QFrame):
    frame.setStyleSheet("#" + frame.objectName() + noBorderFrameStyleSheetTemplate)
    return frame


def removeExcessiveBorders(frames: List[QFrame]):
    return list(map(setProperStyleSheet, frames))


def disconnectFunction(editableTextEdit):
    editableTextEdit.textChanged.disconnect()
    return editableTextEdit


def saveAllInvestments(investments: Dict[int, Investment], isSaved: Dict[int, bool]):
    def saveInvestment(investment: Investment):
        if isSaved[investment.id] is False:
            investment.save()
            isSaved[investment.id] = True
        return investment

    return dict(zip(investments, map(saveInvestment, investments.values()))), isSaved


def connectEventFilter(textEdit: QTextEdit):
    textEdit.installEventFilter(textEdit)
    return textEdit


def setValidators(textEditNumbers: List[QLineEdit]):
    pass
    # textEditNumbers[0].va


def setDarkerBackgroundForStaticTextEdits(staticTextEdits: List[QTextEdit]):
    def setStyleSheet(textEdit):
        textEdit.setStyleSheet(darkerStyleSheet)
        return textEdit

    return list(map(setStyleSheet, staticTextEdits))


def clearHomePageWidgetsAndLoadNewWidgets(homePageInvestments: List[HomePageInvestment], app):
    homePageInvestments = list(map(lambda widget: widget.destroy(), homePageInvestments))
    homePageInvestments = app.loadInvestments()
    return homePageInvestments
