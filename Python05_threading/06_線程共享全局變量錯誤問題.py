import threading

g_num = 0

# 循環100萬次執行的任務
def task1():
    for i in range(1000000):
        global g_num    # 表示要聲明修改全局變量的內存地址
        # 每循環一次給全局變量+1
        g_num += 1
    # 代碼執行到此，說明數據計算完成
    print(f'task1: {g_num}')

# 循環100萬次執行的任務
def task2():
    for i in range(1000000):
        global g_num    # 表示要聲明修改全局變量的內存地址
        # 每循環一次給全局變量+1
        g_num += 1
    # 代碼執行到此，說明數據計算完成
    print(f'task2: {g_num}')


if __name__ == '__main__':
    # 創建兩個子線程
    first_thread = threading.Thread(target=task1)
    second_thread = threading.Thread(target=task2)
    # 啟動線程執行任務
    first_thread.start()
    # 線程等待，讓第一個線程先執行，然後再讓第二個線程在執行，保證數據不會有問題。
    first_thread.join()
    second_thread.start()

