import os

def ctext(text,cname):
    color = {
        'gray': 90,
        'red': 91,
        'green': 92,
        'yellow': 93,
        'blue': 94,
        'purple': 95,
        'cyan': 96 
    }
    return f"\033[{color[cname]}{text}\033[0m"

def main():
    if os.name != 'nt':
        input("\033[91;1mStarTool support Windows system only!")
        exit()
    os.system('cls')
    print(ctext('StarTool','blue'),'-',ctext('Your best tool in CWK.','cyan'))
    
    