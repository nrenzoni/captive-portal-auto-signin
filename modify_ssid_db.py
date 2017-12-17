from getpass import getpass

def add_ssid_entry():
	while True:
		username = input("enter username: ")
		password = getpass()
		if username and password:
			break
		else:
			print('username and password cannot not be empty')