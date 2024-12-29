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

![image](C:\Users\AIROHA\Jeff\Python\advance\Python_advance\img\xlwings vba引用.png)

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

![image-20241229205441046](C:\Users\jianf\AppData\Roaming\Typora\typora-user-images\image-20241229205441046.png)

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

















