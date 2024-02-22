from pynput import keyboard, mouse
import pynput

def on_mouse_click(x, y, button, pressed):
    if button == pynput.mouse.Button.right and pressed:
        # 鼠标右键点击触发的函数1
        function1()

def on_keyboard_press(key):
    if key == pynput.keyboard.Key.f12:
        # 键盘F12点击停止监听
        mouse_listener.stop()
        keyboard_listener.stop()

def function1():
            # 实现函数1的逻辑
    print("函数1被触发！")

        # 创建鼠标监听器
mouse_listener = pynput.mouse.Listener(on_click=on_mouse_click)
        # 创建键盘监听器
keyboard_listener = pynput.keyboard.Listener(on_press=on_keyboard_press)

        # 启动监听器
mouse_listener.start()
keyboard_listener.start()

        # 进入监听状态，直到手动停止监听
mouse_listener.join()
keyboard_listener.join()

print('hello,world')