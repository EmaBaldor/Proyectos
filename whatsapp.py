import pyautogui, webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+54341111111")
sleep(10)


with open ("msj.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")

