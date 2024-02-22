# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Sextant.ui'
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
    QLineEdit, QPushButton, QSizePolicy, QTextEdit,
    QWidget)

class Ui_Sextant(object):
    def setupUi(self, Sextant):
        if not Sextant.objectName():
            Sextant.setObjectName(u"Sextant")
        Sextant.resize(540, 299)
        self.gridLayout_2 = QGridLayout(Sextant)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(Sextant)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 4, 0, 1, 1)

        self.label_6 = QLabel(Sextant)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.lineEdit_B_x = QLineEdit(Sextant)
        self.lineEdit_B_x.setObjectName(u"lineEdit_B_x")

        self.gridLayout.addWidget(self.lineEdit_B_x, 2, 1, 1, 1)

        self.lineEdit_C_x = QLineEdit(Sextant)
        self.lineEdit_C_x.setObjectName(u"lineEdit_C_x")

        self.gridLayout.addWidget(self.lineEdit_C_x, 4, 1, 1, 1)

        self.label_5 = QLabel(Sextant)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.label = QLabel(Sextant)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(Sextant)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.lineEdit_A_y = QLineEdit(Sextant)
        self.lineEdit_A_y.setObjectName(u"lineEdit_A_y")

        self.gridLayout.addWidget(self.lineEdit_A_y, 1, 3, 1, 1)

        self.lineEdit_A_x = QLineEdit(Sextant)
        self.lineEdit_A_x.setObjectName(u"lineEdit_A_x")

        self.gridLayout.addWidget(self.lineEdit_A_x, 1, 1, 1, 1)

        self.lineEdit_B_y = QLineEdit(Sextant)
        self.lineEdit_B_y.setObjectName(u"lineEdit_B_y")

        self.gridLayout.addWidget(self.lineEdit_B_y, 2, 3, 1, 1)

        self.lineEdit_C_y = QLineEdit(Sextant)
        self.lineEdit_C_y.setObjectName(u"lineEdit_C_y")

        self.gridLayout.addWidget(self.lineEdit_C_y, 4, 3, 1, 1)

        self.label_3 = QLabel(Sextant)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(10000, 20))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_4 = QLabel(Sextant)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.textEdit = QTextEdit(Sextant)
        self.textEdit.setObjectName(u"textEdit")

        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_8 = QLabel(Sextant)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout.addWidget(self.label_8)

        self.pushButton_start = QPushButton(Sextant)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout.addWidget(self.pushButton_start)

        self.pushButton_save = QPushButton(Sextant)
        self.pushButton_save.setObjectName(u"pushButton_save")

        self.horizontalLayout.addWidget(self.pushButton_save)

        self.pushButton_stop = QPushButton(Sextant)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)

        self.label_9 = QLabel(Sextant)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)


        self.gridLayout_2.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.label_10 = QLabel(Sextant)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_2.addWidget(self.label_10, 5, 0, 1, 1)


        self.retranslateUi(Sextant)

        QMetaObject.connectSlotsByName(Sextant)
    # setupUi

    def retranslateUi(self, Sextant):
        Sextant.setWindowTitle(QCoreApplication.translate("Sextant", u"Sextant", None))
        self.label_7.setText("")
        self.label_6.setText("")
        self.label_5.setText(QCoreApplication.translate("Sextant", u"\u7f57\u76d8", None))
        self.label.setText(QCoreApplication.translate("Sextant", u"\u5730\u56fe", None))
        self.label_2.setText(QCoreApplication.translate("Sextant", u"\u516d\u5206\u4eea", None))
        self.label_3.setText(QCoreApplication.translate("Sextant", u"X", None))
        self.label_4.setText(QCoreApplication.translate("Sextant", u"Y", None))
        self.label_8.setText("")
        self.pushButton_start.setText(QCoreApplication.translate("Sextant", u"Start", None))
        self.pushButton_save.setText(QCoreApplication.translate("Sextant", u"Save", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Sextant", u"Stop", None))
        self.label_9.setText("")
        self.label_10.setText(QCoreApplication.translate("Sextant", u"\u5730\u56fe\u3001\u4ed3\u5e93\u548c\u80cc\u5305\u540c\u65f6\u6253\u5f00\uff0c\u7f57\u76d8\u653e\u901a\u8d27\u9875\u7b2c\u4e00\u4e2a\uff0c\u81ea\u52a8\u70b9\u6700\u4e0a\u65b9\u516d\u5206\u4eea\uff0c\u5176\u4ed6\u4e09\u4e2a\u81ea\u884c\u5c4f\u853d\u8bcd\u7f00", None))
    # retranslateUi

