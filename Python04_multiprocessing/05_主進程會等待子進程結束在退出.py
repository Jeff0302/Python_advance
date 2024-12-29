import multiprocessing as m
import os, time

def task():
    for i in range(10):
        print(f'[{m.current_process()}] 任務執行中~~~')
        time.sleep(0.5)


if __name__ == '__main__':
    # 創建子進程
    p1 = m.Process(target=task)
    # p1.daemon = True
    p1.start()

    # 主進程延時0.5s
    time.sleep(2)
    p1.terminate()
    print('Main over')
    # 結論: 主進程會等子進程執行完成以後再退出
    # 解決辦法: 主進程退出子進程銷毀
    #       1. 讓子進程設置為守護主進程。主進程退出子進程銷毀，子進程會依賴主進程。
    #       2. 讓主進程退出前先終止(銷毀)子進程。