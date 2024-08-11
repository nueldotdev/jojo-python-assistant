# from transformers import pipeline

# print(pipeline('sentiment-analysis')('we love you'))

import winreg

def get_installed_apps():
    apps = {}
    uninstall_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"
    registry_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, uninstall_key)
    
    for i in range(0, winreg.QueryInfoKey(registry_key)[0]):
        sub_key = winreg.EnumKey(registry_key, i)
        app_key = winreg.OpenKey(registry_key, sub_key)
        try:
            app_name = winreg.QueryValueEx(app_key, 'DisplayName')[0]
            app_path = winreg.QueryValueEx(app_key, 'InstallLocation')[0]
            apps[app_name] = app_path
        except FileNotFoundError:
            pass
    
    return apps

installed_apps = get_installed_apps()
print(installed_apps)
