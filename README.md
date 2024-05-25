[TOC]

# Python 進階

---

## 1. 抽象類

### 1-1. 什麼是抽象類(未實現的類)
a. 抽象類是一個<font title="red">不能被實例化的類</font>。

b. 抽象方法是一個沒有具體實現的方法(子類中重寫方法)。	

c. 一個抽象類可以有或沒有抽象發法。

注意: Python沒有直接支持抽象類，但提供一個`模塊(abc)`來允許定義抽向類。



### 1-2. 如何定義抽象類

1. 通過繼承`abc.ABC`來定義一個抽象類
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

### 1-3. 使用抽象類

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

