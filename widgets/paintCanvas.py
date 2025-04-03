from PySide2 import QtCore, QtWidgets, QtGui


class PaintCanvas(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGBA8888)
        # self.pixmap.fill(QtCore.Qt.white)
        self.last_point = None
        self.pen_color = QtCore.Qt.white
        self.pen_size = 5
        self.setCursor(QtCore.Qt.BlankCursor)
        self.setTabletTracking(True)
        self.setMouseTracking(True)
        self.paper_style = "grid"
        self.__hasTableEvent = False
        self.__backgroundColor = QtGui.QColor("#202020")


    def set_pen_color(self, color):
        if color.isValid() is False:
            color = QtGui.QColor(self.__backgroundColor)
        self.pen_color = color

    def set_pen_size(self, size):
        self.pen_size = size
        self.update()

    def tabletEvent(self, event):
        self.__hasTableEvent = True
        super().tabletEvent(event)
        if event.type() == QtCore.QEvent.TabletPress:
            self.last_point = event.pos()
        elif event.type() == QtCore.QEvent.TabletMove:
            if self.last_point is not None:
                painter = QtGui.QPainter(self.image)
                painter.setRenderHint(QtGui.QPainter.Antialiasing, True)

                pen = QtGui.QPen(painter.background(), self.pen_size, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap,
                                 QtCore.Qt.RoundJoin)
                painter.setPen(pen)
                painter.drawLine(self.last_point, event.pos())
                self.last_point = event.pos()
        elif event.type() == QtCore.QEvent.TabletRelease:
            self.last_point = None

        self.__hasTableEvent = False
        self.update()

    # def mousePressEvent(self, event):
    #     if event.button() == QtCore.Qt.LeftButton and self.__hasTableEvent is False:
    #         self.last_point = event.pos()
    #
    # def mouseMoveEvent(self, event):
    #     if self.last_point is not None and self.__hasTableEvent is False:
    #         painter = QtGui.QPainter(self.image)
    #         painter.setRenderHint(QtGui.QPainter.Antialiasing, True)
    #         pen = QtGui.QPen(self.pen_color, self.pen_size, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap,
    #                          QtCore.Qt.RoundJoin)
    #         painter.setPen(pen)
    #         painter.drawLine(self.last_point, event.pos())
    #         self.last_point = event.pos()
    #     self.update()
    #
    # def mouseReleaseEvent(self, event):
    #     if event.button() == QtCore.Qt.LeftButton and self.__hasTableEvent is False:
    #         self.last_point = None

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        cursorPos = self.mapFromGlobal(QtGui.QCursor.pos())


        painter.fillRect(self.rect(), QtGui.QBrush(self.__backgroundColor))
        self.drawLines(painter)
        painter.drawImage(0, 0, self.image)
        painter.setPen(QtGui.QPen(QtGui.QColor(self.pen_color)))
        painter.drawRoundedRect(
                QtCore.QRect(cursorPos - QtCore.QPoint(self.pen_size / 2.0, self.pen_size / 2.0),
                             QtCore.QSize(self.pen_size, self.pen_size)),
                self.pen_size, self.pen_size)

    def drawLines(self, painter):
        painter.save()
        pen = painter.pen()
        pen.setColor(QtGui.QColor("#404040"))
        painter.setPen(pen)
        if self.paper_style == "lined":
            for y in range(20, self.height(), 20):
                painter.drawLine(0, y, self.width(), y)
        elif self.paper_style == "grid":
            for x in range(20, self.width(), 20):
                for y in range(20, self.height(), 20):
                    painter.drawRect(x, y, 20, 20)
        elif self.paper_style == "dotted":
            for x in range(20, self.width(), 30):
                for y in range(20, self.height(), 30):
                    painter.drawPoint(x, y)
        painter.restore()

    def clear_canvas(self):
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGBA8888)
        print(list(self.image.bits()))
        self.update()

    def save_canvas(self):
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "", "PNG Files (*.png);;All Files (*)")
        if file_path:
            self.image.save(file_path, "PNG")

    def resizeEvent(self, event):
        super(PaintCanvas, self).resizeEvent(event)
        self.image = QtGui.QImage(self.size(), QtGui.QImage.Format_RGBA8888)
