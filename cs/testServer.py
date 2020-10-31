import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_IP = socket.gethostname()
UDP_PORT = 1234
UDP_ADDR = (UDP_IP, UDP_PORT)
s.bind(UDP_ADDR)
ack = ''
c = 0
count = 0
while 1:
    pkt, addr = s.recvfrom(1024)
    ack = pkt.decode()[0]
    #print(pkt)
    s.sendto(ack.encode(), addr)
