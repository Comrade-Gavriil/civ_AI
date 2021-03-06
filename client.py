import requests
import json


class client:
    def __init__(self, server_url, key, player_name):

        self.url  = server_url
        self.board_url = server_url + '/api/board'
        self.cities_url = server_url + '/api/cities'
        self.armies_url = server_url + '/api/armies'
        self.workers_url = server_url + '/api/workers'
        self.resources_url = server_url + '/api/resources'
        self.players_url = server_url + '/api/players'
        self.current_player_url = server_url + '/api/current_player'
        self.set_name_url = server_url + '/api/set_name'
        self.player_index_url = server_url + '/api/player_index'
        self.produce_url = server_url + '/api/produce'
        self.technology_url = server_url + '/api/technology'
        self.move_worker_url = server_url + '/api/move_worker'
        self.move_army_url = server_url + '/api/move_army'
        self.end_turn_url = server_url + '/api/end_turn'
        self.key = key

        id_params = {'key':self.key}
        self.id = requests.get(self.player_index_url, id_params).json()['player']

        set_name_params = {'key':self.key, 'name': player_name}
        requests.post(self.set_name_url, set_name_params)
    
    def get_board(self):
        params = {'key': self.key} 
        r = requests.get(self.board_url, params)
        data = r.json()
        board = data['board']
        return board


    def get_cities(self, player_numb):
        params = {'key': self.key} 
        r = requests.get(self.cities_url, params)
        data = r.json()
        cities_info = data['cities'][player_numb]
        return cities_info
    
    def get_armies(self, player_numb):
        params = {'key': self.key} 
        r = requests.get(self.armies_url, params)
        data = r.json()
        armies_info = data['armies'][player_numb]
        return armies_info
    
    def get_workers(self, player_numb):
        params = {'key': self.key} 
        r = requests.get(self.workers_url, params)
        data = r.json()
        workers_info = data['workers'][player_numb]
        return workers_info
    
    def get_resources(self, player_numb):
        params = {'key': self.key} 
        r = requests.get(self.resources_url, params)
        data = r.json()
        resources_info = data['resources'][player_numb]
        return resources_info
    
    def get_players(self, player_numb):
        params = {'key': self.key} 
        r = requests.get(self.players_url, params)
        data = r.json()
        players_info = data['players'][player_numb]
        return players_info
    
    def get_turn(self):
        params = {'key': self.key} 
        r = requests.get(self.current_player_url, params)
        data = r.json()
        current_player_info = data['turn']
        return current_player_info
    
    def do_produce(self, unit_type, loc_x , loc_y):
        params = {'key': self.key, 'type': unit_type, 'x': loc_x, 'y':loc_y} 
        r = requests.post(self.produce_url, params).json()
        if r['error'] != None:
            print(r)


    def do_technology(self, tek_tpye):
        params = {'key': self.key, 'type': tek_tpye} 
        r = requests.post(self.technology_url, params).json()
        if r['error'] != None:
            print(r)
    

    def do_move_worker(self, scr_x, scr_y,dst_x,dst_y):
        params = {'key': self.key, 'srcX': scr_x, 'srcY': scr_y, 'dstX': dst_x, 'dstY': dst_y } 
        r = requests.post(self.move_worker_url, params).json()
        if r['error'] != None:
            print(r)
        
    def do_move_army(self, scr_x, scr_y,dst_x,dst_y):
        params = {'key': self.key, 'srcX': scr_x, 'srcY': scr_y, 'dstX': dst_x, 'dstY': dst_y } 
        r = requests.post(self.move_army_url, params).json()
        if r['error'] != None:
            print(r)
    
    def do_end_turn(self):
        params = {'key': self.key} 
        r = requests.post(self.end_turn_url, params).json()
        if r['error'] != None:
            print(r)
    
    






# handle0 = client('http://localhost:8080', 'secret0', 'the_big_yeeter')
# handle1 = client('http://localhost:8080', 'secret1', 'my man')
# handle2 = client('http://localhost:8080', 'secret2', 'twomad 360')
# handle3 = client('http://localhost:8080', 'secret3', 'trump for 2020')
# handle1.get_board()
# print(handle0.get_cities(0))
# print(handle0.get_armies(0))
# print(handle0.get_workers(0))
# print(handle0.get_players(0))
# print(handle0.get_resources(0))
# print(handle0.get_turn())




    

