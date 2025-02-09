import socket

def display_menu():
    print("\nMenu:")
    print("1. Change the case of a string")
    print("2. Evaluate a mathematical expression")
    print("3. Find the reverse of a string")
    print("4. Exit")

def get_user_input():
    choice = input("Enter your choice (1-4): ")
    if choice == '4':
        return "4"
    data = input("Enter data: ")
    return f"{choice} {data}"

def start_client(host='127.0.0.1', port=65430):
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        
        while True:
            display_menu()
            user_input = get_user_input()
            if user_input == "4":
                print("Exiting client...")
                client_socket.close() # This is not needed, read the comment below
                break
            
            client_socket.sendall(user_input.encode())
            response = client_socket.recv(1024).decode()
            print(f"Server Response: {response}")
    # with socket block exits, so client socket is automatically closed

if __name__ == "__main__":
    start_client()
