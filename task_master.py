# -*- coding: utf-8 -*-
# 分布式进程：发布任务的进程

import random
import time
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

task_queue = queue.Queue()  # 发送任务的队列
result_queue = queue.Queue()  # 接收结果的队列


class QueueManager(BaseManager):
    pass


def getTask():
    return task_queue


def getResult():
    return result_queue


def do_task_master():
    # 把两个Queue都注册到网络上，callable参数是关联了Queue对象
    # windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    QueueManager.register('get_task_queue', callable=getTask)
    QueueManager.register('get_result_queue', callable=getResult)
    # 绑定端口5000，设置验证码'abc',windows下需要填写ip地址，linux下不填默认为本地
    manager = QueueManager(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.start()  # 启动Queue
    try:
        # 获得通过网络访问的Queue对象
        task = manager.get_task_queue()
        result = manager.get_result_queue()
        # 放几个任务进去
        for i in range(10):
            n = random.randint(0, 10000)
            print('Put task %d...' % n)
            task.put(n)
        # 从result队列读取结果
        print('Try get results...')
        for i in range(10):
            r = result.get(timeout=10)
            print('Result: %s' % r)
    finally:
        # 关闭
        manager.shutdown()  # 一定要关闭，否则会报管道未关闭的错误
        print('master exit.')


if __name__ == '__main__':
    freeze_support()  # windows下多进程可能会炸，添加这句可以缓解
    do_task_master()
