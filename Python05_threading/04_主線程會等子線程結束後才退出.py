# 導入多線程模塊
import threading
import time, os

def task():
    while True:
        print(f'任務執行中~~~')
        time.sleep(0.3)
    

if __name__ == '__main__':
    # 創建子線程
    sub_thread = threading.Thread(target=task)
    # 啟動子線程對應的任務
    sub_thread.daemon = True
    sub_thread.start()

    time.sleep(1)
    print('主線程結束')

    # 結論: 主線程會等待子線程結束後才退出。
    # 解決辦法: 將子線程設置為守護主線程。
