#-*- coding:utf-8 -*-
# datetime:2019/5/20 0020 14:28
# software: PyCharm
import multiprocessing   # 分布式进程
import multiprocessing.managers     # 分布式进程管理器
import random,time


class QueueManger(multiprocessing.managers.BaseManager):
    pass


if __name__ == "__main__":
    QueueManger.register('get_task')
    QueueManger.register('get_result')
    manger = QueueManger(address=('10.12.31.42', 8000), authkey=int('12345'))
    manger.connect()
    task, result = manger.get_task(),manger.get_result()
    for i in range(1000):
        time.sleep(1)
        try:
            data = task.get()
            print('client get',data)
            result.put('client'+str(data+10))
        except:
            pass



