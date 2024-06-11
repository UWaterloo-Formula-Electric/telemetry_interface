import socket

def main():
    # 设置服务器地址和端口
    server_ip = '208.68.36.87'
    server_port = 2333
    buffer_size = 1024  # 每次接收数据的缓冲区大小

    # 创建一个TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # 连接服务器
        sock.connect((server_ip, server_port))
        print(f'Connected to {server_ip}:{server_port}')

        # 打开一个文件用于写入接收到的数据
        with open('received_data.txt', 'w') as file:
            while True:
                # 从socket接收数据
                data = sock.recv(buffer_size)
                if not data:
                    break  # 连接关闭时退出循环

                # 将接收到的数据写入文件
                file.write(data.decode('utf-8'))

    except Exception as e:
        print(f'An error occurred: {e}')
    
    finally:
        # 关闭socket连接
        sock.close()
        print('Connection closed')

if __name__ == "__main__":
    main()
