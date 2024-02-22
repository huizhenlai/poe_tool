# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alteration.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Alteration(object):
    def setupUi(self, Alteration):
        if not Alteration.objectName():
            Alteration.setObjectName(u"Alteration")
        Alteration.setEnabled(True)
        Alteration.resize(730, 440)
        icon = QIcon()
        icon.addFile(u"Orb_of_Alteration_inventory_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        Alteration.setWindowIcon(icon)
        self.pushButton_start = QPushButton(Alteration)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(360, 350, 90, 50))
        font = QFont()
        font.setPointSize(14)
        self.pushButton_start.setFont(font)
        self.label_5 = QLabel(Alteration)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(250, 30, 230, 40))
        font1 = QFont()
        font1.setPointSize(20)
        self.label_5.setFont(font1)
        self.label_5.setLayoutDirection(Qt.LeftToRight)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.layoutWidget = QWidget(Alteration)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(240, 120, 221, 23))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.checkBox_p_1 = QCheckBox(self.layoutWidget)
        self.checkBox_p_1.setObjectName(u"checkBox_p_1")

        self.horizontalLayout.addWidget(self.checkBox_p_1)

        self.lineEdit_p_1 = QLineEdit(self.layoutWidget)
        self.lineEdit_p_1.setObjectName(u"lineEdit_p_1")

        self.horizontalLayout.addWidget(self.lineEdit_p_1)

        self.layoutWidget1 = QWidget(Alteration)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(240, 160, 221, 23))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.checkBox_p_2 = QCheckBox(self.layoutWidget1)
        self.checkBox_p_2.setObjectName(u"checkBox_p_2")

        self.horizontalLayout_2.addWidget(self.checkBox_p_2)

        self.lineEdit_p_2 = QLineEdit(self.layoutWidget1)
        self.lineEdit_p_2.setObjectName(u"lineEdit_p_2")

        self.horizontalLayout_2.addWidget(self.lineEdit_p_2)

        self.layoutWidget2 = QWidget(Alteration)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(240, 200, 221, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.checkBox_p_3 = QCheckBox(self.layoutWidget2)
        self.checkBox_p_3.setObjectName(u"checkBox_p_3")

        self.horizontalLayout_3.addWidget(self.checkBox_p_3)

        self.lineEdit_p_3 = QLineEdit(self.layoutWidget2)
        self.lineEdit_p_3.setObjectName(u"lineEdit_p_3")

        self.horizontalLayout_3.addWidget(self.lineEdit_p_3)

        self.layoutWidget3 = QWidget(Alteration)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(110, 360, 136, 28))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_10 = QLabel(self.layoutWidget3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_10)

        self.lineEdit_time = QLineEdit(self.layoutWidget3)
        self.lineEdit_time.setObjectName(u"lineEdit_time")
        self.lineEdit_time.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_time.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.lineEdit_time)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.label_11 = QLabel(self.layoutWidget3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.horizontalLayout_5.addWidget(self.label_11)

        self.layoutWidget_2 = QWidget(Alteration)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(490, 200, 221, 23))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.checkBox_s_3 = QCheckBox(self.layoutWidget_2)
        self.checkBox_s_3.setObjectName(u"checkBox_s_3")

        self.horizontalLayout_9.addWidget(self.checkBox_s_3)

        self.lineEdit_s_3 = QLineEdit(self.layoutWidget_2)
        self.lineEdit_s_3.setObjectName(u"lineEdit_s_3")

        self.horizontalLayout_9.addWidget(self.lineEdit_s_3)

        self.layoutWidget_3 = QWidget(Alteration)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(490, 120, 221, 23))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.checkBox_s_1 = QCheckBox(self.layoutWidget_3)
        self.checkBox_s_1.setObjectName(u"checkBox_s_1")

        self.horizontalLayout_10.addWidget(self.checkBox_s_1)

        self.lineEdit_s_1 = QLineEdit(self.layoutWidget_3)
        self.lineEdit_s_1.setObjectName(u"lineEdit_s_1")

        self.horizontalLayout_10.addWidget(self.lineEdit_s_1)

        self.layoutWidget_4 = QWidget(Alteration)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(490, 160, 221, 23))
        self.horizontalLayout_11 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.checkBox_s_2 = QCheckBox(self.layoutWidget_4)
        self.checkBox_s_2.setObjectName(u"checkBox_s_2")

        self.horizontalLayout_11.addWidget(self.checkBox_s_2)

        self.lineEdit_s_2 = QLineEdit(self.layoutWidget_4)
        self.lineEdit_s_2.setObjectName(u"lineEdit_s_2")

        self.horizontalLayout_11.addWidget(self.lineEdit_s_2)

        self.layoutWidget_5 = QWidget(Alteration)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(240, 240, 221, 23))
        self.horizontalLayout_12 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.checkBox_p_4 = QCheckBox(self.layoutWidget_5)
        self.checkBox_p_4.setObjectName(u"checkBox_p_4")

        self.horizontalLayout_12.addWidget(self.checkBox_p_4)

        self.lineEdit_p_4 = QLineEdit(self.layoutWidget_5)
        self.lineEdit_p_4.setObjectName(u"lineEdit_p_4")

        self.horizontalLayout_12.addWidget(self.lineEdit_p_4)

        self.layoutWidget_6 = QWidget(Alteration)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(240, 280, 221, 23))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.checkBox_p_5 = QCheckBox(self.layoutWidget_6)
        self.checkBox_p_5.setObjectName(u"checkBox_p_5")

        self.horizontalLayout_13.addWidget(self.checkBox_p_5)

        self.lineEdit_p_5 = QLineEdit(self.layoutWidget_6)
        self.lineEdit_p_5.setObjectName(u"lineEdit_p_5")

        self.horizontalLayout_13.addWidget(self.lineEdit_p_5)

        self.layoutWidget_7 = QWidget(Alteration)
        self.layoutWidget_7.setObjectName(u"layoutWidget_7")
        self.layoutWidget_7.setGeometry(QRect(490, 240, 221, 23))
        self.horizontalLayout_14 = QHBoxLayout(self.layoutWidget_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.checkBox_s_4 = QCheckBox(self.layoutWidget_7)
        self.checkBox_s_4.setObjectName(u"checkBox_s_4")

        self.horizontalLayout_14.addWidget(self.checkBox_s_4)

        self.lineEdit_s_4 = QLineEdit(self.layoutWidget_7)
        self.lineEdit_s_4.setObjectName(u"lineEdit_s_4")

        self.horizontalLayout_14.addWidget(self.lineEdit_s_4)

        self.layoutWidget_8 = QWidget(Alteration)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.layoutWidget_8.setGeometry(QRect(490, 280, 221, 23))
        self.horizontalLayout_15 = QHBoxLayout(self.layoutWidget_8)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.checkBox_s_5 = QCheckBox(self.layoutWidget_8)
        self.checkBox_s_5.setObjectName(u"checkBox_s_5")

        self.horizontalLayout_15.addWidget(self.checkBox_s_5)

        self.lineEdit_s_5 = QLineEdit(self.layoutWidget_8)
        self.lineEdit_s_5.setObjectName(u"lineEdit_s_5")

        self.horizontalLayout_15.addWidget(self.lineEdit_s_5)

        self.label_9 = QLabel(Alteration)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(330, 90, 41, 24))
        self.label_9.setFont(font)
        self.label_12 = QLabel(Alteration)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(580, 90, 41, 24))
        self.label_12.setFont(font)
        self.pushButton_end = QPushButton(Alteration)
        self.pushButton_end.setObjectName(u"pushButton_end")
        self.pushButton_end.setGeometry(QRect(570, 350, 90, 50))
        self.pushButton_end.setFont(font)
        self.lineEdit_aim_x = QLineEdit(Alteration)
        self.lineEdit_aim_x.setObjectName(u"lineEdit_aim_x")
        self.lineEdit_aim_x.setGeometry(QRect(109, 266, 50, 21))
        self.lineEdit_aim_x.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_aim_x.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(Alteration)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(21, 265, 57, 24))
        self.label_6.setFont(font)
        self.lineEdit_aim_y = QLineEdit(Alteration)
        self.lineEdit_aim_y.setObjectName(u"lineEdit_aim_y")
        self.lineEdit_aim_y.setGeometry(QRect(165, 266, 50, 21))
        self.lineEdit_aim_y.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_aim_y.setAlignment(Qt.AlignCenter)
        self.lineEdit_zf_x = QLineEdit(Alteration)
        self.lineEdit_zf_x.setObjectName(u"lineEdit_zf_x")
        self.lineEdit_zf_x.setGeometry(QRect(109, 208, 50, 21))
        self.lineEdit_zf_x.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_zf_x.setAlignment(Qt.AlignCenter)
        self.lineEdit_zf_y = QLineEdit(Alteration)
        self.lineEdit_zf_y.setObjectName(u"lineEdit_zf_y")
        self.lineEdit_zf_y.setGeometry(QRect(165, 208, 50, 21))
        self.lineEdit_zf_y.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_zf_y.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Alteration)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(21, 207, 82, 24))
        self.label_3.setFont(font)
        self.label = QLabel(Alteration)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(21, 149, 82, 24))
        self.label.setFont(font)
        self.lineEdit_gz_y = QLineEdit(Alteration)
        self.lineEdit_gz_y.setObjectName(u"lineEdit_gz_y")
        self.lineEdit_gz_y.setGeometry(QRect(165, 150, 50, 21))
        self.lineEdit_gz_y.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_gz_y.setAlignment(Qt.AlignCenter)
        self.lineEdit_gz_x = QLineEdit(Alteration)
        self.lineEdit_gz_x.setObjectName(u"lineEdit_gz_x")
        self.lineEdit_gz_x.setGeometry(QRect(109, 150, 50, 21))
        self.lineEdit_gz_x.setMaximumSize(QSize(50, 16777215))
        self.lineEdit_gz_x.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Alteration)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 390, 331, 51))

        self.retranslateUi(Alteration)

        QMetaObject.connectSlotsByName(Alteration)
    # setupUi

    def retranslateUi(self, Alteration):
        Alteration.setWindowTitle(QCoreApplication.translate("Alteration", u"Alteration", None))
        self.pushButton_start.setText(QCoreApplication.translate("Alteration", u"\u5f00\u59cb", None))
        self.label_5.setText(QCoreApplication.translate("Alteration", u"\u9b54\u6cd5\u7269\u54c1\u81ea\u52a8\u6539\u9020", None))
        self.checkBox_p_1.setText("")
        self.checkBox_p_2.setText("")
        self.checkBox_p_3.setText("")
        self.label_10.setText(QCoreApplication.translate("Alteration", u"\u95f4\u9694 :", None))
        self.lineEdit_time.setText("")
        self.label_11.setText(QCoreApplication.translate("Alteration", u"s", None))
        self.checkBox_s_3.setText("")
        self.checkBox_s_1.setText("")
        self.checkBox_s_2.setText("")
        self.checkBox_p_4.setText("")
        self.checkBox_p_5.setText("")
        self.checkBox_s_4.setText("")
        self.checkBox_s_5.setText("")
        self.label_9.setText(QCoreApplication.translate("Alteration", u"\u524d\u7f00", None))
        self.label_12.setText(QCoreApplication.translate("Alteration", u"\u540e\u7f00", None))
        self.pushButton_end.setText(QCoreApplication.translate("Alteration", u"\u7ed3\u675f", None))
        self.label_6.setText(QCoreApplication.translate("Alteration", u"\u76ee\u6807\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Alteration", u"\u589e\u5e45\u77f3 \uff1a", None))
        self.label.setText(QCoreApplication.translate("Alteration", u"\u6539\u9020\u77f3 \uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Alteration", u"\u8b66\u544a\uff1a\u5982\u679c\u4ec5\u9700\u8981\u5355\u524d\u7f00\uff0c\u4e5f\u9700\u8981\u5728\u540e\u7f00\u52fe\u9009\u4e00\u4e2a\u7a7a\u767d\u3002", None))
    # retranslateUi

