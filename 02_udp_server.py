import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 212
BUFFER_SIZE = 1024

messages = ["Halo Server", "Apa Kabar?"]

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    for message in messages:
        message_bytes = message.encode('utf-8')
        sck.sendto(message_bytes, (SERVER_IP, SERVER_PORT))
        conn, addr = sck.recvfrom(BUFFER_SIZE)
        print('Response from server: %s' % conn.decode('utf-8'))

except socket.error as msg:
    print('Error! %s' % msg)

except Exception as e :
    print('Ops, coding salah! %s' % e)

finally:
    sck.close()
