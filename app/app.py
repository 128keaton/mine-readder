from collections import OrderedDict
import mcstatus, yaml, time, threading
from bottle import route, run, template, static_file, error

try:
    import gevent.monkey
    gevent.monkey.patch_all()
except:
    pass
import os
import datetime
import time
import urllib2
import HTMLParser
import praw
from bs4 import BeautifulSoup

data = {}
json_response = None

players = 0
maxPlayers = 0
username = 'BeardCraftMCBot'
password = ''
subreddit =  'beardcraftmc'       
userAgent = 'Mine_Bot_S/v1.1.0 by 128keaton'
sidebar = None

def fetch_sidebar():  

  
    r = praw.Reddit(user_agent='BeardCraftMC v1.1 by TeroTheTerror')
        
    r.login(username,password, disable_warning=True)

    sidebar = r.get_subreddit(subreddit).get_wiki_page('edit_sidebar').content_md
    return sidebar
   
   

with open('config.yml', 'r') as cfg_file:
    servers_config = yaml.load(cfg_file)

# c = 0.0
def manual_run():
    for category in servers_config:
        print category
        data[category] = {}
        for server in servers_config[category]:
            print "- " + server + ": " + servers_config[category][server]
            ip = servers_config[category][server]
            if "/" not in ip:
                ip += "/25565"
            status = mcstatus.McServer(ip.split("/")[0], ip.split("/")[1])
            # c += 1
            data[category][server] = status
            generate_json()


for category in servers_config:
    print category
    data[category] = {}
    for server in servers_config[category]:
        print "- " + server + ": " + servers_config[category][server]
        ip = servers_config[category][server]
        if "/" not in ip:
            ip += "/25565"
        status = mcstatus.McServer(ip.split("/")[0], ip.split("/")[1])
        # c += 1
        data[category][server] = status
        

def update_all():
#    i = 0.0
    for category in data:
#        d = 5.0 / c
        for server in data[category]:
#            i += 1.0
            status = data[category][server]
            threading.Thread(target=lambda: status.Update()).start()
            
def sort_dict_by_key(to_sort):
    return OrderedDict(sorted(to_sort.items(), key=lambda t: t[0]))

def generate_json():
    alive = "alive"
    dead = "dead"
    response = {}
    response[alive] = {}
    response[dead] = {}
    
    for category in data:
        response[alive][category] = {}
        response[dead][category] = []
        for server in data[category]:
            status = data[category][server]
            
            if status.available:
                response[alive][category][server] =   ', '.join(status._player_names_sample) + str(status.num_players_online) + "/" + str(status.max_players_online)
                sidebar = fetch_sidebar()
                h = HTMLParser.HTMLParser()
                sidebar_list = sidebar.split('***')
                sidebar = (sidebar_list[0] + str(status.num_players_online) + "/" + str(status.max_players_online))
                sidebar = h.unescape(sidebar)
                r = praw.Reddit(user_agent='BeardCraftMC  v1.1 by TeroTheTerror')
                r.login(username,password)
                settings = r.get_subreddit(subreddit).get_settings()
                settings['description'] = sidebar
                settings = r.get_subreddit(subreddit).update_settings(description=settings['description'])
                print "Players online", players
               
            else:
                response[dead][category].append(server)
        response[alive][category] = sort_dict_by_key(response[alive][category])
        response[dead][category].sort()
        if len(response[alive][category]) == 0:
            del response[alive][category]
        if len(response[dead][category]) == 0:
            del response[dead][category]
    response[alive] = sort_dict_by_key(response[alive])
    response[dead] = sort_dict_by_key(response[dead])
    return response

def schedule_update():
    threading.Timer(5, schedule_update).start()
    update_all()


def schedule_json():
    threading.Timer(1.5, schedule_json).start()
    global json_response
    json_response = generate_json()

@route('/status')
def index():
    return json_response

@route('/')
def server_static():
    return static_file('index.html', '..')

@error(404)
def error404(error):
    return static_file('404.html', '..')

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root = '..')

schedule_update()

schedule_json()

port = int(os.environ.get('PORT', 5000))

run(server='gevent', host='0.0.0.0', port=port)

    


