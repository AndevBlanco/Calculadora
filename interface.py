# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def toSum(self, MainWindow):
        values=self.textEdit.toPlainText()
        inpu=self.inp.toPlainText()
        inpu2=self.inp2.toPlainText()
        if((inpu.isdigit()) and (inpu2=="")):
            self.inp3.setText(inpu)
            values=values+(inpu)+"\n"
            self.textEdit.setText(values)
        elif((inpu2.isdigit()) and (inpu=="")):
            self.inp3.setText(inpu2)
            values=values+(inpu2)+"\n"
            self.textEdit.setText(values)
        elif(((inpu.isdigit())==True) and ((inpu2.isdigit())==True)):
            self.inp3.setText(str(int(inpu)+int(inpu2)))
            values=values+(str(int(inpu)+int(inpu2)))+"\n"
            self.textEdit.setText(values)
        elif((inpu=="") and (inpu2=="")):
            self.inp3.setText("Empty")
        elif(((inpu.isdigit())==False) and ((inpu2.isdigit())==False)):
            def vali(inpu, inpu2):
                try:
                    float(inpu)
                    try:
                        float(inpu2)
                        return True
                    except:
                        return False
                except:
                    return False
            R=vali(inpu, inpu2)
            if(R==True):
                self.inp3.setText(str(float(inpu)+float(inpu2)))
                values=values+(str(float(inpu)+float(inpu2)))+"\n"
                self.textEdit.setText(values)
        elif(((inpu.isdigit())==False) and (inpu2!="")):
            def vali(inpu):
                try:
                    float(inpu)
                    return True
                except:
                    return False
            R=vali(inpu)
            if((R==True) and (inpu2.isdigit())):
                self.inp3.setText(str(float(inpu)+int(inpu2)))
                values=values+(str(float(inpu)+int(inpu2)))+"\n"
                self.textEdit.setText(values)
        elif(((inpu2.isdigit())==False) and (inpu!="")):
            def vali(inpu2):
                try:
                    float(inpu2)
                    return True
                except:
                    return False
            R=vali(inpu2)
            if((R==True) and (inpu.isdigit())):
                self.inp3.setText(str(float(inpu2)+int(inpu)))
                values=values+(str(float(inpu2)+int(inpu)))+"\n"
                self.textEdit.setText(values)
    def toMin(self, MainWindow):
        values=self.textEdit.toPlainText()
        inpu=self.inp.toPlainText()
        inpu2=self.inp2.toPlainText()
        if((inpu.isdigit()) and (inpu2=="")):
            self.inp3.setText(inpu)
            values=values+(inpu)+"\n"
            self.textEdit.setText(values)
        elif((inpu2.isdigit()) and (inpu=="")):
            self.inp3.setText("-"+inpu2)
            values=values+(inpu2)+"\n"
            self.textEdit.setText(values)
        elif(((inpu.isdigit())==True) and ((inpu2.isdigit())==True)):
            self.inp3.setText(str(int(inpu)-int(inpu2)))
            values=values+(str(int(inpu)-int(inpu2)))+"\n"
            self.textEdit.setText(values)
        elif((inpu=="") and (inpu2=="")):
            self.inp3.setText("Empty")
        elif(((inpu.isdigit())==False) and ((inpu2.isdigit())==False)):
            def vali(inpu, inpu2):
                try:
                    float(inpu)
                    try:
                        float(inpu2)
                        return True
                    except:
                        return False
                except:
                    return False
            R=vali(inpu, inpu2)
            if(R==True):
                self.inp3.setText(str(float(inpu)-float(inpu2)))
                values=values+(str(float(inpu)-float(inpu2)))+"\n"
                self.textEdit.setText(values)
        elif(((inpu.isdigit())==False) and (inpu2!="")):
            def vali(inpu):
                try:
                    float(inpu)
                    return True
                except:
                    return False
            R=vali(inpu)
            if((R==True) and (inpu2.isdigit())):
                self.inp3.setText(str(float(inpu)-int(inpu2)))
                values=values+(str(float(inpu)-int(inpu2)))+"\n"
                self.textEdit.setText(values)
        elif(((inpu2.isdigit())==False) and (inpu!="")):
            def vali(inpu2):
                try:
                    float(inpu2)
                    return True
                except:
                    return False
            R=vali(inpu2)
            if((R==True) and (inpu.isdigit())):
                self.inp3.setText(str(float(inpu2)-int(inpu)))
                values=values+(str(float(inpu2)-int(inpu)))+"\n"
                self.textEdit.setText(values)
    def toMultiply(self, MainWindow):
        values=self.textEdit.toPlainText()
        inpu=self.inp.toPlainText()
        inpu2=self.inp2.toPlainText()
        if((inpu.isdigit()) and (inpu2=="")):
            self.inp3.setText("0")
            values=values+("0")+"\n"
            self.textEdit.setText(values)
        elif((inpu2.isdigit()) and (inpu=="")):
            self.inp3.setText("0")
            values=values+("0")+"\n"
            self.textEdit.setText(values)
        elif(((inpu.isdigit())==True) and ((inpu2.isdigit())==True)):
            self.inp3.setText(str(int(inpu)*int(inpu2)))
            values=values+(str(int(inpu)*int(inpu2)))+"\n"
            self.textEdit.setText(values)
        elif((inpu=="") and (inpu2=="")):
            self.inp3.setText("Empty")
        elif(((inpu.isdigit())==False) and ((inpu2.isdigit())==False)):
            def vali(inpu, inpu2):
                try:
                    float(inpu)
                    try:
                        float(inpu2)
                        return True
                    except:
                        return False
                except:
                    return False
            R=vali(inpu, inpu2)
            if(R==True):
                self.inp3.setText(str(float(inpu)*float(inpu2)))
                values=values+(str(float(inpu)*float(inpu2)))+"\n"
                self.textEdit.setText(values)
        elif(((inpu.isdigit())==False) and (inpu2!="")):
            def vali(inpu):
                try:
                    float(inpu)
                    return True
                except:
                    return False
            R=vali(inpu)
            if((R==True) and (inpu2.isdigit())):
                self.inp3.setText(str(float(inpu)*int(inpu2)))
                values=values+(str(float(inpu)*int(inpu2)))+"\n"
                self.textEdit.setText(values)
        elif(((inpu2.isdigit())==False) and (inpu!="")):
            def vali(inpu2):
                try:
                    float(inpu2)
                    return True
                except:
                    return False
            R=vali(inpu2)
            if((R==True) and (inpu.isdigit())):
                self.inp3.setText(str(float(inpu2)*int(inpu)))
                values=values+(str(float(inpu2)*int(inpu)))+"\n"
                self.textEdit.setText(values)
    def toDiv(self, MainWindow):
        values=self.textEdit.toPlainText()
        inpu=self.inp.toPlainText()
        inpu2=self.inp2.toPlainText()
        if(inpu=="0" or inpu2=="0"):
            self.inp3.setText("Error 404")
        elif(((inpu.isdigit())==True) and ((inpu2.isdigit())==True)):
            self.inp3.setText(str(int(inpu)/int(inpu2)))
            values=values+(str(int(inpu)/int(inpu2)))+"\n"
            self.textEdit.setText(values)
        elif((inpu=="") and (inpu2=="")):
            self.inp3.setText("Empty")
        elif(((inpu.isdigit())==False) and ((inpu2.isdigit())==False)):
            def vali(inpu, inpu2):
                try:
                    float(inpu)
                    try:
                        float(inpu2)
                        return True
                    except:
                        return False
                except:
                    return False
            R=vali(inpu, inpu2)
            if(R==True):
                self.inp3.setText(str(float(inpu)/float(inpu2)))
                values=values+(str(float(inpu)/float(inpu2)))+"\n"
                self.textEdit.setText(values)
        elif(((inpu.isdigit())==False) and (inpu2!="")):
            def vali(inpu):
                try:
                    float(inpu)
                    return True
                except:
                    return False
            R=vali(inpu)
            if((R==True) and (inpu2.isdigit())):
                self.inp3.setText(str(float(inpu)/int(inpu2)))
                values=values+(str(float(inpu)/int(inpu2)))+"\n"
                self.textEdit.setText(values)
        elif(((inpu2.isdigit())==False) and (inpu!="")):
            def vali(inpu2):
                try:
                    float(inpu2)
                    return True
                except:
                    return False
            R=vali(inpu2)
            if((R==True) and (inpu.isdigit())):
                self.inp3.setText(str(float(inpu2)/int(inpu)))
                values=values+(str(float(inpu2)/int(inpu)))+"\n"
                self.textEdit.setText(values)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(424, 300)
        MainWindow.setStyleSheet("background-color:#2b2c2e;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.equal = QtWidgets.QPushButton(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(360, 210, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.equal.setFont(font)
        self.equal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equal.setStyleSheet("background-color:#ff9f0a;\n"
"color:#e4e4e5;")
        self.equal.setObjectName("equal")
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(360, 160, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.add.setFont(font)
        self.add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add.setStyleSheet("background-color:#ff9f0a;\n"
"color:#e4e4e5;")
        self.add.setObjectName("add")
        self.add.clicked.connect(self.toSum)
        self.minus = QtWidgets.QPushButton(self.centralwidget)
        self.minus.setGeometry(QtCore.QRect(360, 110, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.minus.setFont(font)
        self.minus.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.minus.setStyleSheet("background-color:#ff9f0a;\n"
"color:#e4e4e5;")
        self.minus.setObjectName("minus")
        self.minus.clicked.connect(self.toMin)
        self.multiply = QtWidgets.QPushButton(self.centralwidget)
        self.multiply.setGeometry(QtCore.QRect(360, 60, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.multiply.setFont(font)
        self.multiply.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiply.setStyleSheet("background-color:#ff9f0a;\n"
"color:#e4e4e5;")
        self.multiply.setObjectName("multiply")
        self.multiply.clicked.connect(self.toMultiply)
        self.inp = QtWidgets.QTextEdit(self.centralwidget)
        self.inp.setEnabled(True)
        self.inp.setGeometry(QtCore.QRect(10, 20, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inp.setFont(font)
        self.inp.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inp.setStyleSheet("color:#e4e4e5;")
        self.inp.setReadOnly(False)
        self.inp.setOverwriteMode(False)
        self.inp.setObjectName("inp")
        self.div = QtWidgets.QPushButton(self.centralwidget)
        self.div.setGeometry(QtCore.QRect(360, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.div.setFont(font)
        self.div.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.div.setStyleSheet("background-color:#ff9f0a;\n"
"color:#e4e4e5;")
        self.div.setObjectName("div")
        self.div.clicked.connect(self.toDiv)
        self.porcent = QtWidgets.QPushButton(self.centralwidget)
        self.porcent.setGeometry(QtCore.QRect(310, 10, 51, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.porcent.setFont(font)
        self.porcent.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.porcent.setStyleSheet("background-color:#434346;\n"
"color:#e4e4e5;")
        self.porcent.setObjectName("porcent")
        self.clearall = QtWidgets.QPushButton(self.centralwidget)
        self.clearall.setGeometry(QtCore.QRect(240, 10, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.clearall.setFont(font)
        self.clearall.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.clearall.setStyleSheet("background-color:#434346;\n"
"color:#e4e4e5;")
        self.clearall.setObjectName("clearall")
        self.binary = QtWidgets.QPushButton(self.centralwidget)
        self.binary.setGeometry(QtCore.QRect(240, 60, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.binary.setFont(font)
        self.binary.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.binary.setStyleSheet("background-color:#434346;\n"
"color:#e4e4e5;")
        self.binary.setObjectName("binary")
        self.hexadecimal = QtWidgets.QPushButton(self.centralwidget)
        self.hexadecimal.setGeometry(QtCore.QRect(240, 110, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.hexadecimal.setFont(font)
        self.hexadecimal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.hexadecimal.setStyleSheet("background-color:#434346;\n"
"color:#e4e4e5;")
        self.hexadecimal.setObjectName("hexadecimal")
        self.decimal = QtWidgets.QPushButton(self.centralwidget)
        self.decimal.setGeometry(QtCore.QRect(240, 160, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.decimal.setFont(font)
        self.decimal.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.decimal.setStyleSheet("background-color:#434346;\n"
"color:#e4e4e5;")
        self.decimal.setObjectName("decimal")
        self.help = QtWidgets.QPushButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(240, 210, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.help.setFont(font)
        self.help.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.help.setStyleSheet("background-color:#434346;\n"
"color:#e4e4e5;")
        self.help.setObjectName("help")
        self.inp2 = QtWidgets.QTextEdit(self.centralwidget)
        self.inp2.setGeometry(QtCore.QRect(10, 80, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inp2.setFont(font)
        self.inp2.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inp2.setStyleSheet("color:#e4e4e5;")
        self.inp2.setReadOnly(False)
        self.inp2.setOverwriteMode(False)
        self.inp2.setObjectName("inp2")
        self.time = QtWidgets.QDateTimeEdit(self.centralwidget)
        self.time.setGeometry(QtCore.QRect(20, 140, 194, 31))
        self.time.setReadOnly(True)
        self.time.setObjectName("time")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color:#e4e4e5;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.inp3 = QtWidgets.QTextEdit(self.centralwidget)
        self.inp3.setGeometry(QtCore.QRect(120, 20, 101, 111))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.inp3.setFont(font)
        self.inp3.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.inp3.setStyleSheet("color:#e4e4e5;")
        self.inp3.setReadOnly(True)
        self.inp3.setOverwriteMode(False)
        self.inp3.setObjectName("inp3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 424, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.equal.setText(_translate("MainWindow", "="))
        self.add.setText(_translate("MainWindow", "+"))
        self.minus.setText(_translate("MainWindow", "-"))
        self.multiply.setText(_translate("MainWindow", "x"))
        self.div.setText(_translate("MainWindow", "÷"))
        self.porcent.setText(_translate("MainWindow", "%"))
        self.clearall.setText(_translate("MainWindow", "A/C"))
        self.binary.setText(_translate("MainWindow", "Binary"))
        self.hexadecimal.setText(_translate("MainWindow", "Hexadecimal"))
        self.decimal.setText(_translate("MainWindow", "Decimal"))
        self.help.setText(_translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

