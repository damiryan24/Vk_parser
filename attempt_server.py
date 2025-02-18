import socket
import vk_parser

host = input('Host: ')
port = int(input('Port: '))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

user, addr = server.accept()

while True:
    data = user.recv(1024)
    request = str(data.decode('WINDOWS-1251'))
    if request == 'end':
        break
    elif request == 'continue':
        data = user.recv(1024)
        domain = str(data.decode('WINDOWS-1251'))
        print(domain)
        data = user.recv(1024)
        count = str(data.decode('WINDOWS-1251'))
        print(count)
        data = user.recv(1024)
        offset = str(data.decode('WINDOWS-1251'))
        print(offset)
        filename = vk_parser.parser(domain, count, offset)
        with open(filename, 'rb') as output:
            while True:
                bytes_read = output.read(1024)
                if not bytes_read:
                    #user.sendall(str.encode('конец файла', 'WINDOWS-1251'))
                    print('end of file')
                    break
                user.sendall(bytes_read)
                bytes_read = None
            print('file sent')
    else:
        break
