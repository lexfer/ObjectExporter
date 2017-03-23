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
        ssl_sock = ssl.wrap_socket(s, ca_certs=ssl_certfile,
                             cert_reqs=ssl.CERT_REQUIRED)
        print("Wrapped client socket for ssl")
    except OSError:
        print("SSL wrapping failed for client")
        err = 1

if not err:
    try:
        ssl_sock.connect((host,port))
        print("Client socket connected")
    except OSError:
        print("Socket connection error for client")
        err = 1
if not err:
    print("Send message...")
    ssl_sock.sendall("Hello SSL!!!!")

s.close()
ssl_sock.close()
print("exit client")
