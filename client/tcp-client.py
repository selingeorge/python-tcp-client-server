# TCP Client Side

import socket
import psutil
import time

# Port and Hostname
HOST1_PORT_NUMBER = 65000
# HOST1_NAME = '100.50.200.5'
# Other Examples
HOST1_NAME = "DESKTOP-QOU8E8F"
# HOST1_NAME = "coding_test_1_1 - Enter the INET name here"

HOST2_PORT_NUMBER = 64000
# HOST2_NAME = '100.50.200.5'
# Other Examples
HOST2_NAME = "DESKTOP-QOU8E8F"
# HOST2_NAME = "coding_test_1_2 - Enter the INET name here"

while True:

    # Prepare a process list
    process_list = []

    for proc in psutil.process_iter():
        try:
            process_list.append(proc.name() + ':' + str(proc.pid))
            # print(proc.name(), proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass

    # Encode process_list to byte stream
    byte_strem = '\n'.join(process_list).encode()

    # Access Server 1 socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.connect((HOST1_NAME, HOST1_PORT_NUMBER))
            soc.sendall(byte_strem)
    except OSError:
        print('Unable to open socket in Server 1')

    # Access Server 2 socket
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
            soc.connect((HOST2_NAME, HOST2_PORT_NUMBER))
            soc.sendall(byte_strem)
    except OSError:
        print('Unable to open socket in Server 2')

    # Sleep for 5 seconds
    time.sleep(5)
