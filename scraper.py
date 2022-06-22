import requests
from bs4 import BeautifulSoup
import pprint

# print(soup.find_all('a'))
# print(soup.title)
# print(soup.find('a'))
# print(soup.find(id='31837479'))
# print(soup.select('.score'))
# print(votes[0].get('id'))

def sort_stories_by_votes(hnList):
    return sorted(hnList, key=lambda k: k['votes'])

def create_custom_hn(links, subtext):
    hn = []
    
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    
    return sort_stories_by_votes(hn)

res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news//p=2')

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res.text, 'html.parser')

links = soup.select('.titlelink')
subtext = soup.select('.subtext')

links2 = soup2.select('.titlelink')
subtext2 = soup2.select('.subtext')

pprint.pprint(create_custom_hn(links, subtext))


mega_links = links + links2
mega_subtext = subtext + subtext2

pprint.pprint(create_custom_hn(mega_links, mega_subtext))