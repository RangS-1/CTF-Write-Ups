from pwn import *

HOST = 'IP' # CHANGE IT WITH YOUR IP
PORT = PORT # CHANGE IT WITH YOUR PORT

RULES = {
    'GORGE': 'STOP',
    'PHREAK': 'DROP',
    'FIRE': 'ROLL'
}

def solve():
    io = remote(HOST, PORT)

    io.sendlineafter(b'(y/n)', b'y')

    while True:
        try:
            line = io.recvline().decode(errors="ignore").strip()
            print("[SERVER]", line)

            # Detect Flag
            if '}' in line:
                print(f"\n[+] Flag Found: {line}")
                break

            # Server gave scenarios, split by comma. example: FIRE,GORGE -> ROLL-STOP 
            scenarios = [s.strip() for s in line.split(',')]

            if not all(s in RULES for s in scenarios):
                continue  # skip LINE IF NOT SCENARIOS

            # Wait for the server to ask for the answer
            io.recvuntil(b'do you do?')

            responses = [RULES[s] for s in scenarios]
            answer = "-".join(responses)

            print(f"[*] {line} -> {answer}")

            io.sendline(answer.encode())

        except EOFError:
            print("\n[!] Connection closed")
            break

    io.close()

if __name__ == "__main__":
    solve()