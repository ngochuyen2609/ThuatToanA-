# Form implementation generated from reading ui file 'application.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import CreateMaze 

class Ui_Demo(object):
    
    def setupUi(self, Demo):
        Demo.setObjectName("Demo")
        Demo.resize(920, 790)
        self.centralwidget = QtWidgets.QWidget(parent=Demo)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 261, 121))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(parent=self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 16))
        self.label.setObjectName("label")
        self.width = QtWidgets.QLineEdit(parent=self.groupBox)
        self.width.setGeometry(QtCore.QRect(180, 20, 61, 20))
        self.width.setObjectName("width")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 171, 16))
        self.label_2.setObjectName("label_2")
        self.height = QtWidgets.QLineEdit(parent=self.groupBox)
        self.height.setGeometry(QtCore.QRect(180, 40, 61, 20))
        self.height.setObjectName("height")
        self.createMaze = QtWidgets.QPushButton(parent=self.groupBox)
        self.createMaze.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.createMaze.setObjectName("createMaze")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 120, 261, 451))
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 121, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 81, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 121, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 110, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 130, 121, 16))
        self.label_8.setObjectName("label_8")
        self.startX = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.startX.setGeometry(QtCore.QRect(160, 50, 81, 20))
        self.startX.setObjectName("startX")
        self.startY = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.startY.setGeometry(QtCore.QRect(160, 70, 81, 20))
        self.startY.setObjectName("startY")
        self.endX = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.endX.setGeometry(QtCore.QRect(160, 110, 81, 20))
        self.endX.setObjectName("endX")
        self.endY = QtWidgets.QLineEdit(parent=self.groupBox_2)
        self.endY.setGeometry(QtCore.QRect(160, 130, 81, 20))
        self.endY.setObjectName("endY")
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 160, 121, 16))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 190, 121, 16))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 310, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_12.setGeometry(QtCore.QRect(20, 230, 121, 16))
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_14.setGeometry(QtCore.QRect(20, 270, 121, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_15.setGeometry(QtCore.QRect(20, 390, 121, 16))
        self.label_15.setObjectName("label_15")
        self.heutistic2 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.heutistic2.setGeometry(QtCore.QRect(160, 230, 75, 23))
        self.heutistic2.setObjectName("heutistic2")
        self.heutistic3 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.heutistic3.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.heutistic3.setObjectName("heutistic3")
        self.heutistic4 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.heutistic4.setGeometry(QtCore.QRect(160, 310, 75, 23))
        self.heutistic4.setObjectName("heutistic4")
        self.heutistic1 = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.heutistic1.setGeometry(QtCore.QRect(160, 190, 75, 23))
        self.heutistic1.setObjectName("heutistic1")
        self.greedyBestFirstSearch = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.greedyBestFirstSearch.setGeometry(QtCore.QRect(160, 390, 75, 23))
        self.greedyBestFirstSearch.setObjectName("greedyBestFirstSearch")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 570, 261, 171))
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label_13.setObjectName("label_13")
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(10, 50, 121, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_18.setGeometry(QtCore.QRect(10, 110, 121, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_19.setGeometry(QtCore.QRect(10, 140, 121, 16))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_20.setGeometry(QtCore.QRect(150, 20, 91, 16))
        self.label_20.setText("")
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_21.setGeometry(QtCore.QRect(150, 50, 91, 16))
        self.label_21.setText("")
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_22.setGeometry(QtCore.QRect(180, 110, 91, 16))
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_23.setGeometry(QtCore.QRect(150, 80, 91, 16))
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_24.setGeometry(QtCore.QRect(150, 140, 91, 16))
        self.label_24.setText("")
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(parent=self.groupBox_3)
        self.label_25.setGeometry(QtCore.QRect(150, 110, 91, 16))
        self.label_25.setText("")
        self.label_25.setObjectName("label_25")
        Demo.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=Demo)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 920, 21))
        self.menubar.setObjectName("menubar")
        Demo.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=Demo)
        self.statusbar.setObjectName("statusbar")
        Demo.setStatusBar(self.statusbar)

        self.retranslateUi(Demo)
        QtCore.QMetaObject.connectSlotsByName(Demo)
        Demo.showFullScreen()
        self.createMaze.clicked.connect(self.create_maze)

    def retranslateUi(self, Demo):
        _translate = QtCore.QCoreApplication.translate
        Demo.setWindowTitle(_translate("Demo", "Demo Maze Solving Algorithm"))
        self.groupBox.setTitle(_translate("Demo", "Create Maze"))
        self.label.setText(_translate("Demo", "The width of the Maze (Max 120)"))
        self.label_2.setText(_translate("Demo", "The height of the Maze (Max 120)"))
        self.createMaze.setText(_translate("Demo", "Create Maze"))
        self.groupBox_2.setTitle(_translate("Demo", "Algorithm"))
        self.label_3.setText(_translate("Demo", "The source coordinate:"))
        self.label_4.setText(_translate("Demo", "X(default X = 0)"))
        self.label_5.setText(_translate("Demo", "Y(default Y = 0)"))
        self.label_6.setText(_translate("Demo", "The destintion coordinate:"))
        self.label_7.setText(_translate("Demo", "X(default X = width - 1)"))
        self.label_8.setText(_translate("Demo", "Y(default Y = height - 1)"))
        self.label_9.setText(_translate("Demo", "Heuristic function"))
        self.label_10.setText(_translate("Demo", "Heuristic1"))
        self.label_11.setText(_translate("Demo", "Heuristic4"))
        self.label_12.setText(_translate("Demo", "Heuristic2"))
        self.label_14.setText(_translate("Demo", "Heuristic3"))
        self.label_15.setText(_translate("Demo", "Greedy best-first search"))
        self.heutistic2.setText(_translate("Demo", "Start"))
        self.heutistic3.setText(_translate("Demo", "Start"))
        self.heutistic4.setText(_translate("Demo", "Start"))
        self.heutistic1.setText(_translate("Demo", "Start"))
        self.greedyBestFirstSearch.setText(_translate("Demo", "Start"))
        self.groupBox_3.setTitle(_translate("Demo", "Result"))
        self.label_13.setText(_translate("Demo", "Heuristic1"))
        self.label_16.setText(_translate("Demo", "Heuristic2"))
        self.label_17.setText(_translate("Demo", "Heuristic3"))
        self.label_18.setText(_translate("Demo", "Heuristic4"))
        self.label_19.setText(_translate("Demo", "Greedy best-first search"))
    def create_maze(self):
        global maze_map
        global grid
        width = int(self.width.text())  # Get width from QLineEdit
        height = int(self.height.text())  # Get height from QLineEdit
        grid, maze_map = CreateMaze.generate_maze(width, height)  # Assume this function returns grid and maze_map
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Demo = QtWidgets.QMainWindow()
    ui = Ui_Demo()
    ui.setupUi(Demo)
    Demo.show()
    sys.exit(app.exec())
