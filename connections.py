import socket

def readresponse(page):
    file = open(page, "r")
    response = file.read()
    return(response)

def edit_response(page, var, replace_with):
    response_to_edit = readresponse(page).split(var)
    response = ""
    for piece in range(len(response_to_edit)):
        response = response + response_to_edit[piece]
        if piece < len(response_to_edit) -1:
            response = response + replace_with
    print(response)
    return(response)

def hostconn(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((host, port))
    print("socketmade")
    sock.listen()
    while True:
        conn, adrr = sock.accept()
        print("connection accepted")
        request = conn.recv(1024)
        return(conn, adrr, request)


def respond(conn, response):
    print("response initiated")
    response = "HTTP/1.0 200 OK" + response
    print(response.encode())
    conn.send(response.encode())
    print(conn.send(response.encode()), "sent")
    #conn.close()?