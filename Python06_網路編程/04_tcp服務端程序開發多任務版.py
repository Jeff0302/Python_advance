import socket
import threading


def handle_client_request(socket_instance: socket.socket, ip):

     while True:
        result = socket_instance.recv(1024)
        if result:
            received_data = result.decode('utf-8')
            print(f'[{ip}][{threading.current_thread()}] 客戶端請求 {received_data}')

            socket_instance.send(f'回應客戶端請求{received_data}'.encode('utf-8'))

        else:
            print(f'[{ip}][{threading.current_thread()}] 客戶端退出')
            break

     socket_instance.close()




if __name__ == '__main__':
    # 建立IP4+TCP服務端套接字
    tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # 設置socket option, 設置服務端程序退出端口立即釋放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,True)

    # 綁定服務器端口
    tcp_server_socket.bind(('', 8888))

    # 設置監聽(排隊等待連接的最大個數)
    tcp_server_socket.listen(128)

    # accept()函數循環等待客戶端連接
    # tcp_server_socket用來負責等待客戶端的連接需求，收發數據不使用該套接字
    while True:
        new_client_socket, ip_port = tcp_server_socket.accept()

        print(f'{ip_port} 已連接')
        # 創建子線程用來與客戶端收發數據
        t = threading.Thread(target=handle_client_request , args=(new_client_socket, ip_port))
        # 設置守護進程(主線程結束，子線程立即釋放)
        t.daemon = True
        t.start()


    # 關閉服務器，通常服務器不關閉的
    # tcp_server_socket.close()


