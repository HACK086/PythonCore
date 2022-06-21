import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0'
url = ''
x = ''
langua = input('Type "en" if you want to translate from French into English, or "fr" if you want to translate from English into French:')
word = input('Type the word you want to translate:')
print(f'You chose "{langua}" as the language to translate "{word}".')
if langua == 'en':
    url = f'https://context.reverso.net/translation/french-english/{word}'
    x = 'English'
else:
    url = f'https://context.reverso.net/translation/english-french/{word}'
    x = 'French'
response = requests.get(url, headers={'User-Agent': user_agent})
soup = BeautifulSoup(response.content, 'html.parser')
perev = [i.text.strip() for i in soup.find_all('a', class_='translation')]
primer = [element.text.strip() for element in soup.find('section', id="examples-content").find_all('span', class_="text")]

print('200 OK')
print(f'{x} Translations')
print(*perev[1:], sep='\n')
print(f'{x} Examples')
print(*primer, sep='\n')