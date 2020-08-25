import requests
from colorama import Fore

token = 'TOKEN-HERE'

code = input('Invite CODE here -> ')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    'Content-Type': 'application/json',
    'Authorization': token,
  }


p = requests.post(f'https://discordapp.com/api/v8/invites/{code}', headers=headers)

if p.status_code == 200:
  print(f'{Fore.GREEN}Successfully{Fore.RESET} joined: {code}')

if p.status_code == 403:
  print(f'This user has been {Fore.RED}banned{Fore.RESET} from: {code}')

elif p.status_code == 401:
  print(f'{Fore.RED}Invalid{Fore.RESET} token.')
  
elif p.status_code == 404:
  print(f'{Fore.RED}Invalid{Fore.RESET} invite.')
