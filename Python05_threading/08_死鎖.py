import threading

g_list = [1, 2, 3]

 # 創建互斥鎖
mutex = threading.Lock()


def get_value(index: int):
    mutex.acquire()
    if index>=len(g_list):
        print(f'下標越界index= {index}')
        # 沒有release會造成死鎖
        mutex.release()
        return
    
    print(g_list[index])
    
    mutex.release()
    

if __name__ == '__main__':
    # 創建大量線程，同時執行根據下標取值任務
    for i in range(10):
        sub_thread = threading.Thread(target=get_value, args=(i,))
        sub_thread.start()


