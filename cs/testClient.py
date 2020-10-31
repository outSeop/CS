import socket
import threading
import time


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

UDP_IP = socket.gethostname()
UDP_PORT = 1234
UDP_ADDR = (UDP_IP, UDP_PORT)

seq = 0
count = 0
recv = 0
losses = 0
ccount = 0
max_rtt = 0.01
received_ack = ''
rcv_ack = 0
recv_button = 0
timer_button = 0
threading_time = 0

def receive_ack():
    global received_ack, recv_button, isChanged
    while 1:
        if recv_button == 1:
            break
    while 1:
        rcv_ack, addr = s.recvfrom(1024)
        received_ack = rcv_ack.decode()


recv_thread = threading.Thread(target=receive_ack)
recv_thread.start()
print("========start========")
total_start = time.perf_counter()
while count < 1000:
    ccount += 1
    # print("===========" + str(count) + "===========")
    pkt = str(seq) + str(count)
    #  print('seq number: ' + str(seq))
    #  print('Packet Data: ' + str(count))
    # transmission delay
    start_send = time.perf_counter()
    s.sendto(pkt.encode(), UDP_ADDR)
    recv_button = 1
    # transmission_delay = time.time() - start_send

    """
    if isChanged == 1:
    """
    temp = 0
    goto_flag = 1
    while goto_flag:

        temp = time.perf_counter() - start_send
        if temp < max_rtt:
            if received_ack == str(seq):
                break
        else:
            print('TIMEOUT: Send Again')
            #print(received_ack)
            print(pkt)
            losses += 1
            goto_flag = 0
            break
    if goto_flag != 1:
        continue


    # print("rcv ack: " + received_ack)
    count += 1
    seq = 1 - seq
# test
print("========result========")
print("loss: " + str(losses))
print('total send: ' + str(ccount))
print(time.perf_counter() - total_start)
recv_thread.join()
