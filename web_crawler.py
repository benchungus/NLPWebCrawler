from bs4 import BeautifulSoup
import requests
from collections import deque

starter_url = "https://en.wikipedia.org/wiki/Despicable_Me"

siteQueue = deque([starter_url])

visited = set()



with open('urls.txt', 'w') as f:
    counter = 0
    while counter < 15:
        currUrl = siteQueue.pop()
        visited.add(currUrl)
        r = requests.get(currUrl)
        data = r.text
        soup = BeautifulSoup(data, features="html.parser")
        sameLinkCounter = 0
# write urls to a file
        for currUrl in soup.find_all('a'):
            link_str = str(currUrl.get('href'))
            print(link_str)
            if 'Despicable' in link_str or 'despicable' in link_str:
                if link_str.startswith('/url?q='):
                    link_str = link_str[7:]
                    print('MOD:', link_str)
                if '&' in link_str:
                    i = link_str.find('&')
                    link_str = link_str[:i]
                if link_str.startswith('http') and 'google' not in link_str:
                    siteQueue.append(link_str)
                    f.write(link_str + '\n')
                    counter += 1
                    if counter >= 15:
                        break
                    

with open('urls.txt', 'r') as f:
    urls = f.read().splitlines()
for u in urls:
    print(u)

# end of program
print("end of crawler")