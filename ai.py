from client import client

class ai:
    def __init__ (self, client):
        self.client = client
        self.id = client.id
    
    def manh_dist(self,x1,y1,x2,y2):
        return abs((x2-x1) + (y2-y1))

    def get_board_xy(self, x, y):
        board = self.client.get_board()
        return board[x][y]
    
    def make_move(self):
        production = self.client.get_resources(self.id)['production'] 
        city_loc = self.client.get_cities(self.id)[0]
        x = city_loc['x']
        y = city_loc['y']

        if production >= 8:
            self.client.do_produce(1, x,y)
        self.client.do_end_turn()

player0 = ai(client('http://localhost:8080', 'secret0', 'the_big_yeeter'))
player1 = ai(client('http://localhost:8080', 'secret1', 'the_big_yeeter'))
player2 = ai(client('http://localhost:8080', 'secret2', 'the_big_yeeter'))
player3 = ai(client('http://localhost:8080', 'secret3', 'the_big_yeeter'))

for i in range(10):
    player0.make_move()
    player1.make_move()
    player2.make_move()
    player3.make_move()