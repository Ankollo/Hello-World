#字符串的相关操作
name = 'MIke'
CharNum = '66'
IntNum = 88

print(name.title())    #首字母大写
print(name.upper())    #全部大写
print(name.lower())    #全部小写
print(int(CharNum)+33)    #字符转换数字
print(('This is char '+str(IntNum)+'.\n').rstrip())  #数字转换成字符  删除多余空行

#list的相关操作
list1 = ['abc','bcd','cde']
list1.append('def')    #添加元素
list1.insert(0,'000')    #在指定位置添加元素
del list1[-1]    #删除最后一个元素
elem = list1.pop(-1)    #弹出最后一个元素给 elem 可以弹出任意位置的元素
list1.remove('abc')    #根据值删除元素
print(elem)
for lis in list1[:]:    #list[:] 是list[]的副本
    print(lis)

list2 = [65,85,63,94,22,518,36,12]
list2.sort()    #对元素进行永久排序
print(list2)
list2.sort(reverse=True)    #对元素进行 从大到小 永久排序
print(list2)
print(sorted(list2))    #对元素进行临时性排序
print(len(list2))    #确定列表的长度

#range()  函数左闭右开
for ran in range(1,10,1): 
    print(ran)

#列表解析
squares = [value**2 for value in range(1,11,1)]
print(squares)

#不可变的列表叫做元组  只能整体赋值
yuanzu = (100,200)
print(yuanzu)