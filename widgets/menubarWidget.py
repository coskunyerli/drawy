from PySide2 import QtWidgets, QtCore, QtGui


class ColorButton(QtWidgets.QPushButton):
    def __init__(self, parent):
        super(ColorButton, self).__init__("", parent)
        self.__currentColor = QtGui.QColor()
        self.setFixedSize(QtCore.QSize(32, 32))
        self.setCheckable(True)

    def setColor(self, color):
        self.__currentColor = color
        self.setStyleSheet(f"ColorButton{{background-color: {color.name()}; border-radius:16px;}}")

    def getColor(self):
        return self.__currentColor


class MenuBarWidget(QtWidgets.QFrame):
    brushSizeChanged = QtCore.Signal(int)
    currentColorChanged = QtCore.Signal(QtGui.QColor)
    clearButtonClicked = QtCore.Signal()
    saveButtonClicked = QtCore.Signal()
    loadButtonClicked = QtCore.Signal()

    def __init__(self, parent = None):
        super(MenuBarWidget, self).__init__(parent)
        self.mainLayout = QtWidgets.QHBoxLayout(self)
        # self.mainLayout.setContentsMargins(0, 0, 0, 0)

        self.brushSizeLabel = QtWidgets.QLabel("Brush Size:", self)
        self.brushSizeSlider = QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
        self.brushSizeSlider.setMinimum(1)
        self.brushSizeSlider.setMaximum(50)
        self.brushSizeSlider.setValue(5)
        self.brushSizeSlider.valueChanged.connect(self.brushSizeChanged)

        self.selectedColorLabel = QtWidgets.QLabel("Color:", self)
        self.colorButton = ColorButton(self)
        self.colorButton.setColor(QtGui.QColor("black"))

        self.colorButton6 = ColorButton(self)
        self.colorButton6.setColor(QtGui.QColor("white"))

        self.colorButton1 = ColorButton(self)
        self.colorButton1.setColor(QtGui.QColor("#00aaff"))

        self.colorButton2 = ColorButton(self)
        self.colorButton2.setColor(QtGui.QColor("#ff616b"))

        self.colorButton3 = ColorButton(self)
        self.colorButton3.setColor(QtGui.QColor("#ffd761"))

        self.colorButton4 = ColorButton(self)
        self.colorButton4.setColor(QtGui.QColor("#ffa061"))

        self.colorButton5 = ColorButton(self)
        self.colorButton5.setColor(QtGui.QColor("#f761ff"))

        self.eraseButton = QtWidgets.QPushButton("Erase", self)
        self.eraseButton.setCheckable(True)
        self.clearButton = QtWidgets.QPushButton("Clear", self)
        self.clearButton.clicked.connect(self.clearButtonClicked)

        self.saveButton = QtWidgets.QPushButton("Save", self)
        self.saveButton.clicked.connect(self.saveButtonClicked)

        self.loadButton = QtWidgets.QPushButton("Load", self)
        self.loadButton.clicked.connect(self.loadButtonClicked)

        self.buttonGroup = QtWidgets.QButtonGroup(self)
        self.buttonGroup.addButton(self.colorButton)
        self.buttonGroup.addButton(self.colorButton1)
        self.buttonGroup.addButton(self.colorButton2)
        self.buttonGroup.addButton(self.colorButton3)
        self.buttonGroup.addButton(self.colorButton4)
        self.buttonGroup.addButton(self.colorButton5)
        self.buttonGroup.addButton(self.colorButton6)
        self.buttonGroup.addButton(self.eraseButton, 0)

        self.buttonGroup.buttonClicked.connect(self.colorButtonClicked)

        self.mainLayout.setSpacing(8)
        self.mainLayout.addWidget(self.brushSizeLabel)
        self.mainLayout.addWidget(self.brushSizeSlider)
        self.mainLayout.addWidget(self.selectedColorLabel)
        self.mainLayout.addWidget(self.colorButton)
        self.mainLayout.addWidget(self.colorButton6)
        self.mainLayout.addWidget(self.colorButton1)
        self.mainLayout.addWidget(self.colorButton2)
        self.mainLayout.addWidget(self.colorButton3)
        self.mainLayout.addWidget(self.colorButton4)
        self.mainLayout.addWidget(self.colorButton5)
        self.mainLayout.addWidget(self.eraseButton)
        self.mainLayout.addWidget(self.clearButton)
        self.mainLayout.addWidget(self.saveButton)
        self.mainLayout.addWidget(self.loadButton)

        self.colorButton6.setChecked(True)

    def colorButtonClicked(self, button):
        id = self.buttonGroup.id(button)
        if id == 0:
            self.currentColorChanged.emit(QtGui.QColor())
        else:
            self.currentColorChanged.emit(button.getColor())
