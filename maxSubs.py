import pytesseract as tess
from PIL import *
import PIL.ImageGrab
import mouse as mouse_get
import numpy as np
import io
import json
import time

from pynput.mouse import Button, Controller
mouse = Controller()

data = {}

try:
	dataJSON = open("data.json","r+")
	data = json.loads(dataJSON.read())
except Exception as e:
	print(e)
	dataJSON = open("data.json","w+")
	pass

print(mouse_get.get_position())
print(data)

def click_sys(coor, button, time1, time2):
    mouse.position = coor
    time.sleep(time1)
    mouse.press(button)
    mouse.release(button)
    time.sleep(time2)

for d in range(100):
	if True:
		tess.pytesseract.tesseract_cmd = r'C:\Users\pycol\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
		imgMatrix = np.zeros((30, 200, 3), dtype=np.uint8)
		followers = np.zeros((60, 160, 3), dtype=np.uint8)

		

		color = PIL.ImageGrab.grab().load()
		for x in range(30):
			for y in range(200):
				imgMatrix[x,y] = color[y+736, x+120]
		img = Image.fromarray(imgMatrix,"RGB")
		# img.show()
		text = tess.image_to_string(img)
		text = text[0:-3]
		text = text.replace("\n","")
		text = text.strip()
		print(text)

		

		if text not in data:

			click_sys((750, 130), Button.left, .1, 1)
			time.sleep(2)
			color = PIL.ImageGrab.grab().load()
			for x in range(30):
				for y in range(80):
					followers[x*2,y*2] = color[y+680, x+260]
					followers[x*2+1,y*2] = color[y+680, x+260]
					followers[x*2,y*2+1] = color[y+680, x+260]
					followers[x*2+1,y*2+1] = color[y+680, x+260]
			img = Image.fromarray(followers,"RGB")
			# img.show()
			num = tess.image_to_string(img)
			num = num[0:-3]
			print(num)

			data[text] = num

			with io.open("data.json",'w',encoding='utf8') as f:
				f.write(json.dumps(data));

			click_sys((947, 976), Button.left, .1, 1)
			print("escapa")
			# time.sleep(4)
			click_sys((1000, 85), Button.left, .1, 4)
		click_sys((743, 927), Button.left, .1, 1)
		print(d)
