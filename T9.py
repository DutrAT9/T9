#Openodulos
import os
import socket
#CloseModulos

print('''##########################################################
# [+] AUTOR:        Gabriel de Moura Dutra               #
# [+] EMAIL:        gabrieldutra-08outlook.com           #
# [+] GITHUB:       https://github.com/gabrielD9         #
# [+] FACEBOOK:     https://fb.com/gabriel.dutra.47884754#
##########################################################''')

#Define a operacao
print("1 : Add repositorios do backbox")
print("2 : Instalar ferramentas de pentest")
print("3 : PortScan")
print("4 : Instalar o tor-browser")
print("5 : Quit")
operacao = int(input("Digite operacao? "))

#RepositoriosBackbox
if operacao == 1:
	os.system("echo '# Kali linux repositories | Added by h4wPy\ndeb http://http.kali.org/kali sana main non-free contrib\ndeb http://security.kali.org/kali-security sana/updates main contrib non-free\ndeb http://repo.kali.org/kali kali-bleeding-edge main' >> /etc/apt/sources.list")
	os.system("apt-key adv --keyserver pgp.mit.edu --recv-keys ED444FF07D8D0BF6")
	os.system("echo '# Backbox repositorios| Added by h4wPy\ndeb http://ppa.launchpad.net/backbox/four/ubuntu trusty main\ndeb-src http://ppa.launchpad.net/backbox/four/ubuntu trusty main' >> /etc/apt/sources.list")
	os.system('sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 78A7ABE1')
	os.system('sudo apt-get update -m')
	

#Instalar ferramentas de pentest
elif operacao == 2:
	print("sqlmap\nAttest\nDnschef\nDotdotpwn\nFang\nJohn the rider\nJoomscan\nKismet\nLogkeys\nAmap\nArmitage\nAtshell\nOwasp\nNmap\nZenmap\nTor\nFimap\nNikto\nSetoolkit\nOpenvas\nW3af\nChunch\nReaver\nOphcrack\nAircrack-ng\nBeef\nWireshark\nScapy\nEtthercap\nHydra")
	os.system('sudo apt-get install sqlmap dnschef dotdotpwn fang john joomscan kismet logkeys amap armitage nmap zenmap tor fimap nikto setoolkit  w3af reaver ophcrack aircrack-ng beef wireshark scapy hydra')


#PortScan
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
	os.system('sudo add-apt-repository -y ppa:webupd8team/tor-browser')
	os.system('sudo apt-get update')
	os.system('sudo apt-get install tor-browser')

#Close
elif operacao == 5:
	print("BYE!!!!!!")
	os.system('clear')
	os.system('exit')

