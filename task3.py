import requests
from pprint import pprint
res = requests.get('https://api.stackexchange.com/2.3/questions?fromdate=1655683200&todate=1655942400&order=desc&sort=activity&tagged=python&site=stackoverflow')
question_link_list = []
for person in (res.json())['items']:
    question_link_list.append(person['link'])
pprint(question_link_list)