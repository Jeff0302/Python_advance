[TOC]

#  抽象類

## 1-1. 什麼是抽象類(未實現的類)

a. 抽象類是一個<font title="red">不能被實例化的類</font>。

b. 抽象方法是一個沒有具體實現的方法(子類中重寫方法)。	

c. 一個抽象類可以有或沒有抽象方法。

注意: Python沒有直接支持抽象類，但提供一個`模塊(abc)`來允許定義抽向類。

## 1-2. 如何定義抽象類

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

## 1-3. 使用抽象類

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

 ## 1-1. xlwings第三方庫安裝

```python
# 1. 安裝xlwings插件
#    1-1. pip install xlwings
#    1-2. xlwings addin intsall
```

##  1-2. 創建工程部步驟

### 1-2-1. 創建一個工程資料夾

### 1-2-2. 在資料夾下創建一個`.xlsm`及一個`.py`文件

>注意: 
>
>\- .xlsm及.py文件需同名，因為excel xlwings插件會跑目錄下的同名.py文件
>
>\- VBA開發人員選項 -> 工具 -> 設定引用項目 -> xlwings需勾選 

![image](C:\Users\AIROHA\Jeff\Python\advance\Python_advance\img\xlwings vba引用.png)

## 1-3. Excel中調用Python腳本及函數

### 1-3-1. VBA `RunPython`函數(無返回值)

```vb
PSub add()
    a = Worksheets(1).Range("A2").Value
    b = Worksheets(1).Range("B2").Value
    RunPython "import test;test.add(" & a & "," & b & ")"
    
End Sub

```

### 1-3-2. Python函數使用`xw.fun`裝飾器導入Excel(可以有返回值)

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





