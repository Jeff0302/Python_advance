import threading

g_num = 0

 # 創建互斥鎖
mutex = threading.Lock()

# 循環100萬次執行的任務
def task1():
    # 上鎖
    mutex.acquire()
    for i in range(1000000):
        global g_num    # 表示要聲明修改全局變量的內存地址
        # 每循環一次給全局變量+1
        g_num += 1
    # 代碼執行到此，說明數據計算完成
    print(f'task1: {g_num}')
    # 釋放鎖
    mutex.release()
    

# 循環100萬次執行的任務
def task2():
    # 上鎖
    mutex.acquire()
    for i in range(1000000):
        global g_num    # 表示要聲明修改全局變量的內存地址
        # 每循環一次給全局變量+1  
        g_num += 1
    # 代碼執行到此，說明數據計算完成
    print(f'task2: {g_num}')
    # 釋放鎖
    mutex.release()
    

if __name__ == '__main__':
    # 創建兩個子線程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)

    # 啟動線程執行任務
    first_thread.start()
    second_thread.start()

    # 互斥鎖可以保證同一時刻只有一個線程執行，能夠保證全局變量的數據沒有問題。
    # 線程等待和互斥鎖都是把多任務變成單任務去執行，保證了數據的準確性，但執行性能會下降。

