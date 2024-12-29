# 導入進程包
from multiprocessing import Process
import time, os

# 跳舞任務
def dance():
    for i in range(10):
        time.sleep(1)
        print(f'[進程編號{os.getpid()}][父進程編號{os.getppid()}] 跳舞中~~~')

# 唱歌任務
def sing():
    for i in range(10):
        time.sleep(1)
        print(f'[進程編號{os.getpid()}][父進程編號{os.getppid()}] 唱歌中~~~')

if __name__ == '__main__':
    print(f'[主進程編號{os.getpid()}]')
    # 創建子進程
    """
        group: 指定的進程組，目前只能使用None，一般不需要設置。
        target: 指定的任務目標。
        name: 進程名字。默認為Process-N, N為從1開始遞增的整數。
    """
    p1 = Process(target=dance)
    p2 = Process(target=sing, name="sing")
    print(f'{p1}')
    print(f'{p2}')
    # 啟動進程執行對應任務
    # 進程執行是無序的，具體哪個進程先執行是由操作系統決定的。
    p1.start()
    p2.start()




