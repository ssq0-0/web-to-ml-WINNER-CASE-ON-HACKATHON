import requests
import time
import csv
import psycopg2
from AI.AI_model import exec
from circulation_page.models import Article


def add(text):
    cat, theme = exec(text)
    Article(full_text=text, category=cat, theme=theme).save()


def do_something():
    token = ''
    ver = '5.199'
    count = '15'

    domain = ''

    res_post = requests.get('https://api.vk.com/method/wall.get',
                 params={
                     'access_token': token,
                     'domain': domain,
                     'count': count,
                     'v': ver
                 })

    post_items = res_post.json()['response']['items']
    post_data = []

    print(str(len(post_items))+"-post_items")
    for item in post_items:
        post_data.append({'owner_id': item['owner_id'], 'post_id': item['id']})

    comments = []

    for x in post_data:
        res = requests.get('https://api.vk.com/method/wall.getComments',
                     params={
                         'access_token': token,
                         'owner_id': x['owner_id'],
                         'post_id': x['post_id'],
                         'v': ver
                     })

        com_items = res.json()['response']['items']
        print(str(len(com_items))+"-com_items")
        time.sleep(1)

        for item in com_items:
            data = item['text']
            comments.append(item["text"])
            add(data)
            print(data)



while True:
    do_something()
    time.sleep(300)
