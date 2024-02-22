import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget,QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel
import pyautogui
import time
import random
import pyperclip
from pynput import mouse, keyboard
import pynput 

from Ui.Ui_Tujen_Class import Ui_Tujen


class Tujen(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Tujen()
        self.ui.setupUi(self)
        self.A = []
        self.B = []
        self.m1 = 0.4
        self.m2 = 0.5
        self.m3 = 0.6
        self.setup_logic()

    def setup_logic(self):
        
        A_screenWidth,A_screenHeight = pyautogui.size()
        x_monitor_res = A_screenWidth
        y_monitor_res = A_screenHeight
        x_t = x_monitor_res/1920
        y_t = y_monitor_res/1080
    
        # 写一个读取
        A = [int(629 * x_t), int(761 * y_t)]
        B = [int(577 * x_t), int(865 * y_t)]

        self.ui.lineEdit_A_x.setText(str(A[0]))
        self.ui.lineEdit_A_y.setText(str(A[1]))
        self.ui.lineEdit_B_x.setText(str(B[0]))
        self.ui.lineEdit_B_y.setText(str(B[1]))

        self.ui.pushButton_start.clicked.connect(self.my_start)
        self.ui.pushButton_stop.clicked.connect(self.my_stop)

    def my_start(self):
        def on_mouse_click(x, y, button, pressed):
            if button == mouse.Button.right and pressed:
                # 鼠标右键点击触发的函数1
                kan()

        def on_keyboard_press(key):
            if key == keyboard.Key.f12:
                # 键盘F12点击停止监听
                print("已停止")
                mouse_listener.stop()
                keyboard_listener.stop()

        def kan():
            print("开砍")
            pyperclip.copy('这是一片空白, 清空剪切板')
            xpos, ypos = mouse.position



        # 创建鼠标监听器
        mouse_listener = mouse.Listener(on_click=on_mouse_click)
        # 创建键盘监听器
        keyboard_listener = keyboard.Listener(on_press=on_keyboard_press)

        # 启动监听器
        mouse_listener.start()
        keyboard_listener.start()

        # 进入监听状态，直到手动停止监听
        mouse_listener.join()
        keyboard_listener.join()

    def my_stop(self):
        pass