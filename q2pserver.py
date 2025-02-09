import socket
from multiprocessing import Process
import time

def process_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024).decode() # max 1024 bytes can be recieved. Decode these bytes to string
            if not data: # This is to handle the case when the client closes the connection by entering option 4
                break
            print(f"Client {addr} Request: {data}")
            response = data[::-1]
            time.sleep(3)
            conn.sendall(response.encode()) # Encode the string to bytes and send it to the client
        print(f"Connection closed by {addr}")

def start_server(host='127.0.0.1', port=65430):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Avoid "Address already in use" error
        server_socket.bind((host, port))
        server_socket.listen(100)
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            Process(target=process_client, args=(conn, addr)).start()
            conn.close()

if __name__ == "__main__":
    start_server()
