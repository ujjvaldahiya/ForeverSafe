import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from joinwindow import Ui_MainWindow
from loginwindow import Ui_LoginWindow

if __name__ == "__main__":
    appdata = os.getenv("APPDATA")
    
    app = QtWidgets.QApplication(sys.argv)
    LaunchWin = QtWidgets.QMainWindow()
    if os.path.exists(appdata + "\\ForeverSafe\\TsnWjtkdhKQmhoPqkVOY.fsi"):
        ui = Ui_LoginWindow()
        ui.setupUi(LaunchWin)
    else:
        ui = Ui_MainWindow()
        ui.setupUi(LaunchWin)
    LaunchWin.show()
    sys.exit(app.exec_())