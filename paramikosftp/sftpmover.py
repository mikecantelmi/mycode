import paramiko
import os

host_IP = input("Please enter host IP to copy files to ")
U_name = input("Username? ")
P_word = input("Password? ")

t = paramiko.Transport(host_IP, 22)

t.connect(username=U_name, password=P_word)

sftp = paramiko.SFTPClient.from_transport(t)

for x in os.listdir("/home/student/filestocopy/"):
    if not os.path.isdir("/home/student/filestocopy/"+x):
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x)

sftp.close()

