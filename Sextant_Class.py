
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QTabWidget,QApplication, QMainWindow, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QLabel
import pyautogui
import time
import random
import pyperclip
from pynput.mouse import Listener, Button
import keyboard

from Ui.Ui_Sextant_Class import Ui_Sextant

class Sextant(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Sextant()
        self.ui.setupUi(self)
        
        self.A = []
        self.B = []
        self.C = []
        self.mod_pool = []
        self.setup_logic()

    def setup_logic(self):
        
        A_screenWidth,A_screenHeight = pyautogui.size()
        x_monitor_res = A_screenWidth
        y_monitor_res = A_screenHeight
        x_t = x_monitor_res/1920
        y_t = y_monitor_res/1080

        # 写一个读取
        self.A = [979 *x_t, 926 * y_t]
        self.B = [158 *x_t, 618 * y_t]
        self.C = [435 *x_t, 400 * y_t]

        self.ui.lineEdit_A_x.setText(str(int(self.A[0])))
        self.ui.lineEdit_A_y.setText(str(int(self.A[1])))
        self.ui.lineEdit_B_x.setText(str(int(self.B[0])))
        self.ui.lineEdit_B_y.setText(str(int(self.B[1])))
        self.ui.lineEdit_C_x.setText(str(int(self.C[0])))
        self.ui.lineEdit_C_y.setText(str(int(self.C[1])))

        self.mod_pool = ["庄园","词缀腐化","暴怒","征服者","裂界","塑界地图","镀金","迷雾","符纹怪物","超越","战乱之殇",
            "吸引鱼","非传奇夺宝奇兵契约","额外深渊","高一阶","被捕捉的魔物","夏乌拉","保险箱","包含裂隙","先驱"]
        
        self.ui.textEdit.setText(str(self.mod_pool))
        self.ui.pushButton_start.clicked.connect(self.my_start)
        self.ui.pushButton_save.clicked.connect(self.my_save)

    def my_start(self):
        time.sleep(3)
        print("开始点六分仪")
        ran_time = 0.1
        A_screenWidth,A_screenHeight = pyautogui.size()
        x_monitor_res = A_screenWidth
        y_monitor_res = A_screenHeight
        x_coord = 0
        y_coord = 0
        iter = 0
        while iter < 60:
            pyautogui.moveTo(self.C)
            time.sleep(ran_time)

            pyautogui.click(button='right')

            time.sleep(ran_time)

            pyautogui.moveTo(self.A)
            
            time.sleep(ran_time)

            pyautogui.click(button='left')

            time.sleep(ran_time)

            pyautogui.hotkey('ctrl', 'c')
            copy_text = pyperclip.paste()

            for i in self.mod_pool:
                if i in copy_text:
                    pyautogui.moveTo(self.B)
                    time.sleep(ran_time)

                    pyautogui.click(button='right')

                    time.sleep(ran_time)
                    pyautogui.moveTo(self.A)
                    time.sleep(ran_time)

                    pyautogui.click(button='left')

                    if iter != 0 and iter%5 == 0:
                        x_coord += 70/2560 * x_monitor_res
                        y_coord = 0
                        iter = 0
                    now_x = 1726/2560 * x_monitor_res + x_coord
                    now_y = 819/1440 * y_monitor_res + y_coord
                    pyautogui.moveTo(now_x, now_y)

                    time.sleep(ran_time)

                    y_coord += 70/1440 * y_monitor_res
                    pyautogui.click(button='left')
                    iter += 1
                    print(i)
                    break
                else:
                    # 回去重复
                    pass

        print("done")

    def my_save(self):
        aim_sextant = eval(self.ui.textEdit.toPlainText())
        self.mod_pool = aim_sextant
        print(aim_sextant)