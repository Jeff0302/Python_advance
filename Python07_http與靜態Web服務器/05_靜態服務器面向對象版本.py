import socket
import threading
import sys

class HttpWebServer:
    def __init__(self, port_num: int):

        self._port_num = port_num

        # 設置ip4 + TCP傳輸協議
        self._http_server_socket = socket.socket(family=socket.AF_INET, type= socket.SOCK_STREAM)
        
        # 當服務器程序退出，端口立即釋放
        self._http_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 綁定端口號
        self._http_server_socket.bind(('', self._port_num))

        # 設置監聽(排隊等待連接的最大數量)
        self._http_server_socket.listen(128)

    def start(self):
        while True:
            # 等待客戶端連接
            new_socket, port = self._http_server_socket.accept()
            # 為每個用戶創建線程處理處理請求
            task = threading.Thread(target=self.handle_client_request, args=(new_socket,))
            
            # 設置守護主線程，當主線程退出，子線程立即釋放
            task.daemon = True

            task.start()
    
    @staticmethod
    def handle_client_request(curr_socket: socket.socket):
        result = curr_socket.recv(4096)

        if result:
            client_request = result.decode('utf-8')
            client_request_line = client_request.split(' ', maxsplit=2)[1]

            # 不指定頁面時，返回主頁面
            if client_request_line == '/':
                client_request_line = '/index.html'

            try:
                with open('./static'+client_request_line,'rb') as file_name:
                    content = file_name.read()
            except Exception as e:
                with open('./static/error.html','rb') as file_name:
                    content = file_name.read()

                # 響應行
                reponse_line = 'HTTP/1.1 404 Not Found\r\n'
                # 響應頭
                reponse_header = 'Server: PWS/1.0\r\n'

            else:
                reponse_line = 'HTTP/1.1 200 OK\r\n'
                reponse_header = 'Server: PWS/1.0\r\n'
            finally:
                # 響應體
                reponse_body = content
                reponse = (reponse_line + reponse_header + '\r\n').encode('utf-8') + reponse_body
                curr_socket.send(reponse)
        
        curr_socket.close()


if __name__ == '__main__':
    
    
    server = HttpWebServer(int(sys.argv[1]) if len(sys.argv) >= 2 else 8888)

    server.start()