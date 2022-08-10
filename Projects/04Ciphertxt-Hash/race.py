##!/usr/bin/python3
# -*- coding: utf-8 -*-
import socket

host = '127.0.0.1'
port = 19999

r=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((host,port))

d=r.recv(2048).decode()
print(d)

r.send(('S\n').encode())
r.send(('e\n').encode())
r.send(('c\n').encode())
r.send(('r\n').encode())
r.send(('e\n').encode())
r.send(('t\n').encode())
