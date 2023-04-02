import socket

LOCAL_IP = '127.0.0.1'
LOCAL_PORT = 212
BUFFER_SIZE = 1024

PESAN_SERVER = "Selamat Datang Client"
PESAN_DALAM_BYTE = str.encode(PESAN_SERVER)

sck = socket.socket(socket.AF_INET, # Address Family InterNET
                    socket.SOCK_DGRAM) # UDP

try:
    sck.bind((LOCAL_IP, LOCAL_PORT))
    print('Bind ke IP %s dengan port %s' % (LOCAL_IP, LOCAL_PORT)) 
    while 1:
        conn, addr = sck.recvfrom(BUFFER_SIZE)
        print('Ada pesan dari IP %s' % addr[0])
        print('Isi pesan: %s' % str(conn,'utf-8'))
        print('-----------------------------')
        sck.sendto(PESAN_DALAM_BYTE, addr)

    conn.close()
except socket.error as msg:
    print('Error! %s' % msg)

except Exception as e :
    print('Ops, coding salah! %s' % e)
