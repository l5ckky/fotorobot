# Form implementation generated from reading ui file 'fotorobot.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 914)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabs = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabs.setGeometry(QtCore.QRect(550, 0, 491, 831))
        self.tabs.setObjectName("tabs")
        self.eyes_tab = QtWidgets.QWidget()
        self.eyes_tab.setObjectName("eyes_tab")
        self.layoutWidget = QtWidgets.QWidget(parent=self.eyes_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 481, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.tab_v_layout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.tab_v_layout.setContentsMargins(0, 0, 0, 0)
        self.tab_v_layout.setObjectName("tab_v_layout")
        self.filters_group_box = QtWidgets.QGroupBox(parent=self.layoutWidget)
        self.filters_group_box.setMinimumSize(QtCore.QSize(0, 0))
        self.filters_group_box.setObjectName("filters_group_box")
        self.layoutWidget1 = QtWidgets.QWidget(parent=self.filters_group_box)
        self.layoutWidget1.setGeometry(QtCore.QRect(5, 20, 471, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.filters_v_layout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.filters_v_layout.setContentsMargins(0, 0, 0, 0)
        self.filters_v_layout.setSpacing(5)
        self.filters_v_layout.setObjectName("filters_v_layout")
        self.filter_h_layout = QtWidgets.QHBoxLayout()
        self.filter_h_layout.setSpacing(20)
        self.filter_h_layout.setObjectName("filter_h_layout")
        self.property_label = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.property_label.setObjectName("property_label")
        self.filter_h_layout.addWidget(self.property_label)
        self.property_combo = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.property_combo.setEditable(False)
        self.property_combo.setObjectName("property_combo")
        self.property_combo.addItem("")
        self.property_combo.addItem("")
        self.filter_h_layout.addWidget(self.property_combo)
        self.filters_v_layout.addLayout(self.filter_h_layout)
        self.filter2_h_layout = QtWidgets.QHBoxLayout()
        self.filter2_h_layout.setSpacing(20)
        self.filter2_h_layout.setObjectName("filter2_h_layout")
        self.gender_label_2 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.gender_label_2.setObjectName("gender_label_2")
        self.filter2_h_layout.addWidget(self.gender_label_2)
        self.countour_eye = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.countour_eye.setEditable(False)
        self.countour_eye.setObjectName("countour_eye")
        self.countour_eye.addItem("")
        self.countour_eye.addItem("")
        self.countour_eye.addItem("")
        self.filter2_h_layout.addWidget(self.countour_eye)
        self.filters_v_layout.addLayout(self.filter2_h_layout)
        self.filter3_h_layout = QtWidgets.QHBoxLayout()
        self.filter3_h_layout.setSpacing(20)
        self.filter3_h_layout.setObjectName("filter3_h_layout")
        self.gender_label_3 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.gender_label_3.setObjectName("gender_label_3")
        self.filter3_h_layout.addWidget(self.gender_label_3)
        self.openin_eye_fissure = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.openin_eye_fissure.setEditable(False)
        self.openin_eye_fissure.setCurrentText("")
        self.openin_eye_fissure.setObjectName("openin_eye_fissure")
        self.filter3_h_layout.addWidget(self.openin_eye_fissure)
        self.filters_v_layout.addLayout(self.filter3_h_layout)
        self.filter4_h_layout = QtWidgets.QHBoxLayout()
        self.filter4_h_layout.setSpacing(20)
        self.filter4_h_layout.setObjectName("filter4_h_layout")
        self.gender_label_4 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.gender_label_4.setObjectName("gender_label_4")
        self.filter4_h_layout.addWidget(self.gender_label_4)
        self.comboBox_4 = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.filter4_h_layout.addWidget(self.comboBox_4)
        self.filters_v_layout.addLayout(self.filter4_h_layout)
        self.filter5_h_layout = QtWidgets.QHBoxLayout()
        self.filter5_h_layout.setSpacing(20)
        self.filter5_h_layout.setObjectName("filter5_h_layout")
        self.gender_label_5 = QtWidgets.QLabel(parent=self.layoutWidget1)
        self.gender_label_5.setObjectName("gender_label_5")
        self.filter5_h_layout.addWidget(self.gender_label_5)
        self.comboBox_5 = QtWidgets.QComboBox(parent=self.layoutWidget1)
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.filter5_h_layout.addWidget(self.comboBox_5)
        self.filters_v_layout.addLayout(self.filter5_h_layout)
        self.f_buttons_layout = QtWidgets.QHBoxLayout()
        self.f_buttons_layout.setObjectName("f_buttons_layout")
        self.f_apply_button = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.f_apply_button.setObjectName("f_apply_button")
        self.f_buttons_layout.addWidget(self.f_apply_button)
        self.f_reset_button = QtWidgets.QPushButton(parent=self.layoutWidget1)
        self.f_reset_button.setObjectName("f_reset_button")
        self.f_buttons_layout.addWidget(self.f_reset_button)
        self.filters_v_layout.addLayout(self.f_buttons_layout)
        self.tab_v_layout.addWidget(self.filters_group_box)
        self.list_frame = QtWidgets.QFrame(parent=self.eyes_tab)
        self.list_frame.setGeometry(QtCore.QRect(0, 220, 481, 581))
        self.list_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.list_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.list_frame.setObjectName("list_frame")
        self.tabs.addTab(self.eyes_tab, "")
        self.nose_tab = QtWidgets.QWidget()
        self.nose_tab.setObjectName("nose_tab")
        self.tabs.addTab(self.nose_tab, "")
        self.refresh_list = QtWidgets.QPushButton(parent=self.centralwidget)
        self.refresh_list.setGeometry(QtCore.QRect(950, 830, 93, 28))
        self.refresh_list.setObjectName("refresh_list")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 26))
        self.menubar.setObjectName("menubar")
        self.datebase = QtWidgets.QMenu(parent=self.menubar)
        self.datebase.setObjectName("datebase")
        self.add_element = QtWidgets.QMenu(parent=self.datebase)
        self.add_element.setObjectName("add_element")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.add_mouth = QtGui.QAction(parent=MainWindow)
        self.add_mouth.setObjectName("add_mouth")
        self.add_nose = QtGui.QAction(parent=MainWindow)
        self.add_nose.setObjectName("add_nose")
        self.add_hair = QtGui.QAction(parent=MainWindow)
        self.add_hair.setObjectName("add_hair")
        self.add_eyes = QtGui.QAction(parent=MainWindow)
        self.add_eyes.setCheckable(False)
        self.add_eyes.setObjectName("add_eyes")
        self.add_eyebrows = QtGui.QAction(parent=MainWindow)
        self.add_eyebrows.setObjectName("add_eyebrows")
        self.add_chin = QtGui.QAction(parent=MainWindow)
        self.add_chin.setObjectName("add_chin")
        self.add_moustache = QtGui.QAction(parent=MainWindow)
        self.add_moustache.setObjectName("add_moustache")
        self.add_hat = QtGui.QAction(parent=MainWindow)
        self.add_hat.setObjectName("add_hat")
        self.add_clothes = QtGui.QAction(parent=MainWindow)
        self.add_clothes.setObjectName("add_clothes")
        self.add_ears = QtGui.QAction(parent=MainWindow)
        self.add_ears.setObjectName("add_ears")
        self.add_wrinkles = QtGui.QAction(parent=MainWindow)
        self.add_wrinkles.setObjectName("add_wrinkles")
        self.add_glasses = QtGui.QAction(parent=MainWindow)
        self.add_glasses.setObjectName("add_glasses")
        self.delete_element = QtGui.QAction(parent=MainWindow)
        self.delete_element.setObjectName("delete_element")
        self.edit_element = QtGui.QAction(parent=MainWindow)
        self.edit_element.setObjectName("edit_element")
        self.add_element.addAction(self.add_eyes)
        self.add_element.addAction(self.add_mouth)
        self.add_element.addAction(self.add_nose)
        self.add_element.addAction(self.add_hair)
        self.add_element.addAction(self.add_eyebrows)
        self.add_element.addAction(self.add_chin)
        self.add_element.addAction(self.add_moustache)
        self.add_element.addAction(self.add_hat)
        self.add_element.addAction(self.add_clothes)
        self.add_element.addAction(self.add_ears)
        self.add_element.addAction(self.add_wrinkles)
        self.add_element.addAction(self.add_glasses)
        self.datebase.addAction(self.add_element.menuAction())
        self.datebase.addAction(self.delete_element)
        self.datebase.addAction(self.edit_element)
        self.menubar.addAction(self.datebase.menuAction())

        self.retranslateUi(MainWindow)
        self.tabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Фоторобот"))
        self.filters_group_box.setTitle(_translate("MainWindow", "Фильтры"))
        self.property_label.setText(_translate("MainWindow", "Пол"))
        self.property_combo.setCurrentText(_translate("MainWindow", "Мужской"))
        self.property_combo.setItemText(0, _translate("MainWindow", "Мужской"))
        self.property_combo.setItemText(1, _translate("MainWindow", "Женский"))
        self.gender_label_2.setText(_translate("MainWindow", "Контур глазной щели"))
        self.countour_eye.setCurrentText(_translate("MainWindow", "Миндалевидный"))
        self.countour_eye.setItemText(0, _translate("MainWindow", "Миндалевидный"))
        self.countour_eye.setItemText(1, _translate("MainWindow", "Сегментоидный"))
        self.countour_eye.setItemText(2, _translate("MainWindow", "Круглый"))
        self.gender_label_3.setText(_translate("MainWindow", "Степень раскрытия глазной щели"))
        self.gender_label_4.setText(_translate("MainWindow", "Положение глазной щели"))
        self.comboBox_4.setCurrentText(_translate("MainWindow", "Горизонтальное"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "Горизонтальное"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "Косовнутреннее"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "Косонаружное"))
        self.gender_label_5.setText(_translate("MainWindow", "Положение век"))
        self.comboBox_5.setCurrentText(_translate("MainWindow", "Среднее"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "Среднее"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "1"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "2"))
        self.f_apply_button.setText(_translate("MainWindow", "Применить"))
        self.f_reset_button.setText(_translate("MainWindow", "Сбросить"))
        self.tabs.setTabText(self.tabs.indexOf(self.eyes_tab), _translate("MainWindow", "Глаза"))
        self.tabs.setTabText(self.tabs.indexOf(self.nose_tab), _translate("MainWindow", "Нос"))
        self.refresh_list.setText(_translate("MainWindow", "обновить"))
        self.datebase.setTitle(_translate("MainWindow", "База данных"))
        self.add_element.setTitle(_translate("MainWindow", "Добавить элемент"))
        self.add_mouth.setText(_translate("MainWindow", "Рот"))
        self.add_nose.setText(_translate("MainWindow", "Нос"))
        self.add_hair.setText(_translate("MainWindow", "Волосы"))
        self.add_eyes.setText(_translate("MainWindow", "Глаза"))
        self.add_eyebrows.setText(_translate("MainWindow", "Брови"))
        self.add_chin.setText(_translate("MainWindow", "Подбородок"))
        self.add_moustache.setText(_translate("MainWindow", "Усы"))
        self.add_hat.setText(_translate("MainWindow", "Головной убор"))
        self.add_clothes.setText(_translate("MainWindow", "Одежда"))
        self.add_ears.setText(_translate("MainWindow", "Уши"))
        self.add_wrinkles.setText(_translate("MainWindow", "Морщины"))
        self.add_glasses.setText(_translate("MainWindow", "Очки"))
        self.delete_element.setText(_translate("MainWindow", "Удалить элемент"))
        self.edit_element.setText(_translate("MainWindow", "Изменить элемент"))
