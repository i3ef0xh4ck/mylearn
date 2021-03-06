"""
周末作业

"""

"""
33.谈一下对于多线程编程的理解,对于CPU密集型怎样使用多线程说说线程池,线程锁的用法,有没有用过 multiprocessing或 concurrent. future? 

多线程编程是指在同一个进程中“同时”处理多个任务，python中的多线程由于GIL锁的存在，同一时间在一个CPU上只允许有一个线程执行，所有不能
完全发挥多核PU的优势；
通过使用线程池来控制线程的数量，达到最大只允许规定好的数量的线程运行，以避免线程数量的失控；
通过线程锁可以解决多个线程对同一全局数据进行修改时的不统一，保证每一次完整修改只有一个线程参与，同时通过线程锁也可以间接实现不同线程
有序执行；
使用multiprocessing中的Process可以开启多进程进行多任务处理。
"""

"""
34.关于守护线程的说法,正确的是  A
A.所有非守护线程终止,即使存在守护线程,进程运行终止
B。所有守护线程终止,即使存在非守护线程,进程运行终止
C.只要有守护线程或者非守护线程其中之一存在,进程就不会终止
D.只要所有的守护线程和非守护线程中终止运行之后,进程才会终止

非守护线程代码运行完毕，守护线程也就结束,（守护的是非守护线程）主线程也是非守护线程（进程包含了线程）
"""

"""
35.TCP协议在每次建立或者拆除连接时,都要在收发双方之间交换(D)报文
A.一个B.两个 C.三个D.四个
"""

"""
36.描述多进程开发中join与 deamon的区别
多进程中join会阻塞主进程直至相应子进程执行完毕
deamon:守护进程 守护进程会在主进程代码执行结束而结束
"""

"""
37.请简述GL对 Python性能的影响
GIL锁是一个互斥锁，它被添加到解释器上，使得同一时间在一个CPU上只允许有一个线程执行，所有不能完全发挥多核PU的优势；
"""

"""
38.曾经在哪里使用过:线程、进程、协程? 

在网络编程中，通过多线程或多进程实现服务器的并发，通过协程来处理计算与IO操作的切换达到更高效的使用CPU
"""

"""
39.请使用yield实现一个协程?

并发的本质：切换+保存状态
yield本身就是一种在单线程下可以保存任务运行状态的方法
1 yiled可以保存状态，yield的状态保存与操作系统的保存线程状态很像，但是yield是代码级别控制的，更轻量级
2 send可以把一个函数的结果传给另外一个函数（中的yield），以此实现单线程内程序之间的切换
yield不能检测IO，实现遇到IO自动切换

3.078932046890259
3.194923162460327 使用协程
"""
import time


# def consumer():
#     while True:
#         goods = yield
#         print(goods)
#
#
# def prodeucer():
#     c = consumer()
#     next(c)
#     for i in range(1000000):
#         c.send('test%s' % i)
#         # print('test%s' % i)
#
#
# start = time.time()
# prodeucer()
# stop = time.time()
# print(stop - start)

"""
40.请使用 python内置 async语法实现一余协程?
"""

"""
41.简述线程死锁是如何造成的如何通免?

线程死锁是指线程之间相使用多个互斥锁，互竞争资源，己方的执行需要对方先执行完并释放锁，从而造成死锁；
使用一把锁后递归锁避免死锁
"""

