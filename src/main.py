# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets
from datetime import date
import requests
from requests.structures import CaseInsensitiveDict
import json


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 820)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.switcher = QtWidgets.QTabWidget(self.centralwidget)
        self.switcher.setObjectName("switcher")
        self.inputpage = QtWidgets.QWidget()
        self.inputpage.setObjectName("inputpage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.inputpage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.inputpage)
        #self.webEngineView.setMinimumSize(QtCore.QSize(0, 500))
        self.webEngineView.setUrl(QtCore.QUrl("https://outlook.office365.com/calendar/published/7e2057ed2d55471295c0b44a8ba2da08@caroos.onmicrosoft.com/f64d98858c1a4892b939356e91604aab14985167320374266920/calendar.html"))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_3.addWidget(self.webEngineView)
        self.widget = QtWidgets.QWidget(self.inputpage)
        self.widget.setObjectName("widget")
        self.widget.setMaximumSize(QtCore.QSize(16777215, 252))
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.select_day = QtWidgets.QComboBox(self.widget)
        self.select_day.setMinimumSize(QtCore.QSize(87, 0))
        self.select_day.setObjectName("select_day")
        self.select_day.addItem("")
        self.select_day.setItemText(0, "0")
        self.select_day.addItem("")
        self.select_day.setItemText(1, "1")
        self.select_day.addItem("")
        self.select_day.setItemText(2, "2")
        self.select_day.addItem("")
        self.select_day.setItemText(3, "3")
        self.select_day.addItem("")
        #self.select_day.setItemText(4, "")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.select_day)
        self.day_input = QtWidgets.QLineEdit(self.widget)
        self.day_input.setObjectName("day_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.day_input)
        self.verticalLayout.addLayout(self.formLayout)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.select_onlycancel = QtWidgets.QComboBox(self.widget)
        self.select_onlycancel.setMinimumSize(QtCore.QSize(87, 0))
        self.select_onlycancel.setObjectName("select_onlycancel")
        self.select_onlycancel.addItem("")
        self.select_onlycancel.setItemText(0, "n")
        self.select_onlycancel.addItem("")
        self.select_onlycancel.setItemText(1, "j")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.select_onlycancel)
        self.onlycancel_input = QtWidgets.QLineEdit(self.widget)
        self.onlycancel_input.setObjectName("onlycancel_input")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.onlycancel_input)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.select_class = QtWidgets.QComboBox(self.widget)
        self.select_class.setMinimumSize(QtCore.QSize(87, 0))
        self.select_class.setObjectName("select_class")
        self.select_class.addItem("")
        #self.select_class.setItemText(0, "")
        self.select_class.addItem("")
        self.select_class.setItemText(1, "8a")
        self.select_class.addItem("")
        self.select_class.setItemText(2, "8b")
        self.select_class.addItem("")
        self.select_class.setItemText(3, "8c")
        self.select_class.addItem("")
        self.select_class.setItemText(4, "8d")
        self.select_class.addItem("")
        self.select_class.setItemText(5, "8e")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.select_class)
        self.class_input = QtWidgets.QLineEdit(self.widget)
        self.class_input.setObjectName("class_input")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.class_input)
        self.verticalLayout.addLayout(self.formLayout_3)
        self.runbutton = QtWidgets.QPushButton(self.widget)
        self.runbutton.setObjectName("runbutton")
        self.verticalLayout.addWidget(self.runbutton)
        self.verticalLayout_3.addWidget(self.widget)
        self.switcher.addTab(self.inputpage, "")
        self.day1_outputpage = QtWidgets.QWidget()
        self.day1_outputpage.setObjectName("day1_outputpage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.day1_outputpage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.day1_outputtable = QtWidgets.QTreeWidget(self.day1_outputpage)
        self.day1_outputtable.setEnabled(True)
        self.day1_outputtable.setToolTip("")
        self.day1_outputtable.setRootIsDecorated(False)
        self.day1_outputtable.setObjectName("day1_outputtable")
        self.day1_outputtable.headerItem().setText(0, "Klasse")
        self.day1_outputtable.headerItem().setText(1, "Stunde")
        self.day1_outputtable.headerItem().setText(2, "Fach")
        self.day1_outputtable.headerItem().setText(3, "Raum")
        self.day1_outputtable.headerItem().setText(4, "Lehrer")
        self.day1_outputtable.headerItem().setText(5, "Text")
#        item_0 = QtWidgets.QTreeWidgetItem(self.day1_outputtable)
#        self.day1_outputtable.topLevelItem(0).setText(0, "1Klasse")
#        self.day1_outputtable.topLevelItem(0).setText(1, "1Stunde")
#        self.day1_outputtable.topLevelItem(0).setText(2, "1Fach")
#        self.day1_outputtable.topLevelItem(0).setText(3, "1Raum")
#        self.day1_outputtable.topLevelItem(0).setText(4, "1Text")
#        self.day1_outputtable.topLevelItem(0).setText(5, "1Weiteres")
#        item_0 = QtWidgets.QTreeWidgetItem(self.day1_outputtable)
#        self.day1_outputtable.topLevelItem(1).setText(0, "2klasse")
#        self.day1_outputtable.topLevelItem(1).setText(1, "2Stunde")
        self.verticalLayout_4.addWidget(self.day1_outputtable)
        #self.switcher.addTab(self.day1_outputpage, "")
        self.day2_outputpage = QtWidgets.QWidget()
        self.day2_outputpage.setObjectName("day2_outputpage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.day2_outputpage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.day2_outputtable = QtWidgets.QTreeWidget(self.day2_outputpage)
        self.day2_outputtable.setEnabled(True)
        self.day2_outputtable.setToolTip("")
        self.day2_outputtable.setRootIsDecorated(False)
        self.day2_outputtable.setObjectName("day2_outputtable")
        self.day2_outputtable.headerItem().setText(0, "Klasse")
        self.day2_outputtable.headerItem().setText(1, "Stunde")
        self.day2_outputtable.headerItem().setText(2, "Fach")
        self.day2_outputtable.headerItem().setText(3, "Raum")
        self.day2_outputtable.headerItem().setText(4, "Lehrer")
        self.day2_outputtable.headerItem().setText(5, "Text")
#        item_0 = QtWidgets.QTreeWidgetItem(self.day2_outputtable)
#        self.day2_outputtable.topLevelItem(0).setText(0, "1Klasse")
#        self.day2_outputtable.topLevelItem(0).setText(1, "1Stunde")
#        self.day2_outputtable.topLevelItem(0).setText(2, "1Fach")
#        self.day2_outputtable.topLevelItem(0).setText(3, "1Raum")
#        self.day2_outputtable.topLevelItem(0).setText(4, "1Text")
#        self.day2_outputtable.topLevelItem(0).setText(5, "1Weiteres")
#        item_0 = QtWidgets.QTreeWidgetItem(self.day2_outputtable)
#        self.day2_outputtable.topLevelItem(1).setText(0, "2klasse")
#        self.day2_outputtable.topLevelItem(1).setText(1, "2Stunde")
        self.verticalLayout_5.addWidget(self.day2_outputtable)
        #self.switcher.addTab(self.day2_outputpage, "")
        self.day3_outputpage = QtWidgets.QWidget()
        self.day3_outputpage.setObjectName("day3_outputpage")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.day3_outputpage)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.day3_outputtable = QtWidgets.QTreeWidget(self.day3_outputpage)
        self.day3_outputtable.setEnabled(True)
        self.day3_outputtable.setToolTip("")
        self.day3_outputtable.setRootIsDecorated(False)
        self.day3_outputtable.setObjectName("day3_outputtable")
        self.day3_outputtable.headerItem().setText(0, "Klasse")
        self.day3_outputtable.headerItem().setText(1, "Stunde")
        self.day3_outputtable.headerItem().setText(2, "Fach")
        self.day3_outputtable.headerItem().setText(3, "Raum")
        self.day3_outputtable.headerItem().setText(4, "Lehrer")
        self.day3_outputtable.headerItem().setText(5, "Text")
#        item_0 = QtWidgets.QTreeWidgetItem(self.day3_outputtable)
#        self.day3_outputtable.topLevelItem(0).setText(0, "1Klasse")
#        self.day3_outputtable.topLevelItem(0).setText(1, "1Stunde")
#        self.day3_outputtable.topLevelItem(0).setText(2, "1Fach")
#        self.day3_outputtable.topLevelItem(0).setText(3, "1Raum")
#        self.day3_outputtable.topLevelItem(0).setText(4, "1Text")
#        self.day3_outputtable.topLevelItem(0).setText(5, "1Weiteres")
#        item_0 = QtWidgets.QTreeWidgetItem(self.day3_outputtable)
#        self.day3_outputtable.topLevelItem(1).setText(0, "2klasse")
#        self.day3_outputtable.topLevelItem(1).setText(1, "2Stunde")
        self.verticalLayout_6.addWidget(self.day3_outputtable)
        #self.switcher.addTab(self.day3_outputpage, "")
        self.verticalLayout_2.addWidget(self.switcher)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.switcher.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Vertretungsplantool"))
        self.label.setText(_translate("MainWindow", "Tag, der nachzuschauen ist (0=Heute, 1=Morgen, 2=Übermorgen...)"))
        self.onlycancel_input.setText("n")
        self.day_input.setText(_translate("MainWindow", "0"))
        self.label_2.setText(_translate("MainWindow", "Sollen nur Ausfälle angezeigt werden? (n = Nein,  j = Ja)"))
        self.label_3.setText(_translate("MainWindow", "Nur Klasse/Jahrgang anzeigen (nichts oder wenn ja welche eingeben)"))
        self.runbutton.setText(_translate("MainWindow", "Ausfüren"))
        self.runbutton.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.switcher.setTabText(self.switcher.indexOf(self.inputpage), _translate("MainWindow", "Eingabe"))
        self.day1_outputtable.setSortingEnabled(False)
        __sortingEnabled = self.day1_outputtable.isSortingEnabled()
        self.day1_outputtable.setSortingEnabled(False)
        self.day1_outputtable.setSortingEnabled(__sortingEnabled)
        self.switcher.setTabText(self.switcher.indexOf(self.day1_outputpage), _translate("MainWindow", "day1_tabname"))
        self.day2_outputtable.setSortingEnabled(False)
        __sortingEnabled = self.day2_outputtable.isSortingEnabled()
        self.day2_outputtable.setSortingEnabled(False)
        self.day2_outputtable.setSortingEnabled(__sortingEnabled)
        self.switcher.setTabText(self.switcher.indexOf(self.day2_outputpage), _translate("MainWindow", "day2_tabname"))
        self.day3_outputtable.setSortingEnabled(False)
        __sortingEnabled = self.day3_outputtable.isSortingEnabled()
        self.day3_outputtable.setSortingEnabled(False)
        self.day3_outputtable.setSortingEnabled(__sortingEnabled)
        self.switcher.setTabText(self.switcher.indexOf(self.day3_outputpage), _translate("MainWindow", "day3_tabname"))

    def MyWorkingCode(self, MainWindow):
        from datetime import date

        url = "https://nessa.webuntis.com/WebUntis/monitor/substitution/data?school=Gym%20Carolinum"

        date = date.today()
        date = date.strftime("%Y%m%d")

        def runbutton_clicked():
            for repeat_index in range(3):
                run(int(repeat_index))

        def run(index):

            dayindex = index + 1

            self.switcher.setCurrentWidget(self.inputpage)
            #self.switcher.setCurrentIndex(1)

            headers = CaseInsensitiveDict()
            headers["Content-Type"] = "application/json"

            tage = int(self.day_input.text()) + index

            nurAusfaelle = self.onlycancel_input.text().replace("j", "true").replace("n", "false")

            data = '"formatName":"VP SuS IServ morgen","schoolName":"Gym Carolinum","date":{},"dateOffset":{},"strikethrough":false,"mergeBlocks":true,"showOnlyFutureSub":false,"showBreakSupervisions":true,"showTeacher":true,"showClass":false,"showHour":true,"showInfo":true,"showRoom":true,"showSubject":true,"groupBy":1,"hideAbsent":false,"departmentIds":[],"departmentElementType":-1,"hideCancelWithSubstitution":true,"hideCancelCausedByEvent":false,"showTime":false,"showSubstText":true,"showAbsentElements":[],"showAffectedElements":[1],"showUnitTime":true,"showMessages":true,"showStudentgroup":false,"enableSubstitutionFrom":false,"showSubstitutionFrom":0,"showTeacherOnEvent":false,"showAbsentTeacher":true,"strikethroughAbsentTeacher":false,"activityTypeIds":[],"showEvent":true,"showCancel":true,"showOnlyCancel":{},"showSubstTypeColor":false,"showExamSupervision":false,"showUnheraldedExams":false'.format(
                date, tage, nurAusfaelle)
            data = "{" + data + "}"

            resp = requests.post(url, headers=headers, data=data)
            raw = resp.content.decode("utf-8")
            data = json.loads(raw)

            klasse = self.class_input.text()

            global outputline

            weekDay = data["payload"]["weekDay"]

            if dayindex == 1: 
                self.switcher.addTab(self.day1_outputpage, "")
                self.day1_outputtable.clear()
                self.switcher.setTabText(self.switcher.indexOf(self.day1_outputpage), weekDay)
            if dayindex == 2: 
                self.switcher.addTab(self.day2_outputpage, "")
                self.day2_outputtable.clear()
                self.switcher.setTabText(self.switcher.indexOf(self.day2_outputpage), weekDay)
            if dayindex == 3: 
                self.switcher.addTab(self.day3_outputpage, "")
                self.day3_outputtable.clear()
                self.switcher.setTabText(self.switcher.indexOf(self.day3_outputpage), weekDay)

            #self.weekday_lable.setText(weekDay)
            outputline = 0
            for x in data['payload']['rows']:
                a = x['group']
                if klasse.upper() in a:
                    pass
                else:
                    continue

                c = [string.replace('<span class="substMonitorSubstElem">',"").replace("</span>", "") for string in x['data']]

                c.insert(0, a)
                print(dayindex, outputline, c)

                global column
                column = 0
                if dayindex == 1: 
                    item_0 = QtWidgets.QTreeWidgetItem(self.day1_outputtable)
                    for each in c:
                        self.day1_outputtable.topLevelItem(outputline).setText(column, str(each))
                        print(column, outputline, each)
                        column = column + 1
                    column = 0
                if dayindex == 2: 
                    item_0 = QtWidgets.QTreeWidgetItem(self.day2_outputtable)
                    for each in c:
                        self.day2_outputtable.topLevelItem(outputline).setText(column, str(each))
                        print(column, outputline, each)
                        column = column + 1
                    column = 0
                if dayindex == 3: 
                    item_0 = QtWidgets.QTreeWidgetItem(self.day3_outputtable)
                    for each in c:
                        self.day3_outputtable.topLevelItem(outputline).setText(column, str(each))
                        print(column, outputline, each)
                        column = column + 1
                    column = 0

                outputline = outputline +1
            #self.switcher.setCurrentIndex(1)


        self.runbutton.clicked.connect(runbutton_clicked)

        def on_dayselect_changed():
            self.day_input.clear()
            self.day_input.insert(self.select_day.currentText())
        self.select_day.currentIndexChanged.connect(on_dayselect_changed)

        def on_onlycancelselect_changed():
            self.onlycancel_input.clear()
            self.onlycancel_input.insert(self.select_onlycancel.currentText())
        self.select_onlycancel.currentIndexChanged.connect(on_onlycancelselect_changed)

        def on_classselect_changed():
            self.class_input.clear()
            self.class_input.insert(self.select_class.currentText())
        self.select_class.currentIndexChanged.connect(on_classselect_changed)

        def on_dayinput_changed():
            self.select_day.setItemText(4, self.day_input.text())
        self.day_input.editingFinished.connect(on_dayinput_changed)

        def on_classinput_changed():
            self.select_class.setItemText(0, self.class_input.text())
        self.class_input.editingFinished.connect(on_classinput_changed)


from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.MyWorkingCode(MainWindow)
    sys.exit(app.exec_())
