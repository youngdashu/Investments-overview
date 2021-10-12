
def changeObjectFontSize(qObject, size):
    font = qObject.font()
    font.setPointSize(size)
    qObject.setFont(font)
    return qObject



