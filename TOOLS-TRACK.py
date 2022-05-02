import os
import time
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
MAGENTA = '\033[35m'
BLUE = '\033[34m' 
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
os.system("clear")



print(MAGENTA+"████████╗░█████╗░░█████╗░██╗░░░░░░██████╗░░░░░░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗")
print("╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝░░░░░░╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝")
print(CYAN+"░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░█████╗░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░")                                                                        
print("░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗╚════╝░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░")
print("░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝░░░░░░░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗")                                                                               
print("░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝ version 1.0")
a = int(input("1-KALI \n2-UBUNTU\n3-LXDE\n4-ARCH\n5-WINDOWS 10 \n>>> "))                                                                                                         


os.system("clear")
print(BLUE+"##################################################")                                                                                                               
print("##  88      a8P         db        88        88  ##")
print("##  88    .88'         d88b       88        88  ##")
print("##  88   88'          d8''8b      88        88  ##")
print("##  88 d88           d8'  '8b     88        88  ##")
print("##  8888'88.        d8YaaaaY8b    88        88  ##")
print("##  88P   Y8b      d8''''''''8b   88        88  ##")
print("##  88     '88.   d8'        '8b  88        88  ##")
print("##  88       Y8b d8'          '8b 888888888 88  ##")
print("##                                              ##")
print("####  ############# NetHunter ####################")

print("[*] Checking device architecture ...")

os.system("apt list")
print(BLUE+"[*] Import Kali")
os.system("apt update -y")
os.system("apt upgrade -y")
os.system("apt update")
os.system("apt upgrade")
os.system("pkg install wget")
os.system("termux-setup-storage")
os.system("apt-get update")
os.system("apt-get upgrade")
os.system("apt-get update")
os.system("wget -O install-nethunter-termux https://offs.ec/2MceZWr")
os.system("chmod +x install-nethunter-termux")
os.system("./install-nethunter-termux")
