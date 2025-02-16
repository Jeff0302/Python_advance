# 導入socket模塊
import socket

if __name__ == '__main__':
    #1. 創建客戶端套接字
    '''
    參數
        family = socket.AF_INET, 表示IP4地址
        type = socket.SOCK_STREAM, 表示TCP協議 (socket.SOCK_DGRAM為UDP協議)
    '''
    tcp_client_socket  = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    #2. 和服務端套接字連接
    '''
    connect(address)
    參數
        address為元組 (str, port_num)
        其中str為ip地址, port_num為端口號
    '''
    tcp_client_socket.connect(('127.0.0.1', 2345))

    #3. 發送數據
    '''
    send(data: bytes) 
    參數
        data為發送數據
    '''

    send_content = '我是客戶端Jeff'.encode('utf-8')
    tcp_client_socket.send(send_content)

    #4. 接收數據
    '''
    recv(bufsize) 
    參數
        bufsize為每次接收最大字節數
    '''
    received_data = tcp_client_socket.recv(1024)
    print(received_data.decode('utf-8'))

    #5. 關閉連接
    tcp_client_socket.close()




