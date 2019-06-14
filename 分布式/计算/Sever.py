#-*- coding:utf-8 -*-
# datetime:2019/5/20 0020 14:28
# software: PyCharm
import multiprocessing   # 分布式进程
import multiprocessing.managers     # 分布式进程管理器
import random,time
from queue import Queue


task_queue = Queue()
result_queue = Queue()


def return_task():
    return task_queue


def return_result():

    return result_queue


class QueueManger(multiprocessing.managers.BaseManager):  # 继承，进程管理共享数据
    pass


if __name__ == "__main__":
    multiprocessing.freeze_support()   # 开启分布式支持
    QueueManger.register('get_task',callable=return_task)  # 注册函数
    QueueManger.register('get_result',callable=return_result)
    manger = QueueManger(address=('10.12.31.42', 8008), authkey=int('123456'))  # 创建一个服务器
    manger.start()
    task, result = manger.get_task(), manger.get_result()
    for i in range(10000):
        print('task add data', i)
        task.put(i)
    print('waitting for------------')
    for i in range(10000):
        res = result.get(timeout=100)
        print('get data', res)

    manger.shutdown()


