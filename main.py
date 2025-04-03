from PySide2 import QtCore, QtGui, QtWidgets
from widgets.paintCanvas import PaintCanvas
from widgets.menubarWidget import MenuBarWidget
import sys


class PaintApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Drawy")
        self.resize(1920, 1080)
        self.canvas = PaintCanvas()
        self.menubarWidget = MenuBarWidget()
        self.menubarWidget.brushSizeChanged.connect(self.brushSizeChanged)
        self.menubarWidget.clearButtonClicked.connect(self.clearButtonClicked)
        self.menubarWidget.currentColorChanged.connect(self.onCurrentColorChanged)
        self.menubarWidget.saveButtonClicked.connect(self.onSaveClicked)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.addWidget(self.menubarWidget)
        self.mainLayout.addWidget(self.canvas)

        self.mainLayout.setStretch(1, 1)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(self.mainLayout)
        self.setCentralWidget(central_widget)

    def choose_color(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.canvas.set_pen_color(color)

    def brushSizeChanged(self, size):
        self.canvas.set_pen_size(size)

    def onSaveClicked(self):
        self.canvas.save_canvas()

    def clearButtonClicked(self):
        self.canvas.clear_canvas()

    def onCurrentColorChanged(self, color):
        self.canvas.set_pen_color(color)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    with open("resource/darkMode.qss") as f:
        qssString = f.read()
        app.setStyleSheet(qssString)

    window = PaintApp()
    window.show()
    sys.exit(app.exec_())
