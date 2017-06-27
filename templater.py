import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from form import Ui_Dialog
from runner_class import *

class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.RUN)
        self.ui.browse_for_asRecieved.clicked.connect(self.BROWSE_RECIEVED)
        self.ui.browse_for_template.clicked.connect(self.BROWSE_TEMPLATE)
        

    def BROWSE_RECIEVED(self):
        self.recieved_filename = QFileDialog.getOpenFileName(None, 'Open File', sys.path[0])
        self.ui.lineEdit.setText(self.recieved_filename)
    
    def BROWSE_TEMPLATE(self):
        self.template_filename = QFileDialog.getOpenFileName(None, 'Open FIle', sys.path[0])
        self.ui.lineEdit_2.setText(self.template_filename)

    def RUN(self):
        print 'starting work!'
        runner = Runner( unicode(self.recieved_filename), unicode(self.template_filename) )
        runner.work(self.ui)
        print 'finished!'

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())
   
