import pyautogui


#shift + F10 현재 설정된파일 실행
#cltr + shif + F10은 현재 열린 파일 실행
pyautogui.sleep(1)
print('win+r키를 누릅니다...')
pyautogui.hotkey('win','r')
pyautogui.keyDown('c')
pyautogui.keyDown('m')
pyautogui.keyDown('d')
pyautogui.hotkey('enter')

fw = pyautogui.getActiveWindow()
fw.maximize()

pyautogui.sleep(2)
fw.restore()

pyautogui.keyDown('e')
pyautogui.keyDown('x')
pyautogui.keyDown('i')
pyautogui.keyDown('t')
pyautogui.sleep(2)
pyautogui.hotkey('enter')

import pyperclip