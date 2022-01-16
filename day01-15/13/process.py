from multiprocessing import Process
import time


def test(name):
    print("%s is running " % name)
    time.sleep(2)
    print('%s is done' % name)


if __name__ == '__main__':
    # 在windows系统之上，开启子进程的操作一定要放在这下面
    # Process(target=test,kwargs={'name':'monicx'})
    p = Process(target=test, args=('monicx',))
    p.start()  # 向操作系统发送一个请求，操作系统会申请内存空间给，然后把父进程的数据拷贝给子进程，作为子进程的初始数据。
    print('=======主')
    time.sleep(3)
    print("wait")
