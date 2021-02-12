import requests

#response = requests.get('https://cspweb--evgenyrahman.repl.co')
response = requests.get('https://thebrizzles.duckdns.org')
print(response.text)
if(response.status_code == 200):
  response = requests.get('https://thebrizzles.duckdns.org/admin.php')

  if(response.status_code == 200):
    print('Vulnerable site')
  else:
    print('Not a vulnerable site')
else:
  print('Request failure')
