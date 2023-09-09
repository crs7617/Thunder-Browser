import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import  *
from PyQt5.QtGui import *
from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5 import QtWidgets


class Mainwindow(QMainWindow):
    def __init__(self,*args, **kwargs):
        super(Mainwindow, self).__init__(*args, **kwargs)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setWindowTitle("THUNDERBOLT BROWSER")
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        navbar.setFixedHeight(36)
        self.addToolBar(navbar)
        self.setWindowIcon(QtGui.QIcon(QPixmap('Screenshot_2021-08-17_at_1.22.09_AM-removebg-preview.png')))
        self.initUI()
        LogIN=QAction(QIcon('login3.png'),'logged in as Sairam',self)
        toolbar = self.addToolBar('login')
        toolbar.setFixedHeight(36)
        toolbar.addAction(LogIN)
        self.show()




        back_btn = QAction(QIcon('back4.png'),'back',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        fwd_btn=QAction(QIcon('fwd5.png'), 'Forward',self)
        fwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(fwd_btn)

        reload=QAction(QIcon('Reload.png'),'reload',self)
        reload.triggered.connect(self.browser.reload)
        navbar.addAction(reload)

        LogIN=QAction(QIcon('Reload.png'),'Logged in',self)




        def navigate_to_home(self):
            self.browser.setUrl(QUrl('http://google.com'))


        home=QAction(QIcon('Home.png'), 'Home',self)
        home.triggered.connect(lambda:navigate_to_home(self))
        navbar.addAction(home)


        def navigate_to_url(self):
            url = self.url_bar.text()
            url='http://'+url
            self.browser.setUrl(QUrl(url))

        self.url_bar = QLineEdit()
        self.url_bar.setFixedWidth(1100)
        self.url_bar.setFixedHeight(30)
        self.url_bar.returnPressed.connect(lambda:navigate_to_url(self))
        navbar.addWidget(self.url_bar)


    def initUI(self):
        menu_Bar = self.menuBar()
        a=menu_Bar.addMenu('File')
        a.addAction("edit")


        menu_Bar.addMenu('Edit')
        menu_Bar.addMenu('View')
        c=menu_Bar.addMenu('History')
        c.addAction("www.youtube.com")
        c.addAction("www.yahoo.com")
        c.addAction("www.republicworld.com")
        menu_Bar.addMenu('Bookmarks')
        menu_Bar.addMenu('Window')
        menu_Bar.addMenu('Help')
        menu_Bar.setNativeMenuBar(False)

        centralWidget = QWidget()
        lay = QVBoxLayout(centralWidget)



import tkinter as tk
import mysql.connector
from tkinter import *


def submitact():
    user = Username.get()
    passw = password.get()

    print("THUNDERBOLT BROWSER---THE FUTURE OF BROWSING")


    logintodb(user, passw)

f=open(r'/Users/armaanpatnaik/Desktop/proj.txt','w')
def logintodb(user, passw):

    if passw:
        db = mysql.connector.connect(host="localhost",
                                     user="root",
                                     password="crs7617",
                                     db="login")
        cursor = db.cursor()


    else:
        db = mysql.connector.connect(host="localhost",
                                     user="root", password="rrsm7617",
                                     db="login")
        cursor = db.cursor()

    savequery = "select * from loginpass"

    cursor.execute(savequery)
    myresult = cursor.fetchall()

    for x in myresult:
        f.write(str(x) + '\n')
        db.rollback()
        print("Welcome back",x[0])


root = tk.Tk()
root.geometry("300x300")
root.title("LOGIN ")

# Defining the first row
lblfrstrow = tk.Label(root, text="Userid -")
lblfrstrow.place(x=50, y=20)

Username = tk.Entry(root, width=35)
Username.place(x=150, y=20, width=100)

lblsecrow = tk.Label(root, text="Password -")
lblsecrow.place(x=50, y=50)

password = tk.Entry(root, width=35)
password.place(x=150, y=50, width=100)

submitbtn = tk.Button(root, text="Login",
                      bg='blue', command=submitact)
submitbtn.place(x=90, y=135, width=155)

root.mainloop()
f.close()

app=QApplication(sys.argv)
#QApplication.setApplicationName('Arrow')
path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'Thunderbolt-removebg-preview.png')
app.setWindowIcon(QIcon(path))
window=Mainwindow()
window.show()

sys.exit(app.exec_())




























