<<<<<<< HEAD
from pynput import mouse as kb

mouse = controler
def pulsa(tecla):
	print('Se ha pulsado la tecla ' + str(tecla))

def suelta(tecla):
	print('Se ha soltado la tecla ' + str(tecla))
	if tecla == kb.KeyCode.from_char('q'):
		return False

escuchador = kb.Listener()
escuchador.start()

while escuchador.is_alive():
	pass
=======
from pynput import keyboard                                    
import time

count = 0 

def on_press(key):
    global count
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
        count += 1
    except AttributeError:
        print('special key {0} pressed'.format(
            key))
        count += 1
def on_release(key):
    print('{0} released'.format(
        key))
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:


    listener.join()

    time.sleep(1)
    on_release(keyboard.Key.esc)
     

       
                           
print(count)
>>>>>>> 2fa29bce84c6df76a1d25be438e08b18fe222c12
