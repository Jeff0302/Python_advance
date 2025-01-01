# 導入多線程模塊
import threading
import time, os

def dance(name: str, dance_name: str):
    for i in range(10):
        print(f'[{threading.current_thread()}] {name}跳{dance_name}中~~~')
        time.sleep(0.2)

def sing(name: str, song_name: str):
    for i in range(10):
        print(f'[{threading.current_thread()}] {name}唱{song_name}中~~~')
        time.sleep(0.2)


if __name__ == '__main__':
    # 創建子線程
    t1 = threading.Thread(target=dance, args=('Jeff','街舞'))
    t2 = threading.Thread(target=sing, kwargs={'name':'Amy', 'song_name':'三天三夜'})
    # 啟動子線程
    t1.start()
    t2.start()
    print(f'[{threading.current_thread()}]Main over')