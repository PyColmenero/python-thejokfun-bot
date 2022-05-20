import time
import mouse as mouse_get
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as kbController
from pynput.keyboard import Key
import win32clipboard
import random
from bs4 import BeautifulSoup
import requests

keyboard = kbController()
mouse = Controller()


def db_click_sys(coor, button, time1, time2):
    mouse.position = coor
    time.sleep(time1)
    mouse.press(button)
    mouse.press(button)
    mouse.release(button)
    mouse.release(button)
    time.sleep(time2)


def tr_click_sys(coor, button, time1, time2):
    mouse.position = coor
    time.sleep(time1)
    mouse.press(button)
    mouse.press(button)
    mouse.press(button)
    mouse.release(button)
    mouse.release(button)
    mouse.release(button)
    time.sleep(time2)


def click_sys(coor, button, time1, time2):
    mouse.position = coor
    time.sleep(time1)
    mouse.press(button)
    mouse.release(button)
    time.sleep(time2)


def write_sys(string, times):
    for c in string:
        keyboard.press(c)
        keyboard.release(c)
    time.sleep(times)


def copy(time1, time2):
    time.sleep(time1)
    keyboard.press(Key.ctrl)
    keyboard.press("c")
    keyboard.release(Key.ctrl)
    keyboard.release("c")
    time.sleep(time2)


def paste(time1, time2):
    time.sleep(time1)
    keyboard.press(Key.ctrl)
    keyboard.press("v")
    keyboard.release(Key.ctrl)
    keyboard.release("v")
    time.sleep(time2)

#click_sys((1428, 117), Button.left, .1, .4)
print(mouse_get.get_position())


def slice():
    mouse.position = (1500,200)
    mouse.press(Button.left)
    for x in range(1,458,2):
        mouse.position = (1500-(x),200)
        time.sleep(0.001)
    time.sleep(1.5)
    mouse.release(Button.left)
    time.sleep(.5)


meme_index = 10

if True:
    # while True: 
    for x in range(27):   
        # Click en boton + de mi perfil
        click_sys((1159, 93), Button.left, .1, 1)
        # Click en Imagen
        click_sys((918, 595), Button.left, .1, 2)
        # Click en Video
        # click_sys((918, 777), Button.left, .1, 2)
        # Click en SharedFolder
        click_sys((918, 595), Button.left, .1, 2)

        # Deslizar
        if meme_index >= 2:
            for x in range(int(meme_index/2)):
                slice()

        if True:
            if meme_index%2 == 0:
                # Click en meme arriba
                click_sys((277, 368), Button.left, .1, 2)
            else:
                # Click en meme abajo
                click_sys((277, 774), Button.left, .1, 2)

            if True:
                # Click en FlechaDerecha de Tunea
                click_sys((1202, 95), Button.left, .1, 2)

            if True:
                # Click en descipcion
                click_sys((687, 306), Button.left, .1, .5)
                #click_sys((696, 403), Button.left, .1, .5)
                write_sys("XD. Sígueme para más ;)",1)

                # Click en hashtags
                click_sys((767, 401), Button.left, .1, .5)
                # click_sys((750, 500), Button.left, .1, .5)
                write_sys("xd",2)
                click_sys((1220, 445), Button.left, .1, .5)

                # Click en Ok de Publicalo
                click_sys((1202, 95), Button.left, .1, .5)

            meme_index+=1
            
            print("Meme: "+str(meme_index))
            for x in range(10):
                for y in range(6):
                    print("Cuenta atrás:", "0"+str(x),":",str(y*10))
                    time.sleep(5)
                