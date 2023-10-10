while True:    
    import socket
    host = input("insert game code here:>")
    port = 9090

    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        while True:
            socket.connect((host,port))
            print("please wait host is decided")
            if socket.recv(1024).decode("utf-8") == "!PLAY1READY":
                play = input("r,p, or s:>")
                socket.send(play.encode("utf-8"))
                print(socket.recv(1024).decode("utf-8"))
                print("waiting for hosts action")
                print(socket.recv(1024).decode("utf-8"))
                if socket.recv(1024).decode("utf-8") == "!END":
                    break
    except:
        print("ERROR could not connect to server")
        print("things you can try:")
        print("     1. make sure you have the correct game code")
        print("     2. make sure the host server is running")
        print("     3. make sure the host server and you are connected to the same network")
        print("     4. make sure your firewall has privite network communication for this application enabled")
   
      
        