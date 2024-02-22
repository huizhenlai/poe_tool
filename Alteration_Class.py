import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget,QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel
import pyautogui
import time
import random
import pyperclip
from pynput.mouse import Listener, Button
import keyboard

from Ui.Ui_Alteration_Class import Ui_Alteration

class Alteration(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Alteration()
        self.ui.setupUi(self)

        self.gz = []
        self.zf = []
        self.aim = []

        self.setup_logic()

        self.need_cizhui_p = []
        self.need_cizhui_s = []

        self.ui.pushButton_start.clicked.connect(self.my_start)
        self.ui.pushButton_end.clicked.connect(self.change_flag)

        self.all_flag = 1

    def setup_logic(self):
        A_screenWidth,A_screenHeight = pyautogui.size()
        x_monitor_res = A_screenWidth
        y_monitor_res = A_screenHeight
        x_t = x_monitor_res/1920
        y_t = y_monitor_res/1080
    
        self.gz = [114*x_t, 261*y_t]
        self.zf = [236*x_t, 320*y_t]
        self.aim = [330*x_t, 390*y_t]

        self.ui.lineEdit_gz_x.setText(str(int(self.gz[0])))
        self.ui.lineEdit_gz_y.setText(str(int(self.gz[1])))
        self.ui.lineEdit_zf_x.setText(str(int(self.zf[0])))
        self.ui.lineEdit_zf_y.setText(str(int(self.zf[1])))
        self.ui.lineEdit_aim_x.setText(str(int(self.aim[0])))
        self.ui.lineEdit_aim_y.setText(str(int(self.aim[1])))
        
        self.ui.checkBox_p_1.setChecked(1)
        self.ui.lineEdit_p_1.setText("所有法术")
        self.ui.checkBox_s_1.setChecked(1)
        self.ui.lineEdit_s_1.setText(" ")
        self.ui.lineEdit_time.setText("0.1")

    def change_flag(self):
        print("停止")
        self.need_cizhui_p = []
        self.need_cizhui_s = []
        self.all_flag = 0

    def check_cizhui(self):
        if self.ui.checkBox_p_1.isChecked():
            self.need_cizhui_p.append(str(self.ui.lineEdit_p_1.text()))
        if self.ui.checkBox_p_2.isChecked():
            self.need_cizhui_p.append(str(self.ui.lineEdit_p_2.text()))
        if self.ui.checkBox_p_3.isChecked():
            self.need_cizhui_p.append(str(self.ui.lineEdit_p_3.text()))
        if self.ui.checkBox_p_4.isChecked():
            self.need_cizhui_p.append(str(self.ui.lineEdit_p_4.text()))
        if self.ui.checkBox_p_5.isChecked():
            self.need_cizhui_p.append(str(self.ui.lineEdit_p_5.text()))

        if self.ui.checkBox_s_1.isChecked():
            self.need_cizhui_s.append(str(self.ui.lineEdit_s_1.text()))
        if self.ui.checkBox_s_2.isChecked():
            self.need_cizhui_s.append(str(self.ui.lineEdit_s_2.text()))
        if self.ui.checkBox_s_3.isChecked():
            self.need_cizhui_s.append(str(self.ui.lineEdit_s_3.text()))
        if self.ui.checkBox_s_4.isChecked():
            self.need_cizhui_s.append(str(self.ui.lineEdit_s_4.text()))
        if self.ui.checkBox_s_5.isChecked():
            self.need_cizhui_s.append(str(self.ui.lineEdit_s_5.text()))

    def my_start(self):
        pyperclip.copy('这是一片空白, 清空剪切板')
        self.check_cizhui()
        self.all_flag = 1

        state_time = eval(self.ui.lineEdit_time.text())
        ran_time = state_time

        time.sleep(3)

        time.sleep(ran_time)
        print(self.gz)

        print("需要的词缀 : ")
        print(self.need_cizhui_s)
        print(self.need_cizhui_p)

        while True:
            if self.all_flag == 0:
                break
            ran_time = random.random()/5 + state_time
            time.sleep(ran_time)
            
            pyautogui.moveTo(self.gz[0], self.gz[1])
            time.sleep(ran_time)
            pyautogui.click(button='right')
            time.sleep(ran_time)

            pyautogui.moveTo(self.aim[0],self.aim[1])
            time.sleep(ran_time)
            pyautogui.click(button='left')
            time.sleep(ran_time)

            pyautogui.hotkey('ctrl', 'c')
            copy_text = pyperclip.paste()
            # print(copy_text)

            for done_str_p in self.need_cizhui_p:
                if done_str_p in copy_text:
                    for done_str_s in self.need_cizhui_s:
                        if done_str_s in copy_text:
                            self.all_flag = 0
                            print(done_str_p,"  ",done_str_s)
                            print()
                            print("完成")
                            return

            pyautogui.moveTo(self.zf[0], self.zf[1])
            time.sleep(ran_time)
            pyautogui.click(button='right')
            time.sleep(ran_time)

            pyautogui.moveTo(self.aim[0],self.aim[1])
            time.sleep(ran_time)
            pyautogui.click(button='left')
            time.sleep(ran_time)
            
            pyautogui.hotkey('ctrl', 'c')
            copy_text = pyperclip.paste()
            # print(copy_text)

            for done_str_p in self.need_cizhui_p:
                if done_str_p in copy_text:
                    for done_str_s in self.need_cizhui_s:
                        if done_str_s in copy_text:
                            self.all_flag = 0
                            print(done_str_p,"  ",done_str_s)
                            print()
                            print("完成")
                            return
                    