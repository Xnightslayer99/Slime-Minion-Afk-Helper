import pynput
from PIL import Image
import pytesseract
from time import sleep

if __name__ == __main__:
    if pytesseract.image_to_string(Image.open('afk.png')):
        keyboard.press('w')
        time.sleep(2)
        keyboard.release('w')
        keyboard.write('/play sb', delay=0.1)
    if pytesseract.image_to_string(Image.open('evac.png')):
        keyboard.write('/is', delay=0.1)