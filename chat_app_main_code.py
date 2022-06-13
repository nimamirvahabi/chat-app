import os

# github address: "https://github.com/nimamirvahabi/chat-app"

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

#main_loop

while True:

    exit(0)
