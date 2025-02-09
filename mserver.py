import socket
import threading

def process_request(request):
    req = request.split(' ', 1)
    if len(req) < 2:
        return "Invalid request"
    option, data = req
    
    if option == '1':
        return data.swapcase()
    elif option == '2':
        try:
            return str(eval(data))
        except Exception as e:
            return f"Error: {e}"
    elif option == '3':
        return data[::-1]
    else:
        return "Invalid option, Please enter a valid option (1-4)"

def process_client(conn, addr):
    print(f"Connected by {addr}")
    with conn:
        while True:
            data = conn.recv(1024).decode()
            if not data:  # Client disconnected
                break
            print(f"Client Request from {addr}: {data}")
            response = process_request(data)
            conn.sendall(response.encode())
    print(f"Connection closed by {addr}")

def start_server(host='127.0.0.1', port=65430):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Avoid "Address already in use" error
        server_socket.bind((host, port))
        server_socket.listen(100)
        print(f"Server listening on {host}:{port}")

        while True:
            conn, addr = server_socket.accept()
            thread = threading.Thread(target=process_client, args=(conn, addr), daemon=True) # daemon=True will ensure that the thread ends when the main program is stopped (by Ctrl+C)
            thread.start()  # Start a new thread for each client

if __name__ == "__main__":
    start_server()
