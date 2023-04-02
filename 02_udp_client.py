import socket

LOCAL_IP = '127.0.0.1'
LOCAL_PORT = 212
BUFFER_SIZE = 1024

PESAN_SERVER = "Selamat Datang Client"
PESAN_DALAM_BYTE = str.encode(PESAN_SERVER)

sck = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    sck.bind((LOCAL_IP, LOCAL_PORT))
    print('Bind ke IP %s dengan port %s' % (LOCAL_IP, LOCAL_PORT))
    messages = []  # initialize an empty list to store the messages
    while len(messages) < 2:  # wait for two messages
        conn, addr = sck.recvfrom(BUFFER_SIZE)
        print('Ada pesan dari IP %s' % addr[0])
        message = str(conn, 'utf-8')
        messages.append(message)
        print('Isi pesan: %s' % message)
        print('-----------------------------')
    combined_message = '\n'.join(messages)  # combine the messages with a new line separator
    sck.sendto(str.encode(combined_message), addr)
    print('Pesan berhasil dikirim kembali ke %s' % addr[0])
    print('Isi pesan: %s' % combined_message)
    print('-----------------------------')
    conn.close()

except socket.error as msg:
    print('Error! %s' % msg)

except Exception as e:
    print('Ops, coding salah! %s' % e)

finally:
    sck.close()