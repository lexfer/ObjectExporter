import socket,ssl

ssl_certfile = 'ssl\ssl_cert'
ssl_keyfile = 'ssl\ssl_key'
host = 'localhost'
port = 15999

err = 0
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket created')
except OSError:
    print('Failed to create socket')
    err = 1

if not err:
    try:
        s.bind((host, port))
        print('Bind worked')
    except OSError:
        print("Bind filed in server")
        err = 1

if not err:
    try:
        s.listen(10)
    except OSError:
        print("Listen failed")
        err = 1

if not err:
    conn, addr = s.accept()
    print("Accepted client connection on address: " + str(addr))
    try:
        global connstream
        connstream = ssl.wrap_socket(conn,
                             server_side=True,
                             certfile=ssl_certfile,
                             keyfile=ssl_keyfile,
                             ssl_version=ssl.PROTOCOL_SSLv23,
                             )
        print("SSL wrap succeeded for sever")
    except OSError:
        print("SSL wrap failed for server")
        err = 1

while True:
    data = connstream.recv(1024)
    if data:
        print("server: " + data)
    else:
        break

s.close()
connstream.close()
print("exit server")
