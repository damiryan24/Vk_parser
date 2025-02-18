import socket

host = input("Host: ")
port = int(input("Port: "))

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.settimeout(5)

while True:
    print('new cycle ("continue" to begin, "end" to stop)')
    command = input()
    if command == "continue":      #continue
        client.sendall(str.encode(command, 'WINDOWS-1251'))
        command = input('domain:')                                               #domain
        filename = str(command + '.xlsx')
        client.sendall(str.encode(command, 'WINDOWS-1251'))
        command = input('count:')                                               #count
        client.sendall(str.encode(command, 'WINDOWS-1251'))
        command = input('offset:')                                               #offset
        client.sendall(str.encode(command, 'WINDOWS-1251'))
        with open(filename, 'wb') as f:
            while True:
                try:
                    bytes_read = client.recv(1024)
                    f.write(bytes_read)
                    bytes_read = None
                except:
                    break
                    '''try:
                        if bytes_read.decode('WINDOWS-1251') == 'конец файла':
                            print('end')
                            break
                    except:
                        pass'''
        print('file received')
    else:
        break
