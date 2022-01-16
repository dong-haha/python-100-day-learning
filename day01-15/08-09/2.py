'''
Python是一门动态语言。
通常，动态语言允许我们在程序运行时给对象绑定新的属性或方法，
当然也可以对已经绑定的属性和方法进行解绑定。但是如果我们需要限定自定义类型的对象只能绑定某些属性，
可以通过在类中定义__slots__变量来进行限定。需要注意的是__slots__的限定只对当前类的对象生效，
对子类并不起任何作用。
'''

class Test():
    def __init__(self,age):
        self.__age = age
    def test(self):
        print("hello,test! age = %d" % self.__age)
def main():
    a = Test(41)
    a.test()
    a.__add_age = 2
    print(a.__add_age)
    # print(a.__age)

if __name__ == '__main__':
    main()
