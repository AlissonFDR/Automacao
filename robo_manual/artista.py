import pyautogui
import time
from configuracoes import *

def abrir_paint():
    pyautogui.press("win")
    time.sleep(1)

    pyautogui.write("paint", interval=0.1)
    time.sleep(1)

    pyautogui.press("enter")
    time.sleep(2)

def desenhar_contorno(contorno):

    print("Quantidade de pontos:", len(contorno))

    primeiro = contorno[0][0]

    pyautogui.moveTo(
        OFFSET_X + primeiro[0] * ESCALA,
        OFFSET_Y + primeiro[1] * ESCALA
    )

    pyautogui.mouseDown()

    for ponto in contorno:

        x, y = ponto[0]

        pyautogui.moveTo(
            OFFSET_X + x * ESCALA,
            OFFSET_Y + y * ESCALA,
            duration = VELOCIDADE
        )
    
    pyautogui.mouseUp()