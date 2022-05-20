import time
import mouse as mouse_get
from pynput.mouse import Button, Controller
from pynput.keyboard import Controller as kbController
from pynput.keyboard import Key
import win32clipboard
import random
from bs4 import BeautifulSoup
import requests
import string
import PIL.ImageGrab

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
        time.sleep(0.1)
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

def slice():
    mouse.position = (1500,200)
    mouse.press(Button.left)
    for x in range(1,461,2):
        mouse.position = (1500-(x),200)
        time.sleep(0.01)
    time.sleep(1.5)
    mouse.release(Button.left)
    time.sleep(.5)

def password():
    length = 12                      

    #define data
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation

    #combine the data
    combination = lower + upper + num #+ symbols

    #use random 
    temp = random.sample(combination,length)
    temp.append(lower[random.randint(0,len(lower)-1 )])
    temp.append(upper[random.randint(0,len(upper)-1 )])
    temp.append(num[random.randint(0,len(num)-1 )])
    #temp.append(symbols[random.randint(0,len(symbols)-1 )])

    #create the password 
    password = "".join(temp)

    #print the password
    return password;


def rellenar_form1():
    # 4 Textfields
    click_sys((1431, 169), Button.left, .1, 1)
    passw = password()
    write_sys(password()+"@gmail.com\t"+password()+"\t"+passw+"\t"+passw+"\t",1)

    # Acepto las condiciones
    click_sys((1574, 613), Button.left, .1, 1)

    # CAMBIAR EDAD
    mouse.position = (1698, 505)
    time.sleep(.1)
    mouse.press(Button.left)
    time.sleep(1)
    mouse.release(Button.left)
    time.sleep(.1)
    write_sys("2000",1)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    # SIGUIENTE
    click_sys((1630, 668), Button.left, 1, 1)

def seguir_momotizate():
    # Click en lupa
    click_sys((1522, 1010), Button.left, .1, 1)
    # Buscar
    click_sys((1441, 96), Button.left, .1, 1)
    write_sys("Momotizate",5)
    # click en el primer perfil
    click_sys((1391, 168), Button.left, .1, 3)
    # SEGUIR
    color = PIL.ImageGrab.grab().load()[1511, 194]
    r,g,b = color[0], color[1], color[2]
    if r == 126 and g == 217 and b == 87:
        click_sys((1511, 194), Button.left, .1, 1)


    # likes
    click_sys((1411, 513), Button.left, 2, 1)
    click_sys((1408, 710), Button.left, .1, 1)
    click_sys((1452, 888), Button.left, .1, 1)

    # theJOKFUN icono
    click_sys((1637, 978), Button.left, .1, 1)
    # ALEATORIOS
    click_sys((1693, 83), Button.left, .1, 3)


pos = mouse_get.get_position()

print(pos)



# while False:
time.sleep(5)
while True:
    if True:
        if True:
            # No volver a mostrar este mensaje
            click_sys((1541, 603), Button.left, .1, 1)
            # CERRAR
            click_sys((1632, 653), Button.left, .1, 1)

        # perfil
        click_sys((1805, 1000), Button.left, .1, 1)
        # REGISTRARTE
        click_sys((1602, 850), Button.left, .1, 1)

        # RELLENAR EL PRIMER FORMULARIO DE REGISTRO
        rellenar_form1()

        if True:
            # AZUL
            click_sys((1689, 490), Button.left, .1, 1)
            # REGÍSTRATE
            click_sys((1609, 700), Button.left, .1, 5)

            # SALTAR
            click_sys((1877, 95), Button.left, 2, 1)

            if True:
                # ALEATORIOS
                click_sys((1693, 83), Button.left, 2, 1)

                ran = random.randint(2,8)
                for x in range(10):
                    # click en seguir si no lo sigo ya
                    color = PIL.ImageGrab.grab().load()[1841, 132]
                    r,g,b = color[0], color[1], color[2]
                    if r == 126 and g == 217 and b == 87:
                        click_sys((1841, 132), Button.left, .1, 1)

                    # LIKE
                    click_sys((1411, 923), Button.left, .1, 2)

                    if x == ran:
                        seguir_momotizate()

                # perfil
                click_sys((1855, 1009), Button.left, .1, 1)
                # configuración
                click_sys((1871, 93), Button.left, .1, 1)
                # Cerrar sesión
                click_sys((1402, 470), Button.left, .1, 1)
                # Cerrar sesión verde
                click_sys((1634, 576), Button.left, .1, 1)

                print("CORRE ESCAPA")
                time.sleep(4)
