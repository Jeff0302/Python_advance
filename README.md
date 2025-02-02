[TOC]

#  抽象類

## 1. 什麼是抽象類(未實現的類)

a. 抽象類是一個<font title="red">不能被實例化的類</font>。

b. 抽象方法是一個沒有具體實現的方法(子類中重寫方法)。	

c. 一個抽象類可以有或沒有抽象方法。

注意: Python沒有直接支持抽象類，但提供一個`模塊(abc)`來允許定義抽向類。

## 2. 如何定義抽象類

1. 通過繼承`ABC`來定義一個抽象類
```python
# 1.引入abc模塊來定義抽象類
from abc import ABC, abstractmethod


# 2.繼承ABC來定義抽象類
class Action(ABC):
    # 3. 定義抽象方法(等同c++純虛函數)(未實現方法)
    @abstractmethod
    def execute(self):
        pass

```



2. 定義抽象方法使用`@abstractmethod`裝飾器

```python
# 2.繼承ABC來定義抽象類
class Action(ABC):
    # 3. 定義抽象方法(等同c++純虛函數)(未實現方法)
    @abstractmethod
    def execute(self):
        pass

```

## 3. 使用抽象類

​	子類繼承抽象類，重寫抽象方法

```python
# 繼承抽象類，重寫抽象方法(純虛函數)
class CreateStudentAction(Action):
    # 如果沒有重寫抽象方法，依然是一個抽象類，則無法實例化
    def execute(self):
        print("CreateStudentAction執行了")

```



範例: <span alt="solid">Python01_抽象類的使用</span>



---

# xlwings

 ## 1. xlwings第三方庫安裝

```python
# 1. 安裝xlwings插件
#    1-1. pip install xlwings
#    1-2. xlwings addin intsall
```

##  2. 創建工程部步驟

### 2-1. 創建一個工程資料夾

### 2-2. 在資料夾下創建一個`.xlsm`及一個`.py`文件

>注意: 
>
>\- .xlsm及.py文件需同名，因為excel xlwings插件會跑目錄下的同名.py文件
>
>\- VBA開發人員選項 -> 工具 -> 設定引用項目 -> xlwings需勾選 

![image](.\img\xlwings vba引用.png)

## 3. Excel中調用Python腳本及函數

### 3-1. VBA `RunPython`函數(無返回值)

```vb
Sub add()
    a = Worksheets(1).Range("A2").Value
    b = Worksheets(1).Range("B2").Value
    RunPython "import test;test.add(" & a & "," & b & ")"

End Sub

```

### 3-2. Python函數使用`xw.fun`裝飾器導入Excel(可以有返回值)

```python
import xlwings as xw

def main():
    wb = xw.Book.caller()
    sht = wb.sheets[0]
    input = sht.range('A2:E2').value
    print(input)


def add(a: int, b: int):
	wb = xw.Book.caller()
	sht = wb.sheets[0]
	sht['I2'].value = a+b

@xw.func
def fun(data: list):
    a, b, c, d, e = data
    return a*10**4 + b*10**3 + c*10**2 + d*10**1 + e*10**0


if __name__ == '__main__':
    xw.Book('test.xlsm').set_mock_caller()
    main()

```



<font title ="red">注意: 要導入函數需要點擊xlwings插件的import functions</font>



參考資料: https://docs.xlwings.org/zh-tw/latest/udfs.html

​		  https://www.kancloud.cn/gnefnuy/xlwings-docs/1127461



範例: <span alt="solid"> Python02_xlwings使用</span>



---



# Logging日誌

## 1. 紀錄程序日誌信息的目的

	### 1-1-1. 可以方便的了解程序運行的情形。

### 1-2. 分析用戶的操作行為、喜好等信息。

### 1-3. 方便開發人員檢查bug



## 2. logging日誌及級別介紹

### 2-1. `DEBUG`: 程序調試bug時使用

### 2-2. `INFO`: 程序正常運行時使用

### 2-3. `WARNING`: 程序未按預期運行時使用，但不是錯誤，如:密碼錯誤

### 2-4. `ERROR`: 程序出現錯誤時使用，如: IO操作失敗

### 2-5. `CRITIACL`: 特別嚴重的問題，導致程序不能再繼續運行時使用，如:磁盤空間為空，一般很少使用

+ 日誌等級由高到低: DEBUG < INFO < WARNING < ERROR < CRITICAL



## 3. 日誌信息輸出控制台範例

```python
import logging

if __name__ == '__main__':

    logging.debug('這是一個debug級別的日誌')
    logging.info('這是一個info級別的日誌')
    logging.warning('這是一個warning級別的日誌')
    logging.error('這是一個error級別的日誌')
    logging.critical('這是一個critical級別的日誌')

```



![image-20241212235823010](C:\Users\jianf\AppData\Roaming\Typora\typora-user-images\image-20241212235823010.png)



### 3-1. 日誌信息只顯示大於等於WARNING級別的日誌，說明<font title=red>默認的日誌級別設置為WARNING</font>

## 4. `logging.basicConfig()`設置日誌輸出等級，格式，目標位置

### 4-1. `level` 設置日誌輸出等級

### 4-2. `format` 設置日誌輸出格式`%(asctime)s`, `%(filename)s`, `%(lineno)d`, `%(levelname)s`, `%(message)s`

### 4-3. `filename` 設置日誌輸出文件名

### 4-4. `filemode` 設置日誌輸出方式`w`重寫, `a`追加



```python
# logging用記錄程序運行時的日誌信息
import logging

if __name__ == '__main__':

    # 設置logging日誌的配置信息
    # level  表示設置級別
    # format 表示輸出格式
    #   %(asctime)s     表示當前時間
    #   %(filename)s    表示程序文件名
    #   %(lineno)d      表示所在行數
    #   %(levelname)s   表示日誌等級
    #   %(message)s     表示輸出信息
    # filename 表示日誌輸出位置
    # filemode 表示日誌輸出方式
    #   'w' 複寫,原有data會消失
    #   'a' 追加,原有data會保留
    
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s-%(filename)s[lineno:%(lineno)d-%(levelname)s}-%(message)s]',
                        filename='log.txt',
                        filemode='w')

    logging.debug('這是一個debug級別的日誌')
    logging.info('這是一個info級別的日誌')
    logging.warning('這是一個warning級別的日誌')
    logging.error('這是一個error級別的日誌')
    logging.critical('這是一個critical級別的日誌')
    # 默認是warning，只有大於等於warning級別的日誌才會輸出

```



如果需要將log同時輸出到控制台及文件可以參考以下網站

[參考資料] https://cloud.tencent.com/developer/article/2028465



範例: <span alt="solid"> Python03_logging</span>



---

# 多進程Process

## 1. 導入進程包`multiprocessing`

## 2. 進程類`Process`說明

### 2-1. `Process(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)`

+ group: 指定的進程組，目前只能使用None。
+ target: 指定的任務目標。
+ name: 進程名字。默認為Process-N, N為從1開始遞增的整數。
+ args:  以元組方式給任務傳參。
+ kwargs:  字典方式給任務傳參。

### 2-2. Process創建實例常用方法`start()`、`join()`、`terminate()`

+ start(): 啟動子進程實例。
+ join(): 等待子進程結束。
+ terminate(): 不管任務是否完成，立即終止子進程。

### 2-3. `multiprocessing.current_process()`: 查看當前代碼由哪個進程執行。



## 3. 獲取進程編號及刪除進程

### 3-1. `os.getpid()`: 獲取當前進程編號。

### 3-2. `os.getppid()`: 獲取父進程編號。

### 3-3. `os.kill(pid, sig)`: 根據進程編號銷毀進程。　　　

## 4. 多進程任務代碼

### 4-1. 多進程使用

```python
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

```



### 4-2. 獲取進程編號

```python
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
```



### 4-3. 執行帶有參數的進程 

```python
import multiprocessing as m
import os, time

def dance(person: str, dance_name:str):
    for i in range(10):
        time.sleep(1)
        print(f'[進程編號{os.getpid()}][{m.current_process()}] {person} 跳{dance_name}中~~~~~~~')
        

def sing(person: str ,sing_name: str):
    for i in range(10):
        time.sleep(1)
        print(f'[進程編號{os.getpid()}][{m.current_process()}] {person} 唱{sing_name}中~~~~~~~')

if __name__ == '__main__':
    # 以元組方式傳參，元組裡面的元素順序要和函數參數的順序保持一致
    p1 = m.Process(target=dance, args=('Jack','街舞'))
    # 以字典方式傳參，字典裡的關鍵字和函數參數名必須保持一致，順序沒有要求
    p2 = m.Process(target=sing, kwargs={'person': 'Amy', 'sing_name': '白色風車'})
    p3 = m.Process(target=sing, args=('Marry',), kwargs={'sing_name': '黑色幽默'})
    # 混合方式傳參
    p1.start()
    p2.start()
    p3.start()

```



### 4-4. 進程間不會共享全局變量

+ 創建子進程會對主進程資源進行拷貝，也就是說子進程是主進程的一個副本，所以進程之間不會共享全局變量，因為操作的是不同進程裡的全局變量，只是不同進程裡的全局變量名字相同而已。

![image-20241229205441046](.\img\進程不共享全局變量.png)

```python
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

```



### 4-5. 主進程會等待所有子進程結束在退出

+ 如果需要主進程執行完後立即終止

  \- 讓子進程設置為守護主進程。主進程退出子進程銷毀，子進程會依賴主進程。

  \- 讓主進程退出前先終止(銷毀)子進程。

  

```python
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
```



範例: <span alt="solid"> Python04_multiprocessing</span>

---

# 多線程Thread

## 1. 線程的概念

>  線程是進程中執行代碼的一個分支。每個執行分支(線程)要想執行代碼需要CPU進行調度，也就是說線程是CPU調度的基本單位，
>
>每個進程至少有一個線程，而這個線程我們通常稱為主線程。



## 2. 線程的作用: 多線程可以完成多任務

![image-20241229220859919](.\img\多線程效果圖.PNG)

## 3. 進程和線程的關係對比

### 3-1. 線程是依附在進程裡的，沒有進程就沒有線程。

### 3-2. 一個進程默認提供一條線程，進程可以創建多個線程。



## 4. 進程和線程的區別對比

### 4-1. 進程之間不共享全局變量。

### 4-2. 線程之間共享全局變量，但需要注意資源競爭的問題，解決辦法:互斥鎖或線程同步。

### 4-3. 創建進程的資源開銷要比創建線程的資源開銷大。

### 4-4. 進程是操作系統資源分配的基本單位，線程是CPU調度的基本單位。

### 4-5. 線程不能獨立執行，必須依存在進程中。

### 4-6. 多進程開發比單進程多線程開發穩定性要強。

## 5. 進程線程優缺點

### 5-1. 進程優缺點: 可以使用多核，資源開銷大

### 5-2. 線程優缺點: 資源開銷小，不能使用多核



## 6. 多線程導入`threading`模塊

## 7.  線程類`Thread`參數說明: 

###  7-1. `Thread(group=None, target=None, name=None, args=(), kwargs={})`

+ group: 線程組，目前只能使用None。
+ target: 指定的任務目標。
+ name: 線程名字。一般不用設置。
+ args:  以元組方式給任務傳參。
+ kwargs:  字典方式給任務傳參。

### 7-2. 啟動線程`start()`



## 8. 多線程任務代碼

### 8-1. 多線程使用

```python
# 導入多線程模塊
import threading
import time, os

def dance():
    for i in range(10):
        print(f'[{threading.current_thread()}] 跳舞中~~~')
        time.sleep(0.2)

def sing():
    for i in range(10):
        print(f'[{threading.current_thread()}] 唱歌中~~~')
        time.sleep(0.2)


if __name__ == '__main__':
    # 創建子線程
    t1 = threading.Thread(target=dance)
    t2 = threading.Thread(target=sing)
    # 啟動子線程
    t1.start()
    t2.start()
    print(f'[{threading.current_thread()}]Main over')
```



### 8-2. 多線程帶有參數任務

```python
# 導入多線程模塊
import threading
import time, os

def dance(name: str, dance_name: str):
    for i in range(10):
        print(f'[{threading.current_thread()}] {name}跳{dance_name}中~~~')
        time.sleep(0.2)

def sing(name: str, song_name: str):
    for i in range(10):
        print(f'[{threading.current_thread()}] {name}唱{song_name}中~~~')
        time.sleep(0.2)


if __name__ == '__main__':
    # 創建子線程
    # 以元組方式傳參，要保證元組裡面元素的順序和函數的參數順序一致。
    t1 = threading.Thread(target=dance, args=('Jeff','街舞'))
    # 以字典方式傳參，要保證字典裡面的key名和函數參數名相同。
    t2 = threading.Thread(target=sing, kwargs={'name':'Amy', 'song_name':'三天三夜'})
    # 啟動子線程
    t1.start()
    t2.start()
    print(f'[{threading.current_thread()}]Main over')
```



### 8-3. 線程的注意點

+ 線程之間執行是無序的。

```python
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
        # 啟動子線程對應的任務
        sub_thread.start()

    # 進程之間執行是無序的，具體哪個線程先執行由cpu調度決定的
```

+ 主線程會等待所以子線程完成後才退出。

```python
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

    # 結論: 主線程會等待子線程結束後才退出
    # 解決辦法: 將子線程設置為守護主線程。

```

+ 線程之間共享全局變量。

```python
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
```

+ 線程之間共享全局變量數據出現錯誤問題。

​	\- 線程同步: 保證同一時刻只能有一個線程去操作全局變量。同步就是協同步調，按預定的先後次序運行。

![image-20250101204921053](.\img\線程間共享全局變量錯誤問題.PNG)

```python
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
```



### 8-4. 互斥鎖的概念: 對共享數據進行鎖定，保證同一時刻只能有一個線程去操作

>  互斥鎖是多個線程一起去搶，搶到鎖的線程先執行，沒有搶到鎖的線程需要等待，等互斥鎖使用完釋放後，其他線程再去搶這個鎖。



+ 互斥鎖使用

  \- 創建鎖 `mutex = threading.Lock()`

  \- 上鎖 `mutex.acquire()`

  \- 釋放鎖 `mutex.release()`

  

```python
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
```



### 8-5. 死鎖的概念: 一直等待對方釋放鎖的情景就是死鎖

```python
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

```



範例: <span alt="solid"> Python05_threading</span>



---

# 網路編程

## 1. IP地址的介紹: 標示網路中設備的一個地址

+ IP地址分為兩類: IPv4和IPv6 (IPv4是目前使用的ip地址)
+ IPv4是由點分十進制組成
+ IPv6是由冒號十六進制組成

![image-20250101204921053](.\img\ip地址.PNG)





## 2. 端口和端口號的介紹

+ 端口:

  端口是傳輸數據的通道。

+ 端口號: 

  操作系統為了統一管理這麼多端口，就對端口進行編號，這就是端口號，端口號其實就是一個數字，好比我們現實生活中的門牌號。`端口號有65536個`。

  進行數據通訊流程: 通過ip地址找到對應設備，通過端口號找到對應端口，然後通過端口把數據傳輸給應用程序。

![image-20250101204921053](.\img\端口和端口號.PNG)

+ 端口號分類

  \- 知名端口號: 眾所周知的端口號，範圍從0到1023。

  >  這些端口號一般固定分配給一些服務，比如21端口分配給FTP(文件傳輸協議)，25端口分配給SMTP(簡單郵件傳輸協議)  服務。

  

  \- 動態端口號: 開發應用程序使用的端口號，範圍從1024到65535。

  >  如果程序員開發沒有設置端口號，操作系統會在動態端口號這個範圍內隨機生成一個給開發的應用程序使用。
  >
  >  當運行一個程序默認會有一個端口號。當程序退出時，所佔用的端口號就會被釋放。



## 3. TCP介紹

+ TCP的英文`Transmission Control Protocol簡稱傳輸控制協議`，它是一種面向連接、可靠、基於字節流的傳輸層通信協議。

### 3-1. TCP通信步驟: 創建連接， 傳輸數據，關閉連接

### 3-2. TCP的特點: 面向連接，可靠傳輸

+ 面向連接: 通信雙方必須先建立好連接才能進行數據傳輸，數據傳輸完成後，雙方必須斷開連接，以釋放系統資源

+ 可靠傳輸: 

  \- TCP採用應答機制

  \- 超時重傳

  \- 錯誤校驗

  \- 流量控制和阻塞管理

## 4. socket的介紹

### 4-1. socket的概念: 進程間通訊的一個工具

>  socket簡稱套接字是進程之間通訊的一個工具，好比現實生活中的插座，所有的家用電器要想工作都是基於插座進行，進程之間要想進行網路通訊需要基於這個socket。



## 5. TCP網路應用程序開發流程介紹

![image-20250101204921053](.\img\網路編程.PNG)

## 6. TCP客戶端程序開發

### 6-1. 導入`socket模塊`

### 6-2. 創建客戶端socket對象`socket.socket(AddressFamily, Type)`

​	\- AddressFamily表示IP2地址類型，分為IPv4和IPv6

​	\- Type表示傳輸協議類型

​	方法說明:

​	`connect(host, port)`表示和服務器端套接建立連接，host表示服務器ip地址，port表示應用程序端口號。

​	`send(data)`表示發送數據，data是二進制數據。

​	`recv(buffersize)`表示接收數據，buffersize是每次接收數據長度。



```python
```







## 7. TCP服務端程序開發

