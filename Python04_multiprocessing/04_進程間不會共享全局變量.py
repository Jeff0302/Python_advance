import multiprocessing as m
import os, time

g_list = []


# 添加數據的任務
def add_data(datas:list):
    global g_list
    g_list.extend(datas)
    print(f'[{m.current_process()}] {g_list}')

def read_data():
    print(f"[{m.current_process()}]g_list_read: {g_list}")


# 提示: 對於linux和mac主進程執行的代碼不會進行拷貝，但對於window系統主進程執行的代碼也會進行拷貝。
# 對於window系統來說創建子進程的代碼，相當於無限遞歸創建子進程，會報錯。

# 如何解決windows遞歸創建子進程: 通過判斷是否是主模塊
if __name__ == '__main__':
    g_list.append(0)
    print(f'Main [{m.current_process()}] {g_list}')

    p1 = m.Process(target=add_data, args=([1,1],))
    p2 = m.Process(target=read_data)

    p1.start()
    # 當前進程等待添加數據進程執行完成以後，在往下執行代碼
    p1.join()
    p2.start()
 
    print(f'Main [{m.current_process()}] {g_list}')

    # 結論: 進程之間不共享全局變量


