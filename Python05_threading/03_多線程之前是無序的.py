# 導入多線程模塊
import threading
import time, os

def task(number: int):
    time.sleep(0.5)
    print(f'任務{number}執行了\n')
    

if __name__ == '__main__':
    # 循環創建大量線程，測試線程之間是否無序
    for i in range(20):
        sub_thread = threading.Thread(target=task, args=(i,))
        # 啟動只線程對應的任務
        sub_thread.start()

    # 進程之間執行是無序的，具體哪個線程先執行由cpu調度決定的

