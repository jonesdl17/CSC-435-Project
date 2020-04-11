import socket
import time

soc = None
PORT = 13456
HOST = "127.0.0.1"
server_address = (HOST, PORT)

def get_color(gameMode):
    return init_connect_to_server(gameMode)

def init_connect_to_server(gameMode):
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

def send_to_server(data):
    print('trying to send')
    global soc

    print('sending %s to the sever' % (data))
    soc.send(data.encode('utf-8'))

def receive_from_server(response_lst):
    global soc
    try:
        returned_data = soc.recv(1024)
        if returned_data:
            print(returned_data.decode('utf-8'))
            response_lst.append(returned_data.decode('utf-8'))
        else:
            print("no data")
    except Exception:
        print("You either kill yourself or get killed!")

def close_socket():
    global soc
    soc.close()