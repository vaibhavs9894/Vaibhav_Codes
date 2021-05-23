import requests

page = requests.get('https://www.gutenberg.org/files/5200/5200-0.txt')
story = page.text

wordlist= story.lower().split()

for word in set(wordlist):
    print(f'{word} occurs {wordlist.count(word)}')