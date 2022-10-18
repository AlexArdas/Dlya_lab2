from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(332, 416)
        MainWindow.setStyleSheet("background-color: rgb(113, 110, 117);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(70, 0, 221, 31))
        self.title.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.title.setObjectName("title")
        self.For_txt = QtWidgets.QLineEdit(self.centralwidget)
        self.For_txt.setGeometry(QtCore.QRect(20, 110, 291, 41))
        self.For_txt.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.For_txt.setText("")
        self.For_txt.setObjectName("For_txt")
        self.For_txt.setToolTip("Введите текст который хотите зашифровать")
        self.zashifr = QtWidgets.QLabel(self.centralwidget)
        self.zashifr.setGeometry(QtCore.QRect(20, 60, 291, 41))
        self.zashifr.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(188, 188, 188);")
        self.zashifr.setObjectName("zashifr")
        self.For_deshifr = QtWidgets.QLineEdit(self.centralwidget)
        self.For_deshifr.setGeometry(QtCore.QRect(20, 240, 291, 41))
        self.For_deshifr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.For_deshifr.setText("")
        self.For_deshifr.setObjectName("For_deshifr")
        self.For_deshifr.setToolTip("Тут отобразиться текст который можно расшифровать, можете дополнить его или заменить")
        self.deshifrov = QtWidgets.QLabel(self.centralwidget)
        self.deshifrov.setGeometry(QtCore.QRect(20, 190, 291, 41))
        self.deshifrov.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(188, 188, 188);")
        self.deshifrov.setObjectName("deshifrov")
        self.Obsh = QtWidgets.QLineEdit(self.centralwidget)
        self.Obsh.setGeometry(QtCore.QRect(20, 370, 291, 41))
        self.Obsh.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Obsh.setText("")
        self.Obsh.setObjectName("Obsh")
        self.Obsh.setToolTip("Расшифрованный текст")
        self.pdtitle = QtWidgets.QLabel(self.centralwidget)
        self.pdtitle.setGeometry(QtCore.QRect(100, 30, 151, 21))
        self.pdtitle.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";")
        self.pdtitle.setObjectName("pdtitle")
        self.Vivod = QtWidgets.QLabel(self.centralwidget)
        self.Vivod.setGeometry(QtCore.QRect(20, 320, 291, 41))
        self.Vivod.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(188, 188, 188);")
        self.Vivod.setObjectName("Vivod")
        self.Bott_shifr = QtWidgets.QPushButton(self.centralwidget)
        self.Bott_shifr.setGeometry(QtCore.QRect(60, 160, 191, 21))
        self.Bott_shifr.setStyleSheet("background-color: rgb(196, 240, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.Bott_shifr.setObjectName("Bott_shifr")
        self.Bott_deshifr = QtWidgets.QPushButton(self.centralwidget)
        self.Bott_deshifr.setGeometry(QtCore.QRect(60, 290, 191, 21))
        self.Bott_deshifr.setStyleSheet("background-color: rgb(196, 240, 255);\n"
"font: 11pt \"MS Shell Dlg 2\";")
        self.Bott_deshifr.setObjectName("Bott_deshifr")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionasdsdas = QtWidgets.QAction(MainWindow)
        self.actionasdsdas.setObjectName("actionasdsdas")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Метод гаммирования"))
        self.zashifr.setText(_translate("MainWindow", "Напишите текст который хотите \n"
"зашифровать"))
        self.deshifrov.setText(_translate("MainWindow", "Напишите текст который хотите \n"
"расшифровать"))
        self.pdtitle.setText(_translate("MainWindow", "Ti+1 = (A*Ti+C) mod M."))
        self.Vivod.setText(_translate("MainWindow", "Расшифрованный текст"))
        self.Bott_shifr.setText(_translate("MainWindow", "Зашифровать"))
        self.Bott_deshifr.setText(_translate("MainWindow", "Расшифровать"))
        self.actionasdsdas.setText(_translate("MainWindow", "asdsdas"))
