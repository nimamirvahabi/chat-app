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

# strat page 

start_page = """ _____________________________________________________  \n
                |                   log_in or sign_up                 | \n
                | --------------------------------------------------- | \n
                |                                                     | \n
                |       sign_up                     log_in            | \n
                |                                                     | \n
                |       close                       introduce         | \n
                |                                                     | \n
                | --------------------------------------------------- | \n
                |    please write your choose ->                      | \n
                |_____________________________________________________| \n"""


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
    with open('./userpass.txt',"r") as f:
        text = f.readlines()
        f.close()

    return text

def txt_prosses(text,by = ','):
    return (text.split(by))

def print_commend(commend,x = 2):
    #print logo that it get and show it for x sec

    print(commend)
    time.sleep(x)
    os.system("cls")

def print_page(page):
    #print page that it get and show it

    print(page)

userpass = read_file()

def user_pass_prosses():
    # user pass setup

    global userpass
    for i in range(len(read_file())):
        userpass[i] = txt_prosses(read_file()[i])












user_pass_prosses()

#main_loop

while True:

    print_commend(logo)
    print(userpass)
    exit(0)
