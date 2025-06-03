import os
import requests


modules = [
    'https://raw.githubusercontent.com/Jacks1002/StarTool/refs/heads/main/modules/commands.py',
    'https://raw.githubusercontent.com/Jacks1002/StarTool/refs/heads/main/modules/functions.py'
]
for module in modules:
    result = requests.get(module)
    exec(result.text)

def pause():
    os.system('pause>nul')

def main():
    while True:
        clear = False
        try:
            if os.name != 'nt':
                input("\033[91;1mStarTool support Windows system only!")
                exit()
            os.system('cls & title StarTool')
            print("\033[93;1m   _____  _             \033[94;1m_______             _ ")
            print("\033[93;1m  / ____|| |           \033[94;1m|__   __|           | |\033[93;1m ⠀⠀⠀⡄⠀⠀⠀⠀⠀⣼⠀⠀")
            print("\033[93;1m | (___  | |_  __ _  _ __ \033[94;1m| |  ___    ___  | |\033[93;1m  ⠀⢀⣷⡀⠀⠀⠴⣶⣿⣶⠦")
            print("\033[93;1m  \___ \ | __|/ _` || '__|\033[94;1m| | / _ \  / _ \ | |\033[93;1m ⠐⠶⣿⣿⡿⠖⠀⠀⠀⢻⠀⠀")
            print("\033[93;1m  ____) || |_| (_| || |   \033[94;1m| || (_) || (_) || |\033[93;1m ⠀⠀⠈⣿⠁⠀⠀⠀⠀⠀⠀⠀")
            print("\033[93;1m |_____/  \__|\__,_||_|   \033[94;1m|_| \___/  \___/ |_|\033[93;1m ⠀⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀")

            print('\n\033[95;1m[1] \033[0;1mInput Method Enhancer')
            print()
            while clear == False:
                usr = input('\n\033[90;1m>> \033[0m')
                if usr[:1] == '/':
                    result = command(usr)
                    if result == 'clear': break
                if usr == '1': func1()
        except KeyboardInterrupt:
            print("\nBye~")
            exit()

if __name__=='__main__':
    main()
