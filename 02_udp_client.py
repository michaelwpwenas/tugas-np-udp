import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 212
BUFFER_SIZE = 1024

PESAN_CLIENT = "Hallo Server"
PESAN_DALAM_BYTE = str.encode(PESAN_CLIENT)

sck = socket.socket(socket.AF_INET, # Address Family InterNET
                    socket.SOCK_DGRAM) # UDP

try:
    # cara 1
    #sck.sendto(PESAN_DALAM_BYTE, (SERVER_IP, SERVER_PORT))
    # cara 2
    sck.connect((SERVER_IP,SERVER_PORT))
    sck.send(PESAN_DALAM_BYTE)
    
    conn, addr = sck.recvfrom(BUFFER_SIZE)
    print('Ada pesan dari IP %s' % addr[0])
    print(addr)
    print('Isi pesan: %s' % str(conn,'utf-8'))
    print('-----------------------------')
    
except socket.error as msg:
    print('Error! %s' % msg)

except Exception as e :
    print('Ops, coding salah! %s' % e)

finally:
    sck.close()
    
