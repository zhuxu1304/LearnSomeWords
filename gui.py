# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import urllib.request
import os
import threading
from pygame import mixer
import time


class Ui_MainWindow(object):
    def __init__(self, wordlist):
        self.wordlist = wordlist

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 1280)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Wordsdisplay = QtWidgets.QTextBrowser(self.centralwidget)
        self.Wordsdisplay.setGeometry(QtCore.QRect(10, 20, 1222, 422))
        font = QtGui.QFont()
        # font.setFamily("MV Boli")
        font.setPointSize(60)
        self.Wordsdisplay.setFont(font)
        self.Wordsdisplay.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.Wordsdisplay.setAutoFillBackground(False)
        self.Wordsdisplay.setFrameShape(QtWidgets.QFrame.Panel)
        self.Wordsdisplay.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.Wordsdisplay.setTextFormat(QtCore.Qt.AutoText)
        # self.Wordsdisplay.setScaledContents(False)
        # self.Wordsdisplay.setWordWrap(False)
        # self.Wordsdisplay.setOpenExternalLinks(False)
        self.Wordsdisplay.setObjectName("Wordsdisplay")

        self.previous = QtWidgets.QPushButton(self.centralwidget)
        self.previous.setGeometry(QtCore.QRect(50, 500, 301, 241))
        self.previous.setObjectName("previous")
        labelfont = QtGui.QFont()
        labelfont.setPointSize(28)
        self.previous.setFont(labelfont)

        self.translate = QtWidgets.QPushButton(self.centralwidget)
        self.translate.setGeometry(QtCore.QRect(450, 500, 301, 241))
        self.translate.setObjectName("translate")
        self.translate.setFont(labelfont)

        self.next = QtWidgets.QPushButton(self.centralwidget)
        self.next.setGeometry(QtCore.QRect(850, 500, 301, 241))
        self.next.setObjectName("next")
        self.next.setFont(labelfont)

        self.pronounce = QtWidgets.QPushButton(self.centralwidget)
        self.pronounce.setGeometry(QtCore.QRect(450, 900, 301, 241))
        self.pronounce.setObjectName("pronounce")
        self.pronounce.setFont(labelfont)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.next.clicked.connect(lambda: self.click_next(self.wordlist))
        self.translate.clicked.connect(lambda: self.click_translate(self.wordlist))
        self.previous.clicked.connect(lambda: self.click_previous(self.wordlist))
        self.pronounce.clicked.connect(lambda: self.click_pronoucne_threading(self.wordlist))

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Learn some words!"))
        self.Wordsdisplay.setText(_translate("MainWindow", self.wordlist.curr_word))
        self.previous.setText(_translate("MainWindow", "previous"))
        self.translate.setText(_translate("MainWindow", "translate"))
        self.next.setText(_translate("MainWindow", "next"))
        self.pronounce.setText(_translate("MainWindow", "pronounce"))

    def click_next(self, wordlist):
        word = wordlist.next()
        self.Wordsdisplay.setText(word)
        # self.update()

    def click_previous(self, wordlist):
        word = wordlist.previous()
        self.Wordsdisplay.setText(word)
        # self.update()

    def click_translate(self, wordlist):
        word = wordlist.translate()
        self.Wordsdisplay.setText(word)
        # self.update()

    def update(self):
        self.Wordsdisplay.adjustSize()

    def click_pronounce(self):
        word = self.wordlist.get_current_word()
        if not os.path.exists(word + '.mp3'):
            response = self.url_open("https://dictionary.cambridge.org/dictionary/english/" + word).decode('utf-8')
            b = response.find('mp3')
            a = response.rfind('/media', 0, b)
            position = response[a:b + 3]

            with open(word + '.mp3', 'wb') as f:
                sound = self.url_open("https://dictionary.cambridge.org" + position)
                f.write(sound)

        filename = word + '.mp3'
        try:
            mixer.init()

            mixer.music.load(filename)
            mixer.music.play()


        except Exception as e:
            print(e)
            time.sleep(0.1)
            self.click_pronounce()

    def click_pronoucne_threading(self, wordlist):
        t = threading.Thread(target=self.click_pronounce)
        t.start()
        # t.join()

    def url_open(self, url):
        req = urllib.request.Request(url)
        req.add_header('User-Agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36')
        req.add_header("Referer", "https://dictionary.cambridge.org/dictionary/english/")
        response = urllib.request.urlopen(req)
        html = response.read()
        return html
