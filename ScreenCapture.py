import pyautogui


def capture():
    count = '0'
    im = pyautogui.screenshot(region=(5, 0, 255, 215))
    im.save(r'C:\ScreenCapture\screenshot' + count + '_.png')
    count = str(int(count) + 1)

    return im


mi = capture()

