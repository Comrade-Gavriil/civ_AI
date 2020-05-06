from ai import ai
from client import client
from sys import argv
import time
import threading



args = argv
args0 = ['play.py','http://localhost:8080/', 'secret0', 'yeet0']
args1 = ['play.py','http://localhost:8080/', 'secret1', 'yeet1']
args2 = ['play.py','http://localhost:8080/', 'secret2', 'yeet2']
args3 = ['play.py','http://localhost:8080/', 'secret3', 'yeet3']

time_client = client(args0[1], args0[2], args0[3])

player0 = ai(client(args0[1], args0[2], args0[3]))
player1 = ai(client(args1[1], args1[2], args1[3]))
player2 = ai(client(args2[1], args2[2], args2[3]))
player3 = ai(client(args3[1], args3[2], args3[3]))

def waiting():
    
    while True:
        i = 0
        running = True
        while running:
            player = time_client.get_turn()
            print('waiting on %i for %i secs' % (player, i))
            time.sleep(1)
            if player != time_client.get_turn():
                running = False
            i+=1
            

print("treads")

t0 = threading.Thread(target=waiting, args=())
t1 = threading.Thread(target=player0.play, args=())
t2 = threading.Thread(target=player1.play, args=())
t3 = threading.Thread(target=player2.play, args=())
t4 = threading.Thread(target=player3.play, args=())
print("treading")

t0.start()
t1.start()
print("t2")
t2.start() 
print("t3")
t3.start() 
print("t4")
t4.start() 


t1.join()
t2.join()
t3.join()
t4.join()