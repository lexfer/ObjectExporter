#!/usr/bin/env python3

from configparser import SafeConfigParser
import socket
import ssl

parser = SafeConfigParser()
parser.read('config.ini')

print(parser.get('server', 'ip'))












