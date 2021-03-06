#! /usr/env/bin python2.7

'''
Start up script to populate the urls and levels hashmaps on Redis.
'''

import json
import pickle

import redis


URL_MAPS = [(1, '/clickme'), (2, '/moveforward'), (3, '/notbhajan'),
            (4, '/inserthinthere'), (5, '/ugb'), (6, '/zwibe1'),
            (7, '/answerordie'), (8, '/justmoveforward'),
            (9, '/callsomeone'), (10, '/ilovethebible'), (11, '/einstein'),
            (12, '/zwibe2'), (13, '/bvs'), (14, '/upordown'), (15, '/aorb'),
            (16, '/dress'), (17, '/gameover'), (18, '/onegame'),
            (19, '/halforfull'), (20, '/zwibe3'), (21, '/candyland'),
            (22, '/shoot'), (23, '/incest'), (24, '/pieceme'),
            (25, '/zwibe4'), (26, '/doneandusted')]

REV_URL_MAPS = [(url[1], url[0]) for url in URL_MAPS]


def add_urls(database, hashmap):
    '''
    Add URL mappins to Redis.
    '''
    for level in URL_MAPS:
        database.hset(hashmap, *level)


def add_rev_urls(database, hashmap):
    '''
    Add URL mappins to Redis.
    '''
    for level in REV_URL_MAPS:
        database.hset(hashmap, *level)


def add_levels(database=None, hashmap=None):
    '''
    Add level data to Redis.
    '''
    with open('static/scripts/parameters.json') as levels:
        data = json.loads(levels.read())
        for level in data['levels']:
            key = str(level['level'])
            data = pickle.dumps(level)
            database.hset(hashmap, key, data)


def main():
    database = database = redis.StrictRedis(host='localhost', port=6379, db=0)
    add_urls(database, 'urls')
    add_rev_urls(database, 'rev-urls')
    add_levels(database, 'levels')


if __name__ == '__main__':
    main()
