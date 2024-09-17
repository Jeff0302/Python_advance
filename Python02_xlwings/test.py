import xlwings as xw

# excel使用Python的方式
# 1. 安裝xlwings插件
#    1-1. pip install xlwings
#    1-2. xlwings addin intsall

# 2. 創建一個工程資料夾，下面須包含.xlsm及.py文件且文件需同名
#    xlwings excel 插件會跑同目錄下的同名.py文件

# 3. 導入xlwings模塊
#    主要目的是通過xlwings模塊操作excel
#    3-1. xw.Book('文件名.xlsm').set_mock_caller()

# 4. @xw.func裝飾器將函數導入excel


def main():
    wb = xw.Book.caller()
    sht = wb.sheets[0]
    input = sht.range('A2:E2').value
    print(input)


@xw.func
def fun(data: list):
    a, b, c, d, e = data
    return a*10**4 + b*10**3 + c*10**2 + d*10**1 + e*10**0


def add(a: int, b: int):
    wb = xw.Book.caller()
    sht = wb.sheets[0]
    sht['I2'].value = a+b



if __name__ == '__main__':
    xw.Book('test.xlsm').set_mock_caller()
    main()
