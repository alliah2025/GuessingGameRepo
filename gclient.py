import socket


host = "localhost" 
port = 7777

s = socket.socket()
s.connect((host, port))

data = s.recv(1024).decode()
print(data)
difficulty = int(input(""))
s.sendall(str(difficulty).encode())

if difficulty == 1:
    low, high = 1, 10
elif difficulty == 2:
    low, high = 1, 50
else:
    low, high = 1, 100

print(s.recv(1024).decode())

while True:
    guess = (low + high) // 2
    print(f"BOT: {guess}")
    s.sendall(str(guess).encode())
    response = s.recv(1024).decode().strip()

    print(f"SERVER: {response}")

    if "CORRECT!" in response:
        break
    elif "Lower" in response:
        high = guess - 1
    elif "Higher" in response:
        low = guess + 1


s.close()