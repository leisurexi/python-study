# author: leisurexi
# date: 2021-01-16 11:46
'''
你应该使用过类似百度网盘、Dropbox 等网盘，但是它们可能空间有限（比如 5GB）。
如果有一天，你计划把家里的 100GB 数据传送到公司，可惜你没带 U 盘，于是你想了一个主意：
每次从家里向 Dropbox 网盘写入不超过 5GB 的数据，而公司电脑一旦侦测到新数据，就立即拷贝到本地，
然后删除网盘上的数据。等家里电脑侦测到本次数据全部传入公司电脑后，再进行下一次写入，
直到所有数据都传输过去。根据这个想法，你计划在家写一个 server.py，在公司写一个 client.py
来实现这个需求。提示：我们假设每个文件都不超过 5GB。你可以通过写入一个控制文件（config.json）来同步状态。
不过，要小心设计状态，这里有可能产生 race condition。你也可以通过直接侦测文件是否产生，或者是否被删除来同步状态，
这是最简单的做法。

'''

import socket


# 读取数据写入文件
def write_file(i):
    with open(f'E:/tmp/{i + 1}.txt', 'r') as fin:
        with open(f'E:/tmp/tmp.txt', 'w') as fout:
            content = fin.readline()
            if not content:
                fout.write(content)


if __name__ == '__main__':
    serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serv_sock.bind(('', 8080))
    serv_sock.listen(5)

    while True:
        client_sock, client_addr = serv_sock.accept()
        for i in range(0, 20):
            write_file(i)
            client_sock.send('write finished'.encode('UTF-8'))
            # 客户端回复了即代表成功，为了简单不做过多判断
            client_sock.recv(1024)
        client_sock.send('send finished'.encode('UTF-8'))
