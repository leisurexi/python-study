# author: leisurexi
# date: 2021-01-16 11:46

import socket
import os


def read_file(file_name, i):
    with open(file_name, 'r') as fin:
        with open(f'E:/tmp/client-tmp{i}.txt', 'w') as fout:
            content = fin.readline()
            if not content:
                fout.write(content)


if __name__ == '__main__':
    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_sock.connect(('localhost', 8080))
    file_name = 'E:/tmp/tmp.txt'
    i = 1
    while True:
        msg = client_sock.recv(1024).decode('UTF-8')
        if msg == 'write finished':
            read_file(file_name, i)
            i += 1
            os.remove(file_name)
            client_sock.send('read finished'.encode('UTF-8'))
        elif msg == 'send finished':
            client_sock.close()
            break
