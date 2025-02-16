# 導入socket模塊
import socket

if __name__ == '__main__':
    #1. 創建服務端socket套接字
    # 服務端套接字用ip4+TCP協議傳輸
    tcp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    #2. 將服務器在指定端口開啟(綁定端口)
    '''
        bind(address)
        參數
            address為元組(str: address, int: 端口號)
            *ip地址一般不指定，表示本機任何一個ip地址皆可
    '''
    tcp_server_socket.bind(('', 2000))

    #3. 設置監聽
    '''
        listen(backlog)表示設置監聽，backlog參數表示排隊等待連接的最大個數。
    '''
    tcp_server_socket.listen(128)
    # 4. 等待接受客戶連接請求
    '''
        accept()表示等待接收客戶端連接請求，返回值為一個socket對象用來和客戶端收發數據
        
        注意點: 每次當客戶端和服務器建立連接成功都會返回一個新的套接字
        tcp_server_socket只負責等待接受客戶端的連接請求，收發數據不使用該套接字
    
    '''
    new_client, ip_port = tcp_server_socket.accept()
    print(new_client)
    print(f'客戶端ip={ip_port[0]}, 端口={ip_port[1]}')

    #5. 接收客戶端數據
    received_data = new_client.recv(1024)
    print(received_data.decode('utf-8'))

    #6. 發送數據給客戶端
    send_data = '收到數據了~~'.encode('utf-8')
    new_client.send(send_data)

    # 關閉服務於客戶端的套接字，表示和客戶端終止通信
    new_client.close()

    #7. 關閉服務端socket套接字
    tcp_server_socket.close()


