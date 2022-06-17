import os
import time
_username = ""
_password = ""

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

start_page =[" ____________________________________________________  \n",
            "|                   log_in or sign_up                 | \n",
            "| --------------------------------------------------- | \n",
            "|                                                     | \n",
            "|       sign_up                     log_in            | \n",
            "|                                                     | \n",
            "|       close                       introduce         | \n",
            "|                                                     | \n",
            "| --------------------------------------------------- | \n",
            "|    please write your choose ->                      | \n",
            "|_____________________________________________________| \n"]

_private_chat = [" ____________________________________________________  \n",
                 "|                   private chat                      | \n",
                 "| --------------------------------------------------- | \n",
                 "|                                                     | \n",
                 "|       see chat                       write chat     | \n",
                 "|                                                     | \n",
                 "|       close                                         | \n",
                 "|                                                     | \n",
                 "| --------------------------------------------------- | \n",
                 "|    please write your choose ->                      | \n",
                 "|_____________________________________________________| \n"]

introduce = """ welcome to chat app \n
                this chat app is made by nimamirvahabi \n
                github address: nima.mirvahabi.github.io/chat-app \n
                and this chat app is made by python \n

                have you ever think about chat in cmdor a shell? \n
                this chat app is made for you \n
                you can use this chat app in cmd or a shell \n
                and you can use this chat app in python \n

                in this app you can make group chat \n
                and you can make private chat \n
                i hope you enjoy this app \n
                and if you have any question \n
                you can contact me in mirvahabinima@gmail.com \n
                """

main_page =[" _____________________________________________________  \n",
            "|                   main_page                         | \n",
            "| --------------------------------------------------- | \n",
            "|                                                     | \n",
            "|       chat_with_friend                              | \n",
            "|                                                     | \n",
            "|       group_chat                                    | \n",
            "|                                                     | \n",
            "|       private_chat                                  | \n",
            "|                                                     | \n",
            "|       log_out                                       | \n",
            "|                                                     | \n",
            "|       close                                         | \n",
            "|                                                     | \n",
            "| --------------------------------------------------- | \n",
            "|    please write your choose ->                      | \n",
            "|_____________________________________________________| \n"]
def pos(x,y):
    # curser goto the x,y position

    return '\x1b[' + str(y) + ';' + str(x) + 'H'

def write_file(text,name="userpass"):
    # write text to file
    with open('./'+name+'.txt', 'w') as f:
            f.write(text)
            f.close()
def make_file(name):
    # make file
    with open('./'+name+".txt","a") as f:
        f.close()

def read_file(name="./userpass"):
    # read file
    with open('./'+name+'.txt',"r") as f:
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

def log_in():
    # log in page

    global _username,_password
    user_name = input("enter your user name:")
    password = input("enter your password:")
    if [user_name,password+"\n"] in userpass:
        print("log in success")
        _username = user_name
        _password = password

        return True
    else:
        print("log in failed")
        return False 

def sign_up():
    # sign up page

    
    user_name = input("enter your user name:")
    password = input("enter your password:")
    userpass.append(["\n"+user_name,password])  
    a = ""
    for i in range(len(userpass)):
        a += userpass[i][0] + "," + userpass[i][1]
    write_file(a)  
    make_file(user_name)

def _start_page():
    #start page that it show it and get commend

    for i in range(len(start_page)):
        print(start_page[i])
    commend = input(pos(34,19))

    if commend == "sign_up":
        # if user want to sign_up
        sign_up()
        return 1
    elif commend == "log_in":
        # if user want to log_in
        counter = 4
        while True:
            os.system("cls")
            if log_in():
                print("log in success")
                return 2

            else:
                counter -= 1
                if counter == 0:
                    print("you have tryed too many times \n wait for 5 sec and try again")
                    time.sleep(5)
                    counter = 4
                print("try again")
                time.sleep(1)
                

    elif commend == "close":
        # if user want to close the program
        exit(0)

    elif commend == "introduce":
        # if user want to see the introduce

        os.system("cls")
        print_page(introduce)
        input("press enter to continue")
        return 1

def private_chat():
    # private chat page

    global _username,_password
    choose = input()
    if choose == "see chat":
        own = read_file(_username)
        for i in range(len(own)):
            print(own[i])
    elif choose == "write chat":
        own = read_file(_username)
        for i in range(len(own)):
            print(own[i])
        write = input()
        own.append(write)
        a = ""
        for i in range(len(own)):
            a += own[i]
        write_file(a,_username)
    input("press enter to continue")

def _main_page():
    # main page that it show it and get commend
    os.system("cls")
    for i in range(len(main_page)):
        print(main_page[i])
    choose = input(pos(43,31))
    if choose == "chat_with_friend":
        # if user want to chat with friend
        os.system("cls")
        return 1
    elif choose == "group_chat":
        # if user want to group chat
        os.system("cls")
        return 2
    elif choose == "private_chat":
        # if user want to private chat
        os.system("cls")
        return 3
    elif choose == "log_out":
        # if user want to log out
        os.system("cls")
        return 4
    elif choose == "close":
        # if user want to close the program
        exit(0)








user_pass_prosses()
print_commend(logo)

#main_loop

while True:

    os.system("cls")
    
    if _start_page() == 2:
        while True:
            choose = _main_page()
            if choose == 1:
                break
            elif choose == 2:
                break
            elif choose == 3:
                for i in range(len(_private_chat)):
                    print(_private_chat[i])
                private_chat()


            elif choose == 4:
                break
            else:
                print("error")
                input("press enter to continue")

    
    os.system("cls")