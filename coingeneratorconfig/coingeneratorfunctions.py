import amino
import random
import string
import base64
from hashlib import sha1

	#coingenerator functions

def deviceIdgenerator(st : int = 69):
	ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = st))
	thedevice = '01' + (MetaSpecial := sha1(ran.encode("utf-8"))).hexdigest() + sha1(bytes.fromhex('01') + MetaSpecial.digest() + base64.b64decode("6a8tf0Meh6T4x7b0XvwEt+Xw6k8=")).hexdigest()
	return thedevice

def login(client : amino.Client, Kawaiaone123@gmail.com : str, password : str):
	try:
		client.login(Kawaiaone123@gmail.com =Kawaiaone123@gmail.com , password=password)
		print(f"Logged in {Kawaiaone123@gmail.com }\n")
	except amino.lib.util.exceptions.YouAreBanned:
		print(f"{Kawaiaone123@gmail.com } This Account Banned")
		return
	except amino.lib.util.exceptions.VerificationRequired as e:
		print(f"Verification required for {Kawaiaone123@gmail.com }")
		link = e.args[0]['url']
		print(link)
		input("Waiting for Verification >> ")
		login(client, Kawaiaone123@gmail.com , password)
	except amino.lib.util.exceptions.InvalidPassword:
		print(f"Incorrect password for {Kawaiaone123@gmail.com }")
		passx = input("Enter correct password >> ")
		login(client, Kawaiaone123@gmail.com , passx)
	except amino.lib.util.exceptions.InvalidAccountOrPassword:
		print(f"Incorrect password for {Kawaiaone123@gmail.com }")
		passx = input("Enter correct password >> ")
		login(client, Kawaiaone123@gmail.com , passx)
	except:
		return
        
        
	#coingenerator functions
