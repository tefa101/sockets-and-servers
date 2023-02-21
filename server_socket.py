import socket

ip = '192.168.1.12'
port = 5678

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s :
        s.bind((ip , port))
        s.listen(1)
        print('waiting for connections .. .')
        conn , addr = s.accept()
        print('got connection from {}'.format(addr) )
        with conn:
            while True:
                conn.send(b"killmeeeeee")
                break
            