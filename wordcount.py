import requests

p= requests.get('https://www.gutenberg.org/cache/epub/5200/pg5200.txt')
print(p.text)