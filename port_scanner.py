import socket
import datetime
import sys

def scanner_port(host,port):
	s=socket.socket()
	s.settimeout(1)
	result=s.connect_ex((host,port))
	s.close()
	return result==0

def  get_service(port):
	try:
		return socket.getservbyport(port)
	except:
		return "Inconnu"
#Recuoeration de l'ip syr le  terminal
if len(sys.argv)!=2:
	print("Usage de python3 port_scanner.py <adresse_ip>")
	sys.exit()
host=sys.argv[1]


#Heure de debut
debut = datetime.datetime.now()
print (f"Scan de {host}...\n")
print (f"Debut:{debut.strftime('%H:%M:%S')}")
print ("-"*30)



for port in range(1,1025):
	if scanner_port(host,port):
		service=get_service(port)
		print(f"[+] Port {port:5} Ouvert -> {service}")

#Heure de fin
fin=datetime.datetime.now()
print("-"*30)
print(f"Fin:{fin.strftime('%H:%M:%S')}")

print(f"Duree:{fin-debut}")
print ("\nScan termine!")
#Test

#scanner_port("127.0.0.1",80)
#scanner_port("127.0.0.1",22)
