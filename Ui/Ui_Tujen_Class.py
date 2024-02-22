# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Tujen.ui'
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

class Ui_Tujen(object):
    def setupUi(self, Tujen):
        if not Tujen.objectName():
            Tujen.setObjectName(u"Tujen")
        Tujen.resize(472, 287)
        self.gridLayout_2 = QGridLayout(Tujen)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Tujen)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_3 = QLabel(Tujen)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(10000, 20))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_2 = QLabel(Tujen)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_A_y = QLineEdit(Tujen)
        self.lineEdit_A_y.setObjectName(u"lineEdit_A_y")

        self.gridLayout.addWidget(self.lineEdit_A_y, 1, 3, 1, 1)

        self.lineEdit_A_x = QLineEdit(Tujen)
        self.lineEdit_A_x.setObjectName(u"lineEdit_A_x")

        self.gridLayout.addWidget(self.lineEdit_A_x, 1, 1, 1, 1)

        self.lineEdit_B_y = QLineEdit(Tujen)
        self.lineEdit_B_y.setObjectName(u"lineEdit_B_y")

        self.gridLayout.addWidget(self.lineEdit_B_y, 2, 3, 1, 1)

        self.lineEdit_B_x = QLineEdit(Tujen)
        self.lineEdit_B_x.setObjectName(u"lineEdit_B_x")

        self.gridLayout.addWidget(self.lineEdit_B_x, 2, 1, 1, 1)

        self.label_4 = QLabel(Tujen)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.label_7 = QLabel(Tujen)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 3, 0, 1, 1)

        self.label_6 = QLabel(Tujen)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(Tujen)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.pushButton_start = QPushButton(Tujen)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout.addWidget(self.pushButton_start)

        self.pushButton_save = QPushButton(Tujen)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.pushButton_stop = QPushButton(Tujen)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.label_9 = QLabel(Tujen)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)


        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)


        self.retranslateUi(Tujen)

        QMetaObject.connectSlotsByName(Tujen)
    # setupUi

    def retranslateUi(self, Tujen):
        Tujen.setWindowTitle(QCoreApplication.translate("Tujen", u"Tujen", None))
        self.label.setText(QCoreApplication.translate("Tujen", u"\u7269\u54c1", None))
        self.label_3.setText(QCoreApplication.translate("Tujen", u"X", None))
        self.label_2.setText(QCoreApplication.translate("Tujen", u"\u6309\u94ae", None))
        self.label_4.setText(QCoreApplication.translate("Tujen", u"Y", None))
        self.label_7.setText("")
        self.label_6.setText("")
        self.label_8.setText("")
        self.pushButton_start.setText(QCoreApplication.translate("Tujen", u"Start", None))
        self.pushButton_save.setText(QCoreApplication.translate("Tujen", u"Save", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Tujen", u"Stop", None))
        self.label_9.setText("")
    # retranslateUi

