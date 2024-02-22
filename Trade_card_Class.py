import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget,QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel
import pyautogui
import time
import random
import pyperclip
from pynput.mouse import Listener, Button
import keyboard

from Ui.Ui_Deck_Trade_card import Ui_Trade_card


class Trade_card(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Deck()
        self.ui.setupUi(self)

    def setup_logic(self):
        A =  [216, 622] 
        # 通货页第二个位置
        B =  [1511, 720]
        # 背包中位置
        self.A = A
        self.B = B
        self.ui.lineEdit_A_x.setText(str(A[0]))
        self.ui.lineEdit_A_y.setText(str(A[1]))
        self.ui.lineEdit_B_x.setText(str(B[0]))
        self.ui.lineEdit_B_y.setText(str(B[1]))

    def my_start(self):
        time.sleep(3)
        while True:
            ran_time = 0.2
            pyautogui.moveTo(self.A)
            time.sleep(ran_time)
            pyautogui.click(button='right')

            time.sleep(ran_time)

            pyautogui.moveTo(self.B)
            time.sleep(ran_time)

            pyautogui.click(button='left')

            time.sleep(ran_time)
            pyautogui.keyDown('ctrl')
            time.sleep(ran_time)
            pyautogui.click(button='left')
            time.sleep(ran_time)
            pyautogui.keyUp('ctrl')
