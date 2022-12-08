#from module import a,b
#from module import a as newname
#from module import *    不推荐使用
#import module
#mport module as newname    使用时需要加上模块名称  newname.a()


def MyPrint1(ret=0,*b):    #b是一个元组,可以接受任意个参数
    flag = "fine"
    print("ret is :",ret)
    print("tuple in is :",b)

    ret = int(input("Please input: "))
    while (ret != 0):
        print("six!")
        ret-=1

    return flag

def MyPrint2(**c):    #c是一个字典,可以接受任意键值对
    flag = "ok"
    print("dictionary in is :",c)

    return flag


num = 1
list1 = ['a','b','c']
dic1 = {'name':'anna',
        'age':18,
        }

#只在本函数执行  不在模块中执行
if __name__ == '__main__':
    print("return MyPrint1 is :",MyPrint1(num,'z1','z2',list1,dic1))
    print("**************************************************")
    print("return MyPrint2 is :",MyPrint2(name = "mike",age = "16"))