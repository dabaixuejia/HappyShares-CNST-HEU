# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\QtProjects\压水堆核电厂二回路热力系统初步设计(V1.0)\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main(object):
    def setupUi(self, Main):
        Main.setObjectName("Main")
        Main.resize(978, 760)
        self.centralwidget = QtWidgets.QWidget(Main)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setEnabled(True)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 981, 731))
        self.tabWidget_2.setAutoFillBackground(True)
        self.tabWidget_2.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget_2.setUsesScrollButtons(True)
        self.tabWidget_2.setDocumentMode(False)
        self.tabWidget_2.setTabsClosable(True)
        self.tabWidget_2.setMovable(False)
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(130, 150, 701, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(780, 620, 171, 61))
        self.label_4.setObjectName("label_4")
        self.pushButton_newPro = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_newPro.setGeometry(QtCore.QRect(330, 290, 271, 41))
        self.pushButton_newPro.setObjectName("pushButton_newPro")
        self.label = QtWidgets.QLabel(self.tab_4)
        self.label.setGeometry(QtCore.QRect(360, 20, 231, 91))
        self.label.setObjectName("label")
        self.pushButton_exit = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_exit.setGeometry(QtCore.QRect(330, 470, 271, 41))
        self.pushButton_exit.setObjectName("pushButton_exit")
        self.label_2 = QtWidgets.QLabel(self.tab_4)
        self.label_2.setGeometry(QtCore.QRect(330, 80, 301, 41))
        self.label_2.setObjectName("label_2")
        self.pushButton_openPro = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_openPro.setGeometry(QtCore.QRect(330, 380, 271, 41))
        self.pushButton_openPro.setObjectName("pushButton_openPro")
        self.tabWidget_2.addTab(self.tab_4, "")
        Main.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main)
        self.statusbar.setObjectName("statusbar")
        Main.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(Main)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 978, 26))
        self.menuBar.setObjectName("menuBar")
        self.menu_file = QtWidgets.QMenu(self.menuBar)
        self.menu_file.setObjectName("menu_file")
        self.menu_save = QtWidgets.QMenu(self.menu_file)
        self.menu_save.setObjectName("menu_save")
        self.menu_plot = QtWidgets.QMenu(self.menuBar)
        self.menu_plot.setObjectName("menu_plot")
        self.menu_par = QtWidgets.QMenu(self.menuBar)
        self.menu_par.setObjectName("menu_par")
        Main.setMenuBar(self.menuBar)
        self.action_new = QtWidgets.QAction(Main)
        self.action_new.setObjectName("action_new")
        self.action_open = QtWidgets.QAction(Main)
        self.action_open.setObjectName("action_open")
        self.action_exit = QtWidgets.QAction(Main)
        self.action_exit.setObjectName("action_exit")
        self.action_structure = QtWidgets.QAction(Main)
        self.action_structure.setObjectName("action_structure")
        self.action_initial = QtWidgets.QAction(Main)
        self.action_initial.setObjectName("action_initial")
        self.action_saveFulu = QtWidgets.QAction(Main)
        self.action_saveFulu.setObjectName("action_saveFulu")
        self.action_saveCode = QtWidgets.QAction(Main)
        self.action_saveCode.setObjectName("action_saveCode")
        self.action_savePlot = QtWidgets.QAction(Main)
        self.action_savePlot.setObjectName("action_savePlot")
        self.action_plot = QtWidgets.QAction(Main)
        self.action_plot.setObjectName("action_plot")
        self.action_showfulu = QtWidgets.QAction(Main)
        self.action_showfulu.setObjectName("action_showfulu")
        self.action_openFile = QtWidgets.QAction(Main)
        self.action_openFile.setObjectName("action_openFile")
        self.menu_save.addAction(self.action_saveFulu)
        self.menu_save.addAction(self.action_saveCode)
        self.menu_save.addAction(self.action_savePlot)
        self.menu_file.addAction(self.action_new)
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_openFile)
        self.menu_file.addAction(self.menu_save.menuAction())
        self.menu_file.addAction(self.action_exit)
        self.menu_plot.addAction(self.action_structure)
        self.menu_plot.addAction(self.action_plot)
        self.menu_par.addAction(self.action_initial)
        self.menu_par.addAction(self.action_showfulu)
        self.menuBar.addAction(self.menu_file.menuAction())
        self.menuBar.addAction(self.menu_par.menuAction())
        self.menuBar.addAction(self.menu_plot.menuAction())

        self.retranslateUi(Main)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Main)

    def retranslateUi(self, Main):
        _translate = QtCore.QCoreApplication.translate
        Main.setWindowTitle(_translate("Main", "主窗口"))
        self.label_3.setText(_translate("Main", "压水堆核电厂二回路热力系统初步设计(V0.1.0)"))
        self.label_4.setText(_translate("Main", "Designed by euaurora"))
        self.pushButton_newPro.setText(_translate("Main", "新建项目"))
        self.label.setText(_translate("Main", "哈尔滨工程大学核科学与技术学院"))
        self.pushButton_exit.setText(_translate("Main", "退出程序"))
        self.label_2.setText(_translate("Main", "核工程与核技术专业本科生课程设计（二）"))
        self.pushButton_openPro.setText(_translate("Main", "打开项目"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("Main", "Welcome"))
        self.menu_file.setTitle(_translate("Main", "文件(&F))"))
        self.menu_save.setTitle(_translate("Main", "另存为"))
        self.menu_plot.setTitle(_translate("Main", "绘制(&P)"))
        self.menu_par.setTitle(_translate("Main", "参数(&V)"))
        self.action_new.setText(_translate("Main", "新建项目"))
        self.action_new.setShortcut(_translate("Main", "Alt+N"))
        self.action_open.setText(_translate("Main", "打开项目"))
        self.action_open.setShortcut(_translate("Main", "Alt+O"))
        self.action_exit.setText(_translate("Main", "退出程序"))
        self.action_exit.setShortcut(_translate("Main", "Alt+E"))
        self.action_structure.setText(_translate("Main", "原理流程图"))
        self.action_structure.setShortcut(_translate("Main", "Alt+P"))
        self.action_initial.setText(_translate("Main", "输入原始参数"))
        self.action_initial.setShortcut(_translate("Main", "Alt+V"))
        self.action_saveFulu.setText(_translate("Main", "附录数据"))
        self.action_saveCode.setText(_translate("Main", "Python代码"))
        self.action_savePlot.setText(_translate("Main", "热线图"))
        self.action_plot.setText(_translate("Main", "查看热线图"))
        self.action_showfulu.setText(_translate("Main", "查看附录数据"))
        self.action_openFile.setText(_translate("Main", "打开文件"))