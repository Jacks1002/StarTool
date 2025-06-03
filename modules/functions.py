import os

def func1():
    addHK = False
    n = 0
    cmd = "$lang = Get-WinUserLanguageList; $lang.Clear();"
    print('\033[93m*為默認選擇*\033[0m')
    usr1 = input(" - 英式鍵盤[\033[93mY\033[0m/N] ")
    if usr1 in ['Y','y','1','']: cmd += "$lang.Add('en-US');"; n+=1

    usr2 = input(" - 微軟拼音[\033[93mY\033[0m/N] ")
    if usr2 in ['Y','y','1','']: cmd += "$lang.Add('zh-CN');"; n+=1

    usr3 = input(" - 微軟速成[\033[93mY\033[0m/N] ")    
    if usr3 in ['Y','y','1','']:
        cmd += "$lang.Add('zh-HK');$lang.InputMethodTips.Clear();"
        addHK = True
        cmd += f"$lang[{n}].InputMethodTips.Add('0404:{{531FDEBF-9B4C-4A43-A2AA-960E8FCDC732}}{{6024B45F-5C54-11D4-B921-0080C882687E}}');"

    usr3 = input(" - 微軟倉頡[Y/\033[93mN\033[0m] ")    
    if usr3 in ['Y','y','1']:
        if not(addHK):
            cmd += "$lang.Add('zh-HK');$lang.InputMethodTips.Clear();"
            addHK = True
        cmd += "$lang.InputMethodTips.Add('0404:{531FDEBF-9B4C-4A43-A2AA-960E8FCDC732}{4BDF9F03-C7D3-11D4-B2AB-0080C882687E}');"

    usr4 = input(" - 微軟注音[Y/\033[93mN\033[0m] ")
    if usr4 in ['Y','y','1']: 
        if not(addHK):
            cmd += "$lang.Add('zh-HK');$lang.InputMethodTips.Clear();"
        cmd += "$lang.InputMethodTips.Add('0404:{B115690A-EA02-48D5-A231-E3578D2FDF80}{B2F9C502-1742-11D4-9790-0080C882687E}');"

    cmd += "Set-WinUserLanguageList -LanguageList $lang -Force"

    os.system(f"powershell -command \"{cmd}\"")
    print("\033[92;1mInput Method Enhanced successfully.")