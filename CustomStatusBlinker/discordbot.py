import requests
import random
import time
import ctypes
import json
from configparser import ConfigParser

ctypes.windll.kernel32.SetConsoleTitleW('Discord Custom Status Blinker')

file = 'config.ini'
config = ConfigParser()
config.read(file)
token = config['login']['token']
messages = ['Probs Doing Fraud','#NeverFold','Big Dick Strength','Dying','Serving the Soviet Union','B E E S E C H U R G E R']
counter = 0

def StatusChanger():
	global counter
	if counter < len(messages):
		counter += 1
	else:
		counter = 0

	try:
		session = requests.Session()
		headers = {
			'authorization': token,
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.306 Chrome/78.0.3904.130 Electron/7.1.11 Safari/537.36',
			'content-type': 'application/json'
		}
		status = messages[counter]
		data = '{"custom_status":{"text":"' + status + '"}}'
		session.patch('https://discordapp.com/api/v6/users/@me/settings', headers=headers, data=data)

		print('Status Successfully Changed To: ' + status)
	except:
		pass
	time.sleep(1)

while True:
	StatusChanger()
