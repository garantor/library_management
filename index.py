from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import sys
import pymysql


from PyQt5.uic import loadUiType

ui,_ = loadUiType('library.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_UI()
        self.Handle_button()

        ####################
        self.Show_author()
        self.Show_category()
        self.Show_Publisher()
        #####################
        self.Show_category_combobox()
        self.Show_author_combobox()
        self.Show_publisher_combobox()


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

        #######################################################
        self.pushButton_7.clicked.connect(self.addNewBooks)
        self.pushButton_14.clicked.connect(self.addCategory)
        self.pushButton_15.clicked.connect(self.addAuthor)
        self.pushButton_16.clicked.connect(self.addPublisher)

        self.pushButton_9.clicked.connect(self.searchBooks)

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
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()


        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_11.text()
        book_category =self.comboBox_12.currentIndex()
        book_author = self.comboBox_13.currentIndex()
        book_publisher = self.comboBox_14.currentIndex()
        book_price = self.lineEdit_12.text()


        self.cur.execute('''
        INSERT INTO book ( book_name, book_description, book_code, book_category, book_price, book_author, book_publisher)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''', (book_title, book_description, book_code, book_category, book_price, book_author, book_publisher, ))

        self.db.commit()
        self.statusBar().showMessage(book_title + ' added Successfully')

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_11.setText('')
        self.comboBox_12.setCurrentIndex(0)
        self.comboBox_13.setCurrentIndex(0)
        self.comboBox_14.setCurrentIndex(0)
        self.lineEdit_12.setText('')

    def editBooks(self):
        pass

    def deleteBooks(self):
        pass

    def searchBooks(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_3.text()

        SQL = ''' SELECT * FROM book WHERE book_name = %s'''
        self.cur.execute(SQL, [book_title])

        data = self.cur.fetchone()
        print(data)

        self.lineEdit_4.setText(data[1])
        self.textEdit_2.setPlainText(data[2])
        self.lineEdit_7.setText(data[3])
        self.comboBox_7.setCurrentIndex(4)
        self.comboBox_8.setCurrentIndex(6)
        self.comboBox_6.setCurrentIndex(7)
        self.lineEdit_8.setText(str(data[5]))


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
    #  Functions for for user Bar #
    ############################################


    def addCategory(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_5.text()

        self.cur.execute('''
        INSERT INTO category(category_name) VALUES (%s)
        ''',(category_name,))
        self.db.commit()
        self.statusBar().showMessage(category_name + ' added')
        self.lineEdit_5.setText('')
        self.Show_category()
        self.Show_category_combobox()

    def Show_category(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        category_data = self.cur.fetchall()


        if category_data:
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row, form in enumerate(category_data):
                for column, item in enumerate(form):
                    self.tableWidget_2.setItem(row,column, QTableWidgetItem(str(item)))
                    column += 1

                row_postion = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_postion)


    def addAuthor(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_6.text()

        self.cur.execute('''
               INSERT INTO author(author_name) VALUES (%s)
               ''', (author_name,))
        self.db.commit()
        self.lineEdit_6.setText('')
        self.statusBar().showMessage(author_name + ' added')
        self.Show_author()
        self.Show_author_combobox()

    def Show_author(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM author ''')
        author_data = self.cur.fetchall()

        if author_data:
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row, form in enumerate(author_data):
                for column, item in enumerate(form):
                    self.tableWidget_3.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_postion = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_postion)

    def addPublisher(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        p_name = self.lineEdit_13.text()

        self.cur.execute(''' INSERT INTO publisher(publisher_name) VALUES (%s) ''', (p_name,))
        self.db.commit()
        self.lineEdit_13.setText('')
        self.statusBar().showMessage(p_name + ' added')
        self.Show_Publisher()
        self.Show_publisher_combobox()

    def Show_Publisher(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        publisher_data = self.cur.fetchall()

        if publisher_data:
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row, form in enumerate(publisher_data):
                for column, item in enumerate(form):
                    self.tableWidget_4.setItem(row, column, QTableWidgetItem(str(item)))
                    column += 1

                row_postion = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_postion)



    def Show_category_combobox(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT category_name FROM category ''')
        combodata =self.cur.fetchall()

        self.comboBox_12.clear()
        for category in combodata:
            self.comboBox_12.addItem(category[0])
            self.comboBox_7.addItem(category[0])


    def Show_author_combobox(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM author ''')
        combodata = self.cur.fetchall()

        self.comboBox_13.clear()
        for author in combodata:
            self.comboBox_13.addItem(author[0])
            self.comboBox_8.addItem(author[0])


    def Show_publisher_combobox(self):
        self.db = pymysql.connect(host='localhost', user='root', password='Sunlabi001.', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        combodata = self.cur.fetchall()

        self.comboBox_14.clear()
        for publisher in combodata:
            self.comboBox_14.addItem(publisher[0])
            self.comboBox_6.addItem(publisher[0])



def main():
    app =QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()