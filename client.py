import socket
import time

soc = None
PORT = 13456
HOST = "127.0.0.1"
server_address = (HOST, PORT)

def get_color(gameMode):
    return connect_to_server(gameMode)

def connect_to_server(gameMode):
    global soc
    #Connect to the server socket
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    soc.connect(server_address)

    try:
        data = gameMode
        print('sending %d to the sever' % (data))
        soc.send(b'%d' % (data))

        returned_data = soc.recv(1024)
        if data:
            print(returned_data.decode('utf-8'))
            return int(returned_data)
        else:
            print("no data")
    except Exception:
        print("You either kill yourself or get killed!")
    finally:
        soc.close()