import requests
from pprint import pprint
from operator import itemgetter
def get_id(name):
    '''определяет id по введенному имени'''
    list_all_json = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    for hero in list_all_json.json():
        if hero['name'] == name:
            id_hero = hero['id']
            return id_hero


def smartest_hero(*names):
    ''''находит героя с самым высоким intelligence'''
    dic_hero_id ={}
    dic_hero_intelligence = {}
    for hero in names:
        #перебираем введенные имена героев и заносим в словарь соответствие имени и id
        dic_hero_id[hero] = get_id(hero)
    for k,v in dic_hero_id.items():
        #перербирам созданный словарь и на основании id назначаем  каждому имени его intelligence
        hero_intelligence = requests.get(f'https://akabab.github.io/superhero-api/api/powerstats/{v}.json')
        dic_hero_intelligence[k] = (hero_intelligence.json())['intelligence']
    dic_max_intelligence = sorted(dic_hero_intelligence.items(), key=itemgetter(1))
    #производим сортировку словаря по значению и выводим имя обладателя максимальной intelligence

    return f'Самый умный герой из предложенных это - {dic_max_intelligence[-1][0]}'



print(smartest_hero('Hulk', 'Captain America', 'Thanos'))
