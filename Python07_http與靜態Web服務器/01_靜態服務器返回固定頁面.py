import socket


def handle_client_request(client_socket: socket.socket): 

    result = client_socket.recv(4096)
    if result:
        http_request = result.decode('utf-8')
        # 打印客戶端請求報文
        print(f'-------HTTP Request-------+\n{http_request}')
            
        # 返回固定頁面
        with open('./static/index.html','r') as file:
                content = file.read()
        
        # 響應行
        response_line =  'HTTP/1.1 200 OK\r\n'
        # 響應頭
        response_header = 'Server: PWS/1.0\r\n'
        # 響應體
        response_body = content
        
        send_data = response_line + response_header + '\r\n' + response_body

        # 打印客戶端響應報文
        print(f'-------HTTP response-------+\n{send_data}')
        
        client_socket.send(send_data.encode('utf-8'))
    
    client_socket.close()  

   




if __name__=='__main__':
    # 使用IP4 + TCP傳輸協議
    tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    # 設置套接字關閉端口立即釋放
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

    # 綁定服務器端口號
    tcp_server_socket.bind(("", 8888))

    # 設置監聽(排隊等待連接的最大數量)
    tcp_server_socket.listen(128)




    while True: 
        # 等待客戶端連接
        new_client_socket, port= tcp_server_socket.accept()

        handle_client_request(new_client_socket)

        