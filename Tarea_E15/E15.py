import pyautogui
import time
import os
#input()
os.system("cls")
for ciclo in range(0, 2, 1):

    res1 = int(input("""¿Marvel o DC?:
    1) Marvel
    2) DC
    3)Ambos
    4) Ninguno 
    R: """))
    res2 = input("Escribe un refrán, catchphrase, dicho popular o cita de libro o película: ")
    pastel_time = '''¿Cuál es la mejor hora del día para comer pastel?:
    Horarios: a) 8am b) 9am c) 10am d) 11am e) 12pm f) 1pm g) 2pm h) 3pm i) 4pm j) 5pm k) 6pm l) Después de las 7
    R: '''
    res3 = input(pastel_time)
    res4 = input("Ingresa una dirección de correo electrónico falsa:  ")

# CHECA LAS COORDENADAS DE LOS RADIO BUTTON EN EL FORMULARIO
    time.sleep(3)
    if res1 == 1:
        pyautogui.click(x=232, y = 443, clicks = 1)
    elif res1 == 2:
        pyautogui.click(x=229, y = 485, clicks = 1)
    elif res1 == 3:
        pyautogui.click(x=231, y = 524, clicks = 1)
    elif res1 == 4:
        pyautogui.click(x=230, y = 563, clicks = 1)
    else:
        print("Respuesta no válida en pregunta 1.")
        exit()

    pyautogui.press('tab')
    pyautogui.press('tab')

# Escribir la frase en el formulario
    pyautogui.typewrite(res2)
    pyautogui.press('tab')
    pyautogui.press('tab')

# Escoger la hora en la lista, presionando la tecla de flecha hacia abajo
    if res3 == 'a':
        for op in range(0, 1):
            pyautogui.press("Down")
    elif res3 == 'b':
        for op in range(0, 2):
            pyautogui.press("Down")
    elif res3 == 'c':
        for op in range(0, 3):
            pyautogui.press("Down")
    elif res3 == 'd':
        for op in range(0, 4):
            pyautogui.press("Down")
    elif res3 == 'e':
        for op in range(0, 5):
            pyautogui.press("Down")
    elif res3 == 'f':
        for op in range(0, 6):
            pyautogui.press("Down")
    elif res3 == 'g':
        for op in range(0, 7):
            pyautogui.press("Down")

    elif res3 == 'h':
        for op in range(0, 8):
            pyautogui.press("Down")

    elif res3 == 'i':
        for op in range(0, 9):
            pyautogui.press("Down")

    elif res3 == 'j':
        for op in range(0, 10):
            pyautogui.press("Down")

    elif res3 == 'k':
        for op in range(0, 11):
            pyautogui.press("Down")

    elif res3 == 'l':
        for op in range(0, 12):
            pyautogui.press("Down")
    else:
        print("Respuesta no válida para pregunta 3")
        exit()
    pyautogui.press('tab')
    pyautogui.press('tab')

# División de correo con arroba
    res4 = res4.split("@")

#primera parte de correo falso
    pyautogui.typewrite(res4[0])

# Escribir arroba con función hotkey
    pyautogui.hotkey('ctrl', 'alt', 'q')#@@

# segunda parte del correo falso
    pyautogui.typewrite(res4[1])
    time.sleep(3)

    pyautogui.press('tab')
    pyautogui.press('enter')

# Esperar a que cargue la nueva pantalla para enviar otra respuesta
    time.sleep(3)

# Solo se intentará enviar otra respuesta si se ha enviado solo una
    if ciclo < 1:
        pyautogui.click(x=266, y = 458, clicks = 1)
    ciclo = ciclo+1