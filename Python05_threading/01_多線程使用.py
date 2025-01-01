# 導入多線程模塊
import threading
import time, os

def dance():
    for i in range(10):
        print(f'[{threading.current_thread()}] 跳舞中~~~')
        time.sleep(0.2)

def sing():
    for i in range(10):
        print(f'[{threading.current_thread()}] 唱歌中~~~')
        time.sleep(0.2)




if __name__ == '__main__':
    # 創建子線程
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)
    # 啟動子線程
    t1.start()
    t2.start()
    print(f'[{threading.current_thread()}]Main over')