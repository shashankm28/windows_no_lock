## This script will simulate a keypress and prevent Windows from locking

import pyautogui
import time

def no_lock(button):
    try:
        while True:
            pyautogui.press(button)
            time.sleep(2)

    except Exception as ex:
        print ('no_lock | Error: ', ex)

def main():
    try:
        print ('Prevent Windows lock')
        kb_button = input('Enter keyboard button: ')
        
        print ('Running')
        no_lock(kb_button)

    except Exception as ex:
        print ('main | Error: ', ex)

if __name__ == "__main__":
    main()
