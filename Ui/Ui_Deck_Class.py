# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Deck.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Deck(object):
    def setupUi(self, Deck):
        if not Deck.objectName():
            Deck.setObjectName(u"Deck")
        Deck.resize(472, 287)
        self.gridLayout_2 = QGridLayout(Deck)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_6 = QLabel(Deck)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 7, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_B_y = QLineEdit(Deck)
        self.lineEdit_B_y.setObjectName(u"lineEdit_B_y")

        self.gridLayout.addWidget(self.lineEdit_B_y, 2, 3, 1, 1)

        self.label_5 = QLabel(Deck)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.lineEdit_cal = QLineEdit(Deck)
        self.lineEdit_cal.setObjectName(u"lineEdit_cal")

        self.gridLayout.addWidget(self.lineEdit_cal, 4, 1, 1, 1)

        self.lineEdit_A_x = QLineEdit(Deck)
        self.lineEdit_A_x.setObjectName(u"lineEdit_A_x")

        self.gridLayout.addWidget(self.lineEdit_A_x, 1, 1, 1, 1)

        self.label_3 = QLabel(Deck)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(10000, 20))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.lineEdit_B_x = QLineEdit(Deck)
        self.lineEdit_B_x.setObjectName(u"lineEdit_B_x")

        self.gridLayout.addWidget(self.lineEdit_B_x, 2, 1, 1, 1)

        self.lineEdit_A_y = QLineEdit(Deck)
        self.lineEdit_A_y.setObjectName(u"lineEdit_A_y")

        self.gridLayout.addWidget(self.lineEdit_A_y, 1, 3, 1, 1)

        self.label_10 = QLabel(Deck)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 3, 1, 1, 1)

        self.label_2 = QLabel(Deck)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.label = QLabel(Deck)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_4 = QLabel(Deck)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.label_7 = QLabel(Deck)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 11, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(Deck)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.pushButton_start = QPushButton(Deck)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout.addWidget(self.pushButton_start)

        self.pushButton_save = QPushButton(Deck)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.pushButton_stop = QPushButton(Deck)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.label_9 = QLabel(Deck)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)


        self.gridLayout_2.addLayout(self.horizontalLayout, 10, 0, 1, 1)

        self.label_11 = QLabel(Deck)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_2.addWidget(self.label_11, 12, 0, 1, 1)


        self.retranslateUi(Deck)

        QMetaObject.connectSlotsByName(Deck)
    # setupUi

    def retranslateUi(self, Deck):
        Deck.setWindowTitle(QCoreApplication.translate("Deck", u"Deck", None))
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("Deck", u"\u8ba1\u6570", None))
        self.label_3.setText(QCoreApplication.translate("Deck", u"X", None))
        self.label_10.setText("")
        self.label_2.setText(QCoreApplication.translate("Deck", u"\u6309\u94ae", None))
        self.label.setText(QCoreApplication.translate("Deck", u"\u7269\u54c1", None))
        self.label_4.setText(QCoreApplication.translate("Deck", u"Y", None))
        self.label_7.setText("")
        self.label_8.setText("")
        self.pushButton_start.setText(QCoreApplication.translate("Deck", u"\u5f00\u59cb", None))
        self.pushButton_save.setText(QCoreApplication.translate("Deck", u"\u7edf\u8ba1", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Deck", u"\u6e05\u96f6", None))
        self.label_9.setText("")
        self.label_11.setText(QCoreApplication.translate("Deck", u"\u5361\u5305\u653e\u901a\u8d27\u9875\u4e0b\u9762\u7b2c\u4e8c\u4e2a", None))
    # retranslateUi

