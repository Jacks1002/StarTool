def command(cmd: str):
    cmd = cmd.split()

    if (cmd[0] == '/help' or cmd[0] == '/?') and  len(cmd) == 1:
        print("\nList of cmds:")
        print("    /exit - Exit StarTool. Same as quit.")
        print("    /help - Display this help.")
        print("    /quit - Quit StarTool.")
        print("    /clear - Clear the screen.")
        print("    /version - Get version of StarTool.")
        
    elif (cmd[0] == '/exit' or cmd[0]=='/quit') and len(cmd) == 1:
        print("Bye~")
        exit()

    elif (cmd[0] == '/clear' or cmd[0] == '/cls') and len(cmd) == 1:
        return 'clear'
    
    elif cmd[0] == '/version' and len(cmd) == 1:
        version = 'Beta-1.0.0'
        print(f"StarTool version: \033[92;1m{version}")

    else:
        print('\033[91;1mUnknown cmd. You can use /help to display cmds list.')
    return ''
    
