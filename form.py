from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(240, 183)
        self.browse_for_asRecieved = QtGui.QPushButton(Dialog)
        self.browse_for_asRecieved.setGeometry(QtCore.QRect(180, 30, 51, 23))
        self.browse_for_asRecieved.setObjectName(_fromUtf8("browse_for_asRecieved"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 30, 151, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(60, 10, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 80, 151, 20))
        self.lineEdit_2.setText(_fromUtf8(""))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.browse_for_template = QtGui.QPushButton(Dialog)
        self.browse_for_template.setGeometry(QtCore.QRect(180, 80, 51, 23))
        self.browse_for_template.setObjectName(_fromUtf8("browse_for_template"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.startButton = QtGui.QPushButton(Dialog)
        self.startButton.setGeometry(QtCore.QRect(10, 130, 75, 23))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(110, 130, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar.setValue(0)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 91, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Templater", None))
        self.browse_for_asRecieved.setText(_translate("Dialog", "Browse", None))
        self.label.setText(_translate("Dialog", "As Recieved", None))
        self.browse_for_template.setText(_translate("Dialog", "Browse", None))
        self.label_2.setText(_translate("Dialog", "Template", None))
        self.startButton.setText(_translate("Dialog", "Run!", None))
        self.label_3.setText(_translate("Dialog", "bvolk@aclara.com", None))
