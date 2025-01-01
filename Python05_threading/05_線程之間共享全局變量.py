# 導入多線程模塊
import threading
import time, os

# 定義全局變量
g_list = []

def add_data(number: int):
    time.sleep(3)
    g_list.append(number)


def read_data():
    time.sleep(2)
    print(g_list)

if __name__ == '__main__':
    # 創建子線程
    sub_thread1 = threading.Thread(target=add_data, args=(1,))
    sub_thread2 = threading.Thread(target=read_data,)
    
    sub_thread1.start()
    # 當前線程等待sub_thread1線程結束才繼續執行
    sub_thread1.join()
    sub_thread2.start()

    print('主線程結束')

    # 結論: 線程之間共享全局變量