import socket
def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
 
local_ip = get_local_ip()
print(f"give this to you freind",local_ip)
host = local_ip
port = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))

server.listen(5)
print("waiting for player2")
while True:
    communication_socket, adress = server.accept()
    print(f"connected to {adress}")
    while True:
        play1 = input("r,p, or s:>")
        print("play2 is decided please wait")
        communication_socket.send(f"!PLAY1READY".encode("utf-8"))
        message = communication_socket.recv(1024).decode("utf-8")
        play2 = message
        if play1 == play2:
            print("tie")
            communication_socket.send(f"tie".encode("utf-8"))
        elif play1 == "r" and play2  == "s":
            print("play1 won")
            communication_socket.send(f"play1 won".encode("utf-8"))
        elif play1 == "r" and play2  == "p":
            print("play2 won")
            communication_socket.send(f"play2 won".encode("utf-8"))
        elif play1 == "p" and play2  == "r":
            print("play1 won")
            communication_socket.send(f"play1 won".encode("utf-8"))
        elif play1 == "p" and play2  == "s":
            print("play2 won")
            communication_socket.send(f"play2 won".encode("utf-8"))
        elif play1 == "s" and play2  == "r":
            print("play2 won")
            communication_socket.send(f"play2 won".encode("utf-8"))
        elif play1 == "s" and play2  == "p":
            print("play1 won")
            communication_socket.send(f"play1 won".encode("utf-8"))
        else:
            print("unown input:>")
            communication_socket.send(f"uknown imput".encode("utf-8"))
        playagain = input("play again y/n:>")
        if playagain != "y":
            communication_socket.send(f"host has ended the game".encode("utf-8"))  
            communication_socket.send(f"!END".encode("utf-8"))   
            communication_socket.close()
            print(f"connection with {adress} ended")
            break
        else:
            communication_socket.send(f"host has contiuned the game".encode("utf-8"))
            communication_socket.send(f"!continue".encode("utf-8"))
    break   
    