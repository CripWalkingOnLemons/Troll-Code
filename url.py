from re import X
import webbrowser
import time
import os
import sys
import wmi

list=["twitch.tv/borjyyy"]

br=["chrome.exe","msedge.exe","firefox.exe"]

def browserloop():
    x=1
    while x <= 1000:
        x+=1
        for i in list:
            time.sleep(1)
            webbrowser.open(i)
    f = wmi.WMI()
  
    flag = 0
  
    # Iterating through all the running processes
    for process in f.Win32_Process():
        if br == process.Name:
            print("Application is Running")
            flag = 1
            break
  
        if flag == 0:
            browserloop()
browserloop()


