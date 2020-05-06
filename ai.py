from client import client
import time
import numpy as np

class ai:
    def __init__ (self, client):
        self.client = client
        self.id = client.id
        self.worker_val_board = None
        self.army_val_board = None
        self.city_val_board = None
    
    def manh_dist(self,x1,y1,x2,y2):
        return abs((x2-x1) + (y2-y1))

    def get_board_xy(self, x, y):
        board = self.client.get_board()
        return board[x][y]
    
    def reasource_eval(self):
        
        numb_troops = len(self.client.get_armies(0)) + len(self.client.get_workers(0))
        food = self.client.get_resources(0)['food']
        
        try:
            self.food_val = int((numb_troops*3)/food)
        except ZeroDivisionError:
            self.food_val = 10

        prod = self.client.get_resources(0)['production']
        self.prod_val = 1

        trade = self.client.get_resources(0)['food']
        self.trade_val = 1


    
    def eval_func_worker(self, x, y):
        
        val = 0
        board = self.client.get_board()
        colectible = False
        
        for city in self.client.get_cities(self.client.id):
            if self.manh_dist(x,y,city['x'],city['y']) <= 2:
                colectible = True
                break

        if not colectible:
            return -1
        
        if board[y][x]== -1:
            return -1
        
        elif board[y][x] == 0:
            return 2*self.trade_val+ 0*self.prod_val+ 1*self.food_val
        
        elif board[y][x] ==1:
            return 2*self.trade_val+ 1*self.prod_val+ 2*self.food_val

        elif board[y][x]== 2:
            return 1*self.trade_val+ 2*self.prod_val+ 2*self.food_val

        elif board[y][x] == 3:
            return 0*self.trade_val+ 3*self.prod_val+ 2*self.food_val
        elif board[y][x] == 4:
            return 0*self.trade_val+ 1*self.prod_val+ 1*self.food_val

        
        workers = self.client.get_workers(self.client.id)
        # for worker in workers:
        #     if x == worker['x'] and y == worker['y']:
        #         return 0
        print('done')
        return val


    def eval_board(self, eval_func): #will give a value to each tile of the board given certain perameters based on the worker goals
        self.reasource_eval()
        board = self.client.get_board()
        for i in range(32):
            for k in range(32):
                board[i][k] = eval_func(k,i)
        return board
    
    def eval_move(self, value_board, gamma, x,y):
        mov_vals = [0,0,0,0,0] #n,e,s,w,null
        move_displacement = [[0,1],[1,0], [0,-1],[-1,0], [0,0]]
        relitive_cords= [[0, 0], [0, 1],  [0, -1],  [0, 2], [0, -2], [0, 3],  [0, -3],  [1, 0], [-1, 0], [1, 1], [-1, 1], [1, -1], [-1, -1], [1, 2], [-1, 2], [1, -2], [-1, -2], [2, 0], [-2, 0], [2, 1], [-2, 1], [2, -1], [-2, -1], [3, 0], [-3, 0],[6,6] ,[-6,6] ,[6,-6] ,[-6,-6], [0,6], [6,0], [0,6], [6,0]]
        def abs_vec(rel_cords):
            return np.add(rel_cords, [x,y])

        for cord in relitive_cords:
            abs_cord = abs_vec(cord)
            try: 
                val = value_board[abs_cord[0]][abs_cord[1]]
            except IndexError:
                val = -10000
            dist = abs(cord[0]) + abs(cord[1])
            val = val*(gamma**dist)
            if cord[0] > 0:
                if cord[1] > 0:
                    mov_vals[1] += val
                    mov_vals[0] += val
                
                if cord[1] == 0:
                    mov_vals[1] += val
                    
                if cord[1] < 0:
                    mov_vals[1] += val
                    mov_vals[2] += val
                
            
            if cord[0] == 0:
                if cord[1] > 0:
                    mov_vals[0] += val
                    
                if cord[1] < 0:
                    mov_vals[2] += val

            if cord[0] < 0:
                if cord[1] > 0:
                    mov_vals[3] += val
                    mov_vals[0] += val
                
                if cord[1] == 0:
                    mov_vals[3] += val
                    
                if cord[1] < 0:
                    mov_vals[3] += val
                    mov_vals[2] += val
        
        ds = move_displacement[np.argmax(mov_vals)]
        return abs_vec(ds)

    def move_workers (self):
        for worker in self.client.get_workers(self.client.id):
            dst_coards = self.eval_move(self.worker_val_board, 0.5, worker['x'], worker['y'])
            self.client.do_move_worker( worker['x'], worker['y'] ,dst_coards[0], dst_coards[1])
            self.worker_val_board[worker['y']][worker['x']] = 0
            for row in self.worker_val_board:
                print(row)

        print('')
    
    def make_move(self):
        self.worker_val_board = self.eval_board(self.eval_func_worker)
            
        waiting = True
        i = 0
        print(self.client.id)
        
        while waiting:
            
            if self.client.get_turn() == self.client.id:
                self.move_workers()
                production = self.client.get_resources(self.client.id)['production'] 
                city_loc = self.client.get_cities(self.id)[0]
                x = city_loc['x']
                y = city_loc['y']
                if production >= 8:
                    self.client.do_produce(1, x,y)
                self.client.do_end_turn()
                waiting = False
            time.sleep(.500)
            
            i += 1.0
            
    
    def play(self):

        while True:
            self.make_move()
            
                
    


# player0 = ai(client('http://localhost:8080', 'secret0', 'the_big_yeeter'))
# player1 = ai(client('http://localhost:8080', 'secret1', 'the_big_yeeter'))
# player2 = ai(client('http://localhost:8080', 'secret2', 'the_big_yeeter'))
# player3 = ai(client('http://localhost:8080', 'secret3', 'the_big_yeeter'))


# for i in range(10):
#     player0.make_move()
#     player1.make_move()
#     player2.make_move()
#     player3.make_move()

# def help(cords):
#     final = []
#     for cord in cords:
#         final.append(cord)
#         final.append([-cord[0],cord[1]])
#         final.append([cord[0],-cord[1]])
#         final.append([-cord[0],-cord[1]])
    
#     print(final)
# help([[0, 0], [0, 1], [0, 2], [0, 3], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [3, 0]])