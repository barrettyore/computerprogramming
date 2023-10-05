import socket
while True:
    host = input("insert game code here:>")
    port = 9090

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host,port))
    while True:
        print("please wait host is decided")
        if socket.recv(1024).decode("utf-8") == "!PLAY1READY":
            play = input("r,p, or s:>")
            socket.send(play.encode("utf-8"))
            print(socket.recv(1024).decode("utf-8"))
            print("waiting for hosts action")
            print(socket.recv(1024).decode("utf-8"))
            if socket.recv(1024).decode("utf-8") == "!END":
                break
        