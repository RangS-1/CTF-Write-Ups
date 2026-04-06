from pwn import *
import re

HOST = 'IP' # Change it with IP you got from HTB
PORT = YOUR_PORT # Change it with PORT you got from HTB

p = remote(HOST, PORT)

flag = ""
i = 0

while True:
    p.recvuntil(b'index:')

    p.sendline(str(i).encode())

    line = p.recvline().decode(errors="ignore")

    match = re.search(r':\s*(.)', line)
    if not match:
        print(f"[!] Failed parse @ index {i}: {line}")
        break

    char = match.group(1)
    flag += char

    print(f"[{i}] {char} -> {flag}")

    if char == "}":
        print("\n[+] DONE:", flag)
        break

    i += 1

p.close()