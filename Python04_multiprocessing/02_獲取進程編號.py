# 導入進程包
import multiprocessing
import time, os

# 跳舞任務
def dance():
    for i in range(10):
        time.sleep(1)
        # multiprocessing.current_process()查看當前代碼由哪個進程執行
        print(f'[進程編號{os.getpid()}][父進程編號{os.getppid()}][{multiprocessing.current_process()}] 跳舞中~~~')
        # os.kill()根據進程編號來銷毀進程
        os.kill(os.getpid(),9)

# 唱歌任務
def sing():
    for i in range(10):
        time.sleep(1)
        print(f'[進程編號{os.getpid()}][父進程編號{os.getppid()}][{multiprocessing.current_process()}] 唱歌中~~~')

if __name__ == '__main__':
    print(f'[主進程編號{os.getpid()}]')
    # 創建子進程
  
    p1 = multiprocessing.Process(target=dance)
    p2 = multiprocessing.Process(target=sing, name="sing")
    print(f'{p1}')
    print(f'{p2}')
    # 啟動進程執行對應任務
    # 進程執行是無序的，具體哪個進程先執行是由操作系統決定的。
    p1.start()
    p2.start()




