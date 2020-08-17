from pwn import *

ip = '129.241.200.165'
port = 3200


conn = remote(ip, port)
conn.send(b'a\n')
print(conn.recvline())
print(conn.recvline())
conn.close()