from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
import mysql.connector


from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_button()

    def Handle_UI(self):
        self.Hide_Thems()
        self.tabWidget.tabBar().setVisible(False)


    def Handle_button(self):
        self.pushButton_2.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hide_Thems)

        ####################################################
        self.pushButton.clicked.connect(self.Day_to_day_tab)
        self.pushButton_5.clicked.connect(self.Books_tab)
        self.pushButton_4.clicked.connect(self.Users_tab)
        self.pushButton_3.clicked.connect(self.settings_Tab)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hide_Thems(self):
        self.groupBox_3.hide()

    ############################################
    #  Functions for settings, users, books, day2day
    ############################################


    def Day_to_day_tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Books_tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Users_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)

    ############################################
    #  Functions for Books tabs
    ############################################

    def addNewBooks(self):
        pass

    def editBooks(self):
        pass

    def deleteBooks(self):
        pass

    def searchBooks(self):
        pass


    ############################################
    #  Functions for for user Bar
    ############################################

    def addNewUser(self):
        pass

    def login(self):
        pass

    def EditUser(self):
        pass

    ############################################
    #  Functions for for user Bar
    ############################################


    def addCategoy(self):
        pass

    def addAuthor(self):
        pass

    def addPublisher(self):
        pass



def main():
    app =QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()