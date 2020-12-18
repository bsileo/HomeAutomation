# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(320, 240)
        MainWindow.setMinimumSize(QtCore.QSize(320, 240))
        MainWindow.setMaximumSize(QtCore.QSize(325, 240))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        MainWindow.setMouseTracking(True)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("#MainWindow {\n"
"background: black;\n"
"}\n"
"\n"
"#MainFrame {\n"
"border: 3px solid gray;\n"
"border-radius: 40px;\n"
"background: black;\n"
"}\n"
"\n"
"QCheckBox#heatCheck:indicator {\n"
"    width: 35px;\n"
"    height: 25px;\n"
"\n"
"}")
        self.MainFrame = QtWidgets.QWidget(MainWindow)
        self.MainFrame.setMaximumSize(QtCore.QSize(295, 218))
        self.MainFrame.setMouseTracking(True)
        self.MainFrame.setObjectName("MainFrame")
        self.layoutWidget = QtWidgets.QWidget(self.MainFrame)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 254, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 11, 11)
        self.gridLayout.setHorizontalSpacing(5)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.fireOnButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fireOnButton.sizePolicy().hasHeightForWidth())
        self.fireOnButton.setSizePolicy(sizePolicy)
        self.fireOnButton.setMinimumSize(QtCore.QSize(120, 30))
        self.fireOnButton.setStyleSheet("background-color:orange;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: black;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.fireOnButton.setAutoDefault(False)
        self.fireOnButton.setObjectName("fireOnButton")
        self.gridLayout.addWidget(self.fireOnButton, 4, 1, 1, 1)
        self.whiteButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.whiteButton.sizePolicy().hasHeightForWidth())
        self.whiteButton.setSizePolicy(sizePolicy)
        self.whiteButton.setMinimumSize(QtCore.QSize(120, 30))
        self.whiteButton.setStyleSheet("background-color:white;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: grey;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.whiteButton.setText("")
        self.whiteButton.setObjectName("whiteButton")
        self.gridLayout.addWidget(self.whiteButton, 3, 0, 1, 1)
        self.redButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.redButton.sizePolicy().hasHeightForWidth())
        self.redButton.setSizePolicy(sizePolicy)
        self.redButton.setMinimumSize(QtCore.QSize(120, 30))
        self.redButton.setAutoFillBackground(False)
        self.redButton.setStyleSheet("background-color:red;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.redButton.setText("")
        self.redButton.setCheckable(False)
        self.redButton.setAutoDefault(False)
        self.redButton.setObjectName("redButton")
        self.gridLayout.addWidget(self.redButton, 0, 0, 1, 1)
        self.blueButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blueButton.sizePolicy().hasHeightForWidth())
        self.blueButton.setSizePolicy(sizePolicy)
        self.blueButton.setMinimumSize(QtCore.QSize(120, 30))
        self.blueButton.setStyleSheet("background-color:blue;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.blueButton.setText("")
        self.blueButton.setObjectName("blueButton")
        self.gridLayout.addWidget(self.blueButton, 0, 1, 1, 1)
        self.purpleButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.purpleButton.sizePolicy().hasHeightForWidth())
        self.purpleButton.setSizePolicy(sizePolicy)
        self.purpleButton.setMinimumSize(QtCore.QSize(120, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(128, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.purpleButton.setPalette(palette)
        self.purpleButton.setStyleSheet("background-color:purple;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.purpleButton.setText("")
        self.purpleButton.setObjectName("purpleButton")
        self.gridLayout.addWidget(self.purpleButton, 1, 0, 1, 1)
        self.yellowButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yellowButton.sizePolicy().hasHeightForWidth())
        self.yellowButton.setSizePolicy(sizePolicy)
        self.yellowButton.setMinimumSize(QtCore.QSize(120, 30))
        self.yellowButton.setStyleSheet("background-color:yellow;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.yellowButton.setText("")
        self.yellowButton.setObjectName("yellowButton")
        self.gridLayout.addWidget(self.yellowButton, 1, 1, 1, 1)
        self.offButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.offButton.sizePolicy().hasHeightForWidth())
        self.offButton.setSizePolicy(sizePolicy)
        self.offButton.setMinimumSize(QtCore.QSize(120, 30))
        self.offButton.setStyleSheet("background-color:grey;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.offButton.setObjectName("offButton")
        self.gridLayout.addWidget(self.offButton, 3, 1, 1, 1)
        self.greenButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.greenButton.sizePolicy().hasHeightForWidth())
        self.greenButton.setSizePolicy(sizePolicy)
        self.greenButton.setMinimumSize(QtCore.QSize(120, 30))
        self.greenButton.setStyleSheet("background-color:#00aa00;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.greenButton.setText("")
        self.greenButton.setObjectName("greenButton")
        self.gridLayout.addWidget(self.greenButton, 2, 0, 1, 1)
        self.ltBlueButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ltBlueButton.sizePolicy().hasHeightForWidth())
        self.ltBlueButton.setSizePolicy(sizePolicy)
        self.ltBlueButton.setMinimumSize(QtCore.QSize(120, 30))
        self.ltBlueButton.setStyleSheet("background-color:lightblue;\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-radius: 10px;\n"
"border-color: beige;\n"
"font: bold 14px;\n"
"padding: 6px;")
        self.ltBlueButton.setText("")
        self.ltBlueButton.setObjectName("ltBlueButton")
        self.gridLayout.addWidget(self.ltBlueButton, 2, 1, 1, 1)
        self.heatCheck = QtWidgets.QCheckBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.heatCheck.setFont(font)
        self.heatCheck.setStyleSheet("color: white;\n"
"font-size:20px;\n"
"text-align:center;\n"
"padding-left:12px\n"
"")
        self.heatCheck.setCheckable(True)
        self.heatCheck.setChecked(True)
        self.heatCheck.setObjectName("heatCheck")
        self.gridLayout.addWidget(self.heatCheck, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.MainFrame)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setEnabled(False)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.fireOnButton.setText(_translate("MainWindow", "Fire On"))
        self.offButton.setText(_translate("MainWindow", "Lights Off"))
        self.heatCheck.setText(_translate("MainWindow", "Heat On"))

