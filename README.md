# Tugas 1 Network Programming

Koneksi UDP Client - Server

# Soal

In a UDP connection, client wants to send 2 messages to the server seperately. How would server combine the two messages to be sent back to the client?

# Jawaban

To meet the requirement, the server needs to be able to receive and combine two messages sent by the client separately. One way to achieve this is to add a loop in the server script that will wait for and receive two messages before combining them and sending them back to the client. To run both scripts, open two command prompt windows or terminals.

At the same time, to send two messages separately, 02_udp_client.py can be modified to send each message separately using sendto method.