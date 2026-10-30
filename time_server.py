import socket
import threading
from datetime import datetime

def handle_client(conn, addr):
    print(f"Koneksi dari {addr}")
    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            
            request = data.decode('utf-8')
            print(f"Menerima request: {repr(request)}")
            
            if request.startswith("TIME") and request.endswith("\r\n"):
                now = datetime.now()
                waktu = now.strftime("%H:%M:%S")
                response = f"JAM {waktu}\r\n"
                conn.sendall(response.encode('utf-8'))
            elif request == "QUIT\r\n":
                response = "Goodbye!\r\n"
                conn.sendall(response.encode('utf-8'))
                break
            else:
                response = "Invalid request\r\n"
                conn.sendall(response.encode('utf-8'))
    finally:
        conn.close()
        print(f"Koneksi dengan {addr} ditutup")

def start_server():
    host = '0.0.0.0'
    port = 45000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((host, port))
        s.listen()
        print(f"Server waktu berjalan di {host}:{port}")
        
        while True:
            conn, addr = s.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()

if __name__ == "__main__":
    start_server()