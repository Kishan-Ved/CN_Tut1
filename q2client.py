import socket

def start_client(host='127.0.0.1', port=65430):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        user_input = "Hello World, this is a really long string."
        client_socket.sendall(user_input.encode())
        response = client_socket.recv(1024).decode()
        print(f"Server Response: {response}")
        client_socket.close()

if __name__ == "__main__":
    start_client()
