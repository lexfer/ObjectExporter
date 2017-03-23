#!/usr/bin/env python3

from configparser import SafeConfigParser
import socket
import ssl

parser = SafeConfigParser()
parser.read('config.ini')
server_ip = parser.get('server', 'ip')
server_port = int(parser.get('server', 'port'))

certfile = parser.get('ssl','ssl_certfile')
print(certfile)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
'''
ssl_sock = ssl.wrap_socket(sock,
                           ca_certs=certfile,
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect((server_ip, server_port))
'''
context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
context.load_verify_locations(certfile)