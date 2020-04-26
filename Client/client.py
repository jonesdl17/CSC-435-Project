import socket
import time
import sys

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
    try:
        soc.connect(server_address)
    except Exception:
        print("Cannot Connect to ", server_address)
        print("Closing in 5 Seconds")
        time.sleep(5)
        sys.exit()
    try:
        data = gameMode
        soc.send(b'%d' % (data))

        returned_data = soc.recv(1024)
        if data:
            return int(returned_data)
        else:
            print("no data")
    except Exception:
        print("You either kill yourself or get killed!")

def send_to_server(data):
    global soc

    soc.send(data.encode('utf-8'))

def receive_from_server(response_lst):
    global soc
    try:
        returned_data = soc.recv(1024)
        if returned_data:
            response_lst.append(returned_data.decode('utf-8'))
        else:
            print("no data")
    except Exception:
        print("You either kill yourself or get killed!")

def close_socket():
    global soc
    soc.close()