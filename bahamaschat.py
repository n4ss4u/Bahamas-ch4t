import socket
import threading
import sys 
import os 
import time
import platform 
import random
import pickle
from colorama import Fore as f, Back as b

if platform.system() == "Windows":
  clear_console = "cls"
else:
  clear_console = "clear"

name = ""

color = random.choice(['\033[91m', '\033[92m', '\033[93m', '\033[94m', '\033[95m', '\033[96m', '\033[33m', '\033[32m', '\033[31m', '\033[36m', '\033[34m'])
reset_color = "\033[0m"

def get_username():
  global name 
  print(f.CYAN + "──▒▒▒▒▒▒───" + f.BLUE + "▄████▄")
  print(f.CYAN + "─▒─▄▒─▄▒──" + f.BLUE + "███▄█▀" + f.CYAN + "───Creador: n4ss4u")
  print(f.CYAN + "─▒▒▒▒▒▒▒─" + f.BLUE + "▐████" + f.CYAN + "──────Version: v0.1")
  print(f.CYAN + "─▒▒▒▒▒▒▒──" + f.BLUE + "█████▄" + f.CYAN + "──LOGIN BAHAMAS-CH4T")
  print(f.CYAN + "┌▒─▒─▒─▒───" + f.BLUE + "▀████▀")
  print(f.CYAN + "│")
  name = input(f.CYAN + "└─[" + f.BLUE + "BAHAMAS-CH4T ~ USUARIO" + f.CYAN + "]>>" + f.RESET + " ")

  if len(name.strip()) == 0:
    print("[!] El nombre de usuario esta vacio, precione ENTER para reintentar.")
    input()
    os.system(clear_console)
    get_username()

def send(sock,addr):
   while True:
    string = input()
    message = name + ": " + string 
    sock.sendto(color.encode("utf-8") + message.encode("utf-8") + reset_color.encode("utf-8") , addr)

    if string == '.exit':
      socket.close()
      sys.exit()


def recv(sock,addr):
   sock.sendto(name.encode("utf-8"),addr)
   while True:
      data = sock.recv(2024)
      file = open("backups.log", "a")
      file.write(data.decode() + "\n")
      file.close()

      file2 = open("backups.log", "r")
      look = file2.readlines()
      file2.close()

      if name + ":" in look[-1]:
        pass

      elif "o------->" in look[-1]:
        print("\r" + look[-1], end='', flush=True)
      
      else:
        look1 = look[-1].replace("\n", "")
        print("\r" + "~" + look[-1], end='', flush=True)


os.system(clear_console)    
print(f.CYAN + "──▒▒▒▒▒▒───" + f.BLUE + "▄████▄")
print(f.CYAN + "─▒─▄▒─▄▒──" + f.BLUE + "███▄█▀" + f.CYAN + "───Creador: n4ss4u")
print(f.CYAN + "─▒▒▒▒▒▒▒─" + f.BLUE + "▐████" + f.CYAN + "──────Version: v0.1")
print(f.CYAN + "─▒▒▒▒▒▒▒──" + f.BLUE + "█████▄" + f.CYAN + "──LOBBY BAHAMAS-CH4T")
print(f.CYAN + "┌▒─▒─▒─▒───" + f.BLUE + "▀████▀")
print(f.CYAN + "│")
print(f.CYAN + "├─[" + f.BLUE + "1" + f.CYAN + "] Entrar")
print(f.CYAN + "├─[" + f.BLUE + "2" + f.CYAN + "] Salir")
print(f.CYAN + "│")

option_menu = input(f.CYAN + "└─[" + f.BLUE + "BAHAMAS-CH4T" + f.CYAN + "]>>" + f.RESET + " ")

if option_menu == "1":
  os.system(clear_console)
  get_username()
  os.system(clear_console)
  print(f.BLUE + "║" + f.CYAN + f"          {time.localtime().tm_mday}-{time.localtime().tm_mon}-{time.localtime().tm_year}" + f.BLUE + "         ║")
  print(f.BLUE + "╚═" + f.CYAN +" Bienvenido a BAHAMAS-CH4T " + f.BLUE + "═╝" + f.RESET)


elif option_menu == "2":
  sys.exit()

else:
  sys.exit()


file = open("source.pkl", "rb")
source = "24.144.124.91"#pickle.load(file)
file.close()

socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server = (source, 9862)

tr = threading.Thread(target=recv,args=(socket,server),daemon=True)
ts = threading.Thread(target=send,args=(socket,server))
tr.start()
ts.start()
ts.join()

socket.close()
