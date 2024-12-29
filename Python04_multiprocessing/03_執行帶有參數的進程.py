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


