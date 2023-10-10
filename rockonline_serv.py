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
        print("player2 is decided please wait")
        communication_socket.send(f"!PLAY1READY".encode("utf-8"))
        message = communication_socket.recv(1024).decode("utf-8")
        play2 = message
        if play1 == play2:
            print("tie, you chose the same")
            communication_socket.send(f"tie, you chose the same".encode("utf-8"))
        elif play1 == "r" and play2  == "s":
            print("you won, rock beats scissors")
            communication_socket.send(f"you lost, rock beats scissors".encode("utf-8"))

        elif play1 == "r" and play2  == "p":
            print("you lost, paper beats rock")
            communication_socket.send(f"you won, paper beats rock".encode("utf-8"))

        elif play1 == "p" and play2  == "r":
            print("you won, paper beats rock")
            communication_socket.send(f"you lost, paper beats rock".encode("utf-8"))

        elif play1 == "p" and play2  == "s":
            print("you lost, scissors beats paper")
            communication_socket.send(f"you won,scissors beats paper".encode("utf-8"))
            
        elif play1 == "s" and play2  == "r":
            print("you lost,rock beats scissoea")
            communication_socket.send(f"you won,rock beats scissors".encode("utf-8"))

        elif play1 == "s" and play2  == "p":
            print("you won,scissors beats paper")
            communication_socket.send(f"you lost,scissors beats paper".encode("utf-8"))

        else:
            print("uknown input, one of you put in a invalid input")
            communication_socket.send(f"uknown input, one of you put in a invalid input".encode("utf-8"))

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
    