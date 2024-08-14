import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget,QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel
import pyautogui
import time
import random
import pyperclip
from pynput.mouse import Listener, Button
# import keyboard

from Alteration_Class import Alteration
from Sextant_Class import Sextant
from Tujen_Class import Tujen
from Deck_Class import Deck

pyautogui.FAILSAFE = True

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("主界面")

        self.central_widget = QWidget()
        self.layout = QVBoxLayout(self.central_widget)
        self.resize(830, 540)
        self.button_layout = QHBoxLayout()
        self.layout.addLayout(self.button_layout)
        
        self.setCentralWidget(self.central_widget)

        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        self.page1 = Alteration()
        self.tab_widget.addTab(self.page1, "改造")

        self.page2 = Sextant()
        self.tab_widget.addTab(self.page2, "六分仪")

        #self.page3 = Tujen()
        #self.tab_widget.addTab(self.page3, "图金")

        self.page4 = Deck()
        self.tab_widget.addTab(self.page4, "开卡")

        #self.page5 = Trade_card()
        #self.tab_widget.addTab(self.page4, "换卡")

    def switch_to_page1(self):
        self.tab_widget.setCurrentWidget(self.page1)

    def switch_to_page2(self):
        self.tab_widget.setCurrentWidget(self.page2)

    def switch_to_page3(self):
        self.tab_widget.setCurrentWidget(self.page3)

    def switch_to_page4(self):
        self.tab_widget.setCurrentWidget(self.page4)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()

    main_window.show()

    sys.exit(app.exec())
