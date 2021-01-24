# -*- coding: UTF-8 -*-
"""
实际使用中,如果应用程序接管了标准输出,可能会暂时把sys.stdout替换为类似文件的其他对象,然后再切换为原有版本.
contextlib.redirect_stdout上下文管理器就是如此: 只传入类似文件的对象,用于替代sys.stdout
"""


class LookingGlass:

    def __enter__(self):  # 除了self之外,Python调用__enter__方法不传入其他参数
        import sys
        self.originale_write = sys.stdout.write  # 把原来的sys.stdout.write保存到一个实例属性,供调用__exit__方法时复原
        sys.stdout.write = self.reverse_write  # 为sys.stdout.write打猴子补丁,替换成自己编写的方法
        return 'JABBERWOCKY'  # 返回字符串存入as子句后的目标变量

    def reverse_write(self, text):  # 取代sys.stdout.write的方法: 把text参数内容翻转
        self.originale_write(text[::-1])

    # 如果__exit__方法返回None或者True之外的值,with语句块的任何异常都会向上抛出.
    def __exit__(self, exc_type, exc_val, exc_tb):  # 无异常时,传入的参数为None,None,None;如果抛出异常,则是异常数据
        import sys  # 重复导入模块不会消耗很多资源,因为Python会缓存导入的模块
        sys.stdout.write = self.originale_write  # 复原为原来的sys.stdout.write方法
        if exc_type is ZeroDivisionError:  # 如果有异常并为ZeroDivisionError异常则打印一个消息
            print("Please DO NOT divide by zero!")
            return True  # 然后返回True告诉解释器异常已经得到了处理


# 使用with语句块测试上下文管理器
with LookingGlass() as what:
    print("Alice, Kitty and Snowdrop")
    print(what)

print(what)

print("Back to normal")


# 在with语句块之外使用上下文管理器类LookingGlass, 手动调用__enter__和__exit__方法
manager = LookingGlass()
print(manager)

monster = manager.__enter__()
print(monster == "JABBERWOCKY")
print(monster)

print(manager)
manager.__exit__(None, None, None)
print(monster)
