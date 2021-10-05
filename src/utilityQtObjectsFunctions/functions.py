from typing import List, Dict

from PySide6.QtWidgets import QFrame, QTextEdit

from src.investmentData.k1 import Investment

noBorderFrameStyleSheetTemplate = """{
        border: 0px solid gray;
        border-radius: 10px;
        background: rgb(207, 206, 209);
        }"""


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
