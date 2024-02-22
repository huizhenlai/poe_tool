import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget,QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel
import pyautogui
import time
import random
import pyperclip
from pynput.mouse import Listener, Button
import keyboard

from Ui.Ui_Deck_Class import Ui_Deck


class Deck(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Deck()
        self.ui.setupUi(self)
        
        self.A = []
        self.B = []

        self.card_pool = []
        self.setup_logic()
        self.num = 0
        self.ui.pushButton_start.clicked.connect(self.my_start)

    def setup_logic(self):
        
        # 通货页第二个位置
        
        # 背包中位置
        A_screenWidth,A_screenHeight = pyautogui.size()
        x_monitor_res = A_screenWidth
        y_monitor_res = A_screenHeight
        x_t = x_monitor_res/1920
        y_t = y_monitor_res/1080
        
        A =  [216 * x_t, 622 * y_t] 
        B =  [1511 * x_t, 720 *y_t]
        self.A = A
        self.B = B
        self.ui.lineEdit_A_x.setText(str(int(A[0])))
        self.ui.lineEdit_A_y.setText(str(int(A[1])))
        self.ui.lineEdit_B_x.setText(str(int(B[0])))
        self.ui.lineEdit_B_y.setText(str(int(B[1])))
        
    def my_start(self):
        time.sleep(3)
        while True:

            num = 0
            ran_time = 0.1
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

        num += 1
        self.ui.lineEdit_cal.setText(str(num))


    def calculate(self):
        pass

    def clear(self):
        self.num = 0