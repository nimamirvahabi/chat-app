import os
import time

# github address: "https://github.com/nimamirvahabi/chat-app"

# our logo ^_^

logo = """
        __              _                     _     _     __                  __                 _    
        [  |            / |_                  (_)   / |_  [  |                [  |               / |_  \n
        | |    .--./) `| |-'    _   _   __   __   `| |-'  | |--.      .---.   | |--.    ,--.   `| |-' \n
        | |   / /'`\;  | |     [ \ [ \ [  ] [  |   | |    | .-. |    / /'`\]  | .-. |  `'_\ :   | |   \n
        | |   \ \._//  | |,     \ \/\ \/ /   | |   | |,   | | | |    | \__.   | | | |  // | |,  | |,  \n
        [___]  .',__`   \__/      \__/\__/   [___]  \__/  [___]|__]   '.___.' [___]|__] \\'-;__/  \__/  \n
            ( ( __))                                                                                 
        """

def pos(x,y):
    # curser goto the x,y position

    return '\x1b[' + str(y) + ';' + str(x) + 'H'

def write_file(text):
    # write text to file
    with open('./userpass.txt', 'w') as f:
            f.write(text)
            f.close()
def make_file():
    # make file
    with open('./userpass.txt',"a") as f:
        f.close()

def read_file():
    # read file
    with open('./userpass',"r") as f:
        text = f.readlines()
        f.close()

    return text

def print_commend(commend,x = 2):
    #print logo that it get and show it for x sec

    print(commend)
    time.sleep(x)
    os.system("cls")


#main_loop

while True:

    print_commend(logo)
    exit(0)
