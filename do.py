import os
import time
import platform
try:
	import phonenumbers
	import json
	import urllib.request
except ModuleNotFoundError:
	print("\n\nNo has instalado los requerimientos para usar este script, por favor escriba: bash install.sh\n")
def number_info(phone):
        info = []
        number = phonenumbers.parse(phone)
        info.append(geocoder.description_for_number(number, "es"))
        info.append(carrier.name_for_number(number, "es"))
        info.append(timezone.time_zones_for_number(number))
        return info
def ipinfo(victim_ip):
	ip = "https://ipinfo.io/"+ip_victim+"/json"
        url = urllib.request.urlopen(ip)
        tre = json.loads(url.read())
        for dato in tre:
                print(dato+":"+tre[dato])
def hom():
	def clear():
		if platform.system() == "Windows":
			os.system("cls")
		else:
			os.system("clear")
		clear()
		print("""\n\nOPCIONES:
				
			1- INFORMACION UNA DIRECCIÓN IP
			2- VER INFORMACION SOBRE UN NUMERO DE TELEFONO""")
		time.sleep(1)
		qr = input("\nIngrese una opcion >>> ")
		if qr=="1" or qr=="uno":
			victim_ip = input("\n\nIngrese la dirección IP >>> ")
			time.sleep(1)
			ipinfo(victim_ip)
		elif qr=="2" or qr=="dos":
			phone = input("\n\nIngrese el número de Telefono >>> ")
			time.sleep(1)
			number_info(phone)
		else:
			print("\nOpcion incorrecta.")
			print("Vuelva a intentarlo...")
			os.system("python3 do.py")
