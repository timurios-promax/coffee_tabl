import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import csv
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.con = sqlite3.connect("coffee.db")
        self.start.clicked.connect(self.show_table)
        self.table = WindowAdd()
        self.addCoffee.clicked.connect(self.open_editor)
        self.titles = None
        self.table.radioButton.clicked.connect(self.run)
        self.table.radioButton_2.clicked.connect(self.run)
        self.table.add.clicked.connect(self.add_coffee)

    def show_table(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffees").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.titles = ['ID', 'название сорта', 'степень обжарки', 'молотый/в зернах',
                       'описание вкуса', 'цена', 'объем упаковки']
        self.tableWidget.setColumnCount(len(self.titles))
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def open_editor(self):
        self.table.show()

    def add_coffee(self):
        cur = self.con.cursor()
        res = cur.execute(f"""INSERT INTO coffees(name, stepobjar, type, taste, price, volume)
                VALUES({self.table.lineEdit.text()}, {self.table.comboBox.currentText()},
                {self.radio}, {self.table.lineEdit_2.text()}, {self.spinBox.value()},
                {self.lineEdit_3.text()})""")
        self.con.commit()

    def run(self):
        self.radio = self.sender().text


class WindowAdd(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Добавление кофе')
        uic.loadUi('addEditCoffeeForm.ui', self)


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())