import socket
import time

import os
from colorama import init, Fore, Back, Style

# init ()
init(autoreset=True)

system = input(" Enter your system\n Linux/Termux - 1\n Windows - 2\n -> ")
if system == '1':
	os.system("clear")
if system == '2':
    os.system("cls")

error = Fore.RED
Green = Fore.LIGHTGREEN_EX
White = Fore.LIGHTWHITE_EX
open_port = Fore.LIGHTGREEN_EX
closed_port = Fore.LIGHTRED_EX
print(f"""{Fore.YELLOW}
.                                                       .
 ██╗███╗░░██╗███████╗░█████╗░██████╗░███╗░░░███╗░█████╗░
 ██║████╗░██║██╔════╝██╔══██╗██╔══██╗████╗░████║██╔══██╗
 ██║██╔██╗██║█████╗░░██║░░██║██████╔╝██╔████╔██║███████║
 ██║██║╚████║██╔══╝░░██║░░██║██╔══██╗██║╚██╔╝██║██╔══██║
 ██║██║░╚███║██║░░░░░╚█████╔╝██║░░██║██║░╚═╝░██║██║░░██║
 ╚═╝╚═╝░░╚══╝╚═╝░░░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝
.                                                       .
                     V - 1.0 [port-scanner]                                      
                                                               
""")
port_scan = input(f"{White}  host ~{Green} ")
cp = input(f"{White} show closed ports? y/n ~{Green} ")
port = [16, 18, 1920, 20, 21, 22, 23, 42, 43, 47, 53, 67, 69, 80, 110, 135, 139, 443, 445, 180, 4746, 8000, 8080, 9595, 480, 3128, 3389, 4747, 6588, 1080, 5900, 8888, 1138, 1020]
print(f"{Fore.BLUE}\n •-==[SCANNING >{port_scan}]==-•\n")

for i in port:
					try:
						scan = socket.socket()
						scan.settimeout(0.5)
						scan.connect((port_scan, i))
					except socket.error:
						if cp.lower() == "y":
							print(f"\n{closed_port} [PORT >> {i} << IS CLOSED]")
					else:
						print("\n----------------------------")
						print(f" {open_port}[PORT >> {i} << IS OPEN]")
						print("----------------------------")
print(f"\n\n{Fore.LIGHTBLUE_EX}press <enter> to exit ")
input()