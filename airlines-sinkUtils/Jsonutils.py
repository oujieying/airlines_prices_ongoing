import json
class MyClass(object):
    def __init__(self):
        self.a = 2
        self.b = 'bb'
if __name__ == '__main__':
    # 创建MyClass对象
    myClass = MyClass()
    # 添加数据c
    myClass.c = 123
    myClass.a = 3
    # 对象转化为字典
    myClassDict = myClass.__dict__
    # 打印字典
    print(myClassDict)
    # 字典转化为json
    myClassJson = json.dumps(myClassDict)
    # 打印json数据
    print(myClassJson)
    print("##############json转化为字典############")
    # json转化为字典
    myClassReBuild = json.loads(myClassJson)
    # 打印重建的字典
    print(myClassReBuild)
    # 新建一个新的MyClass对象
    myClass2 = MyClass()
    # 将字典转化为对象
    myClass2.__dict__ = myClassReBuild;
    # 打印重建的对象
    print(myClass2.a)
