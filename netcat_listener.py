import socket
import subprocess
import sys

def start_listener(ip='0.0.0.0', port=4444):
    print(f"[+] Listening on {ip}:{port}...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)
    print("[+] Waiting for connection...")
    
    conn, addr = server.accept()
    print(f"[+] Connection established from {addr}")
    
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(data.decode())
        
        cmd = input("Enter command (exit to quit): ")
        if cmd.lower() == 'exit':
            break
        conn.send(cmd.encode())
        if not data:
            break
            
    conn.close()
    server.close()

if __name__ == "__main__":
    start_listener()
