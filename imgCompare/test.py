from PIL import Image, ImageGrab
import pytesseract
from compareImg import compareImg
from utils import *
from pymouse import PyMouse
import time
mouse = PyMouse()
# im2 = ImageGrab.grab((809, 271, 847, 290))
# im2.save('shimen.jpg', 'jpeg')
# 循环截图操作
# while True:
#     im2 = ImageGrab.grab((806, 722, 909, 768))
#     im2.save('now.jpg', 'jpeg')
#     if compareImg('now.jpg', 'use.jpg') > 90 :
#         print ('执行点击使用')
#         # mouse.click(857,744) 
#         mouse.press(857,744)
#         # 点击时间也要随机
#         time.sleep(getRandomfloat(1))
#         mouse.release(857,744)
#     else:
#         im2 = ImageGrab.grab((809, 271, 847, 290))
#         im2.save('now.jpg', 'jpeg')
#         if compareImg('now.jpg', 'use.jpg') > 100 :
#             print ('执行点击师门')
#             mouse.press(906,310)
#             time.sleep(getRandomfloat(1))
#             mouse.release(906,310)
#     #等待时间在1-5s随机取
#     time.sleep(getRandomInt(1,5))
