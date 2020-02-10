import requests
import threading
import colorama
import random
import os
import ctypes
import time
from colorama import Fore,init
clear = lambda: os.system('cls')
init()
lock = threading.Lock()


viewed = 0
failed = 0
proxys = []

url = input('Item url: ')
threads = int(input('Threads: '))
clear()


def viewer():
    global viewed
    global failed
    with requests.Session() as s:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        o = s.get(url,headers=headers)
        E = 'Access Denied'
        time.sleep(1)
        if E not in o.text:
             lock.acquire()
             print(Fore.YELLOW+'[+] Sent view succesfully')
             viewed +=1
             ctypes.windll.kernel32.SetConsoleTitleW(" Ebay viewbot | Viewed: {} | Failed: {} ".format(viewed, failed, str(viewed+failed)))
             lock.release()
        else:
            lock.acquire()
            print(Fore.RED+'[-] view failed ')
            ctypes.windll.kernel32.SetConsoleTitleW(" Ebay viewbot | Viewed: {} | Failed: {} ".format(viewed, failed, str(viewed+failed)))
            failed +=1
            lock.release()
            time.sleep(0.1)



while True:
    if threading.active_count() <= threads:
        threading.Thread(target=viewer, args=(),).start()
