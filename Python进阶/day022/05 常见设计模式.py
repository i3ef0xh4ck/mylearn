# 设计模式（编程模板）
# 最佳可重用解决方案

# 单例模式
# 一个类只有一个对象
class Singletion(object):
    isin = None
    def __new__(cls, *args, **kwargs): #cls 代表当前类
        if cls.isin == None:
            cls.isin = super().__new__(cls)#获取了基于当前类的内存地址
        return cls.isin  #返回值必须是一个类的实例化
# xiaoming = Singletion() #自动调用new方法创建内存空间，然后再调用init方法
# xiaoli = Singletion()
# print(id(xiaoming),id(xiaoli))
# print(Singletion.__dict__)
# class Mother(Singletion):
#     def __init__(self, msg = ""):
#         self.msg = msg
#     def get_food(self, new_food):
#         self.msg += new_food
#     def food(self):
#         print('做菜: ', self.msg)
# mother1 = Mother()
# mother2 = Mother()
# mother1.get_food('西红柿')
# mother2.get_food('鸡蛋')
# print('儿子的妈妈id：', id(mother1))
# mother1.food()
# print('女儿的妈妈id：', id(mother2))
# mother2.food()





# 工厂模式
# 通过管理者
# 创建基类-创建子类-创建工厂类-使用
class Girl1:
    def xiyinli(self):
        print("我腿长")

class Girl2:
    def xiyinli(self):
        print("我美")

class Girl3:
    def xiyinli(self):
        print("我有钱")

class Girl4:
    def xiyinli(self):
        print("不存在")

class Factory:
    def get_girl(self,choice):
        if choice == "腿长":
            return Girl1()
        if choice == "美":
            return Girl2()
        if choice == "有钱":
            return Girl3()
        return Girl4()


f1 = Factory()
my_girl = f1.get_girl("脱发")
my_girl.xiyinli()