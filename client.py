import socket
import time

def send_request(request):
    host = 'localhost'
    port = 45000
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode('utf-8'))
        response = s.recv(1024)
        print(f"Response: {repr(response.decode('utf-8'))}")

if __name__ == "__main__":
    # Get current time
    print("Sending TIME request...")
    send_request("TIME\r\n")
    
    time.sleep(1)
    
    # Quit the connection
    print("Sending QUIT request...")
    send_request("QUIT\r\n")