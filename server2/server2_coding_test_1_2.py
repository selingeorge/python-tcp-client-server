# Python TCP Server

import socket
from datetime import datetime

PORT_NUMBER = 64000
HOST = socket.gethostname()

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(HOST)

soc.bind((HOST, PORT_NUMBER))
soc.listen(5)

print('Listening in progress...')

while True:
    con, adr = soc.accept()
    print('Connection established from', soc)

    logfile = 'server_log_' + datetime.today().strftime('%Y_%b_%d__%Hh_%Mm_%Ss') + '.txt'
    f = open(logfile, 'w')

    while True:
        data = con.recv(1024)
        # print(data)
        if not data:
            break
            # write data to a file
        f.write(data.decode())
    f.close()
con.close()