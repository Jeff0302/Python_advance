import socket


def handle_client_request(curr_socket: socket.socket):

    result = curr_socket.recv(4096)
    if result:
        http_request = result.decode('utf-8')
        print(http_request)
        # 獲取請求的頁面
        # 設置最大分割為2，只split到第2的空格
        request_page = http_request.split(' ', maxsplit=2)[1]
        
        # 如果不指定頁面返回主頁面
        if request_page == '/':
            request_page = '/index.html'
        
        print(f'請求頁面{request_page}')

        # ***為了兼容圖片格式以二進制形式打開文件***
        with open('./static' + request_page, 'rb') as file_name:
            content = file_name.read()

        # 返回http response
        response_line = 'HTTP/1.1 200 OK\r\n'

        response_header = 'Server: PWS/1.0\r\n'

        response_body = content

        # 二進制無法和字符串拼接，須將字符串轉成bytes二進制形式
        send_data = (response_line + response_header + '\r\n').encode('utf-8') + response_body

        curr_socket.send(send_data)

    
    curr_socket.close()


if __name__ == '__main__':
    # 設置ip4 + TCP傳輸協議
    http_server_socket = socket.socket(family=socket.AF_INET,  type=socket.SOCK_STREAM)

    # 設置服務器退出端口立即釋放
    http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 綁定服務器端口
    http_server_socket.bind(('', 8888))

    # 設置監聽(排隊等待連接的最大數量)
    http_server_socket.listen(128)
    
    while True:
        # 等待客戶端連接
        new_socket, port= http_server_socket.accept()

        handle_client_request(new_socket)
    