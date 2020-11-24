import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import csv
import sqlite3


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.start.clicked.connect(self.star)
        self.con = sqlite3.connect("coffee.db")
        self.modified = {}
        self.titles = None

    def star(self):
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
        self.modified = {}


app = QApplication(sys.argv)
ex = MyWidget()
ex.show()
sys.exit(app.exec_())