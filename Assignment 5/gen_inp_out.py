import paramiko
import time

hostname = "172.27.26.188"
port = 22
username = "students"
password = "cs641a"

ssh = paramiko.client.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, port, username, password, allow_agent=False, look_for_keys=False)

chan = ssh.invoke_shell()
chan.send("The_Kryptonians\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("kryptology\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("5\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("go\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("wave\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("dive\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("go\n")
time.sleep(1)
chan.recv(5000)
time.sleep(1)
chan.send("read\n")
time.sleep(1)
chan.recv(5000)


convert_to_hex = {'f':'0', 'g':'1', 'h':'2', 'i':'3', 'j':'4', 'k':'5', 'l':'6', 'm':'7', 'n':'8', 'o':'9', 'p':'i', 'q':'b', 'r':'c', 's':'d', 't':'e', 'u':'f'}
convert_to_cipher = {'0':'f', '1':'g', '2':'h', '3':'i', '4':'j', '5':'k', '6':'l', '7':'m', '8':'n', '9':'o', 'i':'p', 'b':'q', 'c':'r', 'd':'s', 'e':'t', 'f':'u'}


def hex_to_cipher(str):
    cipher=''
    for i in str:
        cipher+=convert_to_cipher[i]
    return cipher

def cipher_to_hex(str):
    hex=''
    for i in str:
        hex+=convert_to_hex[i]
    return hex


chan.send("password\n")
time.sleep(1)
chan.recv(5000)    

chan.send("c\n")
time.sleep(1)
chan.recv(5000)
inp_str = []
for i in range(1,128):
    m = hex(i)[2:]
    if len(m)==1:
        m='0'+m
    for b in range(1,9):
        inp = hex_to_cipher(m)
        str = 'ff'*(b-1)+inp+'ff'*(9-b-1)
        inp_str.append(str)
inp = ['f'*16]*8
for i in range(8):
    for j in range(127):
        inp[i]+=' '+inp_str[8*j+i][:16]

file = open("inputs.txt","w")
for i in inp:
    file.write(i)
    file.write("\n")
file.close()
file1 = open('inputs.txt', 'r')
lines = file1.readlines()
out = []
for line in lines:
    inpf=''
    for inp in line.split():
        chan.send(inp+"\n")
        time.sleep(1)
        x = chan.recv(5000)
        x = x[-43:-27]
        inpf += ' '+x.decode("UTF-8")
        chan.send("c\n")
        time.sleep(1)
        chan.recv(5000)
    out.append(inpf[1:])

file = open("outputs.txt","w")
for i in out:
    file.write(i)
    file.write("\n")
file.close()