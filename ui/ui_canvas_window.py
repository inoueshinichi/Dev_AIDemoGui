# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_canvas_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from canvas_view import CanvasView


class Ui_CanvasWindow(object):
    def setupUi(self, CanvasWindow):
        if not CanvasWindow.objectName():
            CanvasWindow.setObjectName(u"CanvasWindow")
        CanvasWindow.resize(573, 355)
        self.centralwidget = QWidget(CanvasWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_image_status = QLineEdit(self.centralwidget)
        self.lineEdit_image_status.setObjectName(u"lineEdit_image_status")
        self.lineEdit_image_status.setReadOnly(True)

        self.horizontalLayout.addWidget(self.lineEdit_image_status)

        self.label_view_scale = QLabel(self.centralwidget)
        self.label_view_scale.setObjectName(u"label_view_scale")

        self.horizontalLayout.addWidget(self.label_view_scale)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.graphicsView_canvas = CanvasView(self.centralwidget)
        self.graphicsView_canvas.setObjectName(u"graphicsView_canvas")
        self.graphicsView_canvas.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.graphicsView_canvas.setMouseTracking(True)
        self.graphicsView_canvas.setAutoFillBackground(True)

        self.verticalLayout.addWidget(self.graphicsView_canvas)

        CanvasWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(CanvasWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 573, 26))
        CanvasWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(CanvasWindow)
        self.statusbar.setObjectName(u"statusbar")
        CanvasWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CanvasWindow)

        QMetaObject.connectSlotsByName(CanvasWindow)
    # setupUi

    def retranslateUi(self, CanvasWindow):
        CanvasWindow.setWindowTitle(QCoreApplication.translate("CanvasWindow", u"CanvasWindow", None))
        self.lineEdit_image_status.setPlaceholderText(QCoreApplication.translate("CanvasWindow", u"Image Status...", None))
        self.label_view_scale.setText(QCoreApplication.translate("CanvasWindow", u"100%", None))
    # retranslateUi

