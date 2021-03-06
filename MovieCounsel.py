#import GUI library


from PyQt5 import QtCore, QtGui, QtWidgets
# Import library for web
# scrapping

from bs4 import BeautifulSoup as SOUP
import re
import requests as HTTP


class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1069, 644)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 214, 214, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 190, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 214, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 214, 214, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/popcorn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 220, 61, 61))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("imgs/Enjoyment.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 290, 111, 31))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"font-family:Montserrat;\n"
"font-weight:bold;\n"
"color: #ffffff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #000000;\n"
"padding: 5px;\n"
"border: 2px solid #ffffff !important;\n"
"border-radius:10px;\n"

"}\n"
"QPushButton:hover{\n"
"color: #000000 !important;\n"
"background: #969898;\n"
"border-color: #969898 !important;\n"
"border-radius:10px;\n"

"}")
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 220, 61, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("imgs/Sad.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(300, 220, 61, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("imgs/Anger.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(560, 220, 61, 61))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("imgs/Anticipation.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 220, 61, 61))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("imgs/Disgust.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(820, 220, 61, 61))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("imgs/Surprise.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(700, 220, 61, 61))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("imgs/Fear.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(940, 220, 61, 61))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("imgs/Trust.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(150, 290, 111, 31))
        self.pushButton_2.setMouseTracking(False)
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"font-family:Montserrat;\n"
"font-weight:bold;\n"
"color: #ffffff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #000000;\n"
"padding: 5px;\n"
"border: 2px solid #ffffff !important;\n"
"border-radius:10px;\n"

"}\n"
"QPushButton:hover{\n"
"color: #000000 !important;\n"
"background: #969898;\n"
"border-color: #969898 !important;\n"
"border-radius:10px;\n"

"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(280, 290, 111, 31))
        self.pushButton_3.setMouseTracking(False)
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"font-family:Montserrat;\n"
"font-weight:bold;\n"
"color: #ffffff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #000000;\n"
"padding: 5px;\n"
"border: 2px solid #ffffff !important;\n"
"border-radius:10px;\n"

"}\n"
"QPushButton:hover{\n"
"color: #000000 !important;\n"
"background: #969898;\n"
"border-color: #969898 !important;\n"
"border-radius:10px;\n"

"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 290, 111, 31))
        self.pushButton_4.setMouseTracking(False)
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"font-family:Montserrat;\n"
"font-weight:bold;\n"
"color: #ffffff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #000000;\n"
"padding: 5px;\n"
"border: 2px solid #ffffff !important;\n"
"border-radius:10px;\n"

"}\n"
"QPushButton:hover{\n"
"color: #000000 !important;\n"
"background: #969898;\n"
"border-color: #969898 !important;\n"
"border-radius:10px;\n"

"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(540, 290, 111, 31))
        self.pushButton_5.setMouseTracking(False)
        self.pushButton_5.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"font-family:Montserrat;\n"
"font-weight:bold;\n"
"color: #ffffff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #000000;\n"
"padding: 5px;\n"
"border: 2px solid #ffffff !important;\n"
"border-radius:10px;\n"

"}\n"
"QPushButton:hover{\n"
"color: #000000 !important;\n"
"background: #969898;\n"
"border-color: #969898 !important;\n"
"border-radius:10px;\n"

"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(670, 290, 111, 31))
        self.pushButton_6.setMouseTracking(False)
        self.pushButton_6.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"font-family:Montserrat;\n"
"font-weight:bold;\n"
"color: #ffffff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #000000;\n"
"padding: 5px;\n"
"border: 2px solid #ffffff !important;\n"
"border-radius:10px;\n"

"}\n"
"QPushButton:hover{\n"
"color: #000000 !important;\n"
"background: #969898;\n"
"border-color: #969898 !important;\n"
"border-radius:10px;\n"

"}")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(800, 290, 111, 31))
        self.pushButton_7.setMouseTracking(False)
        self.pushButton_7.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"font-family:Montserrat;\n"
"font-weight:bold;\n"
"color: #ffffff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #000000;\n"
"padding: 5px;\n"
"border: 2px solid #ffffff !important;\n"
"border-radius:10px;\n"

"}\n"
"QPushButton:hover{\n"
"color: #000000 !important;\n"
"background: #969898;\n"
"border-color: #969898 !important;\n"
"border-radius:10px;\n"

"}")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(930, 290, 111, 31))
        self.pushButton_8.setMouseTracking(False)
        self.pushButton_8.setStyleSheet("QPushButton {\n"
"width: 50px;\n"
"font-family:Montserrat;\n"
"font-weight:bold;\n"
"color: #ffffff !important;\n"
"text-transform: uppercase;\n"
"text-decoration: none;\n"
"background: #000000;\n"
"padding: 5px;\n"
"border: 2px solid #ffffff !important;\n"
"border-radius:10px;\n"

"}\n"
"QPushButton:hover{\n"
"color: #000000 !important;\n"
"background: #969898;\n"
"border-color: #969898 !important;\n"
"border-radius:10px;\n"

"}")
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(80, 70, 871, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_9.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(140, 430, 841, 161))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(179, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 212, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 212, 214, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(179, 189, 190))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 212, 214))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 212, 214, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(211, 212, 214, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_10.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(18)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(80, 370, 711, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_11.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(0, 0, 1071, 641))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("imgs/background3.jpg"))
        self.label_12.setScaledContents(True)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(900, 610, 161, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_13.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Montserrat Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_12.raise_()
        self.label.raise_()
        self.pushButton.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_13.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #define what button does when clicked
        #calls webscrappe function when clicked passing the emotion argument
        
        self.pushButton.clicked.connect(lambda: self.webscrape("Enjoyment"))
        self.pushButton_2.clicked.connect(lambda: self.webscrape("Sad"))
        self.pushButton_3.clicked.connect(lambda: self.webscrape("Anger"))
        self.pushButton_4.clicked.connect(lambda: self.webscrape("Disgust"))
        self.pushButton_5.clicked.connect(lambda: self.webscrape("Anticipation"))
        self.pushButton_6.clicked.connect(lambda: self.webscrape("Fear"))
        self.pushButton_7.clicked.connect(lambda: self.webscrape("Surprise"))
        self.pushButton_8.clicked.connect(lambda: self.webscrape("Trust"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MovieCounsel"))
        self.pushButton.setText(_translate("MainWindow", "Happy"))
        self.pushButton_2.setText(_translate("MainWindow", "Sad"))
        self.pushButton_3.setText(_translate("MainWindow", "Angry"))
        self.pushButton_4.setText(_translate("MainWindow", "Disgusted"))
        self.pushButton_5.setText(_translate("MainWindow", "Thoughtful"))
        self.pushButton_6.setText(_translate("MainWindow", "Scared"))
        self.pushButton_7.setText(_translate("MainWindow", "Surprised"))
        self.pushButton_8.setText(_translate("MainWindow", "Trusting"))
        self.label_9.setText(_translate("MainWindow", "How are you feeling today ?"))

        self.label_13.setText(_translate("MainWindow", "?? Shoaib Areeb 2021"))
    def webscrape(self, emotion):
                _translate = QtCore.QCoreApplication.translate #required for updating label through functions
                # IMDb Url for Drama genre of
                # movie against emotion Sad
                if(emotion == "Sad"):
                        urlhere = 'http://www.imdb.com/search/title?genres=drama&title_type=feature&sort=moviemeter, asc'

                # IMDb Url for Musical genre of
                # movie against emotion Disgust
                elif(emotion == "Disgust"):
                        urlhere = 'http://www.imdb.com/search/title?genres=musical&title_type=feature&sort=moviemeter, asc'

                # IMDb Url for Family genre of
                # movie against emotion Anger
                elif(emotion == "Anger"):
                        urlhere = 'http://www.imdb.com/search/title?genres=family&title_type=feature&sort=moviemeter, asc'

                # IMDb Url for Thriller genre of
                # movie against emotion Anticipation
                elif(emotion == "Anticipation"):
                        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

                # IMDb Url for Sport genre of
                # movie against emotion Fear
                elif(emotion == "Fear"):
                        urlhere = 'http://www.imdb.com/search/title?genres=sport&title_type=feature&sort=moviemeter, asc'

                # IMDb Url for Thriller genre of
                # movie against emotion Enjoyment
                elif(emotion == "Enjoyment"):
                        urlhere = 'http://www.imdb.com/search/title?genres=thriller&title_type=feature&sort=moviemeter, asc'

                # IMDb Url for Western genre of
                # movie against emotion Trust
                elif(emotion == "Trust"):
                        urlhere = 'http://www.imdb.com/search/title?genres=western&title_type=feature&sort=moviemeter, asc'

                # IMDb Url for Film_noir genre of
                # movie against emotion Surprise
                elif(emotion == "Surprise"):
                        urlhere = 'http://www.imdb.com/search/title?genres=film_noir&title_type=feature&sort=moviemeter, asc'

                # HTTP request to get the data of
                # the whole page
                response = HTTP.get(urlhere)
                data = response.text


                # Parsing the data using
                # BeautifulSoup
                soup = SOUP(data, "lxml")

                # Extract movie titles from the
                # data using regex
                title = soup.find_all("a", attrs = {"href" : re.compile(r'\/title\/tt+\d*\/')})
                

                a = title
                count = 0
                ans=""
                for i in a:
                        tmp = str(i).split('>')
                
                        if(len(tmp) == 3):
                                ans= ans+tmp[1][:-3]+"\n"
                                
                        
                
                        if(count > 13):
                                break
                        count+=1 
                #instead of printing output in console we change the label text
                self.label_11.setText(_translate("MainWindow", "Here are some movies you can watch then :"))
                self.label_10.setText(_translate("MainWindow", ans))    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
