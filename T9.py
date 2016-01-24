import os
import socket

print('''##########################################################
# [+] AUTOR:        Gabriel de Moura Dutra               #
# [+] EMAIL:        gabrieldutra-08outlook.com           #
# [+] GITHUB:       https://github.com/gabrielD9         #
# [+] FACEBOOK:     https://fb.com/gabriel.dutra.47884754#
##########################################################''')

print("1 : Add repositorios do backbox")
print("2 : Instalar ferramentas de pentest")
print("3 : PortScan")
print("4 : Sair")

operacao = int(input("Digite operacao? "))

if operacao == 1:

	os.system("echo '# Backbox repositorios| Added by h4wPy\ndeb http://ppa.launchpad.net/backbox/four/ubuntu trusty main\ndeb-src http://ppa.launchpad.net/backbox/four/ubuntu trusty main' >> /etc/apt/sources.list")
	os.system('sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 78A7ABE1')
	os.system('sudo apt-get update')
	os.system('sudo apt-get upgrade')

elif operacao == 2:
	os.system('sudo apt-get install sqlmap, attest, dnschef, dotdotpwn, fang, john, joomscan, kismet, logkeys, amap, armitage, atshell, owasp, nmap, zenmap, tor, fimap, nikto, setoolkit, openvas, w3af, chunch, reaver, ophcrack, aircrack-ng, beef, wireshark, scapy, etthercap, hydra, ')


elif operacao == 3:
	host = input("Digite IP: ")
	def site_porta(host, port):

		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect((host, port))

		except socket.error:
			return False
		return True


	for port in range(21, 3306):
		if site_porta(host, port):
			print("{}  <<Porta aberta".format(port))

elif operacao == 4:
	print("BYE!!!!!")
	os.system('clear')
	os.system('exit')

