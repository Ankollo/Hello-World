
dic1 = {'name':'Mike',
        'sex':'male',
        'age':18, 
        }
print(dic1['name'])
dic1['school'] = 'little'
print(dic1)
del dic1['age']    #删除键-值对
print(dic1)

#遍历字典
for k,v in dic1.items():
    print('\nkeys:'+k)
    print('values:'+v)

#遍历键
for k in dic1.keys():
    print('keys:'+k)

#遍历值
for v in dic1.values():
    print('value:'+v)

#集合set()  元素无重复
for v in set(dic1.values()):
    print('value:'+v)

'''列表对应数组，字典对应结构体'''
#字典列表
list1 = [{'name':'xiaoming','age':'18','sex':'male'},
        {'name':'xiaohong','age':'16','sex':'female'},
        {'name':'xiaogang','age':'19','sex':'male'},
        ]
for l in list1:
    print(l)

#列表字典
dic2 = {'name':'mike',
        'language':['c','c++','python']
        }
print(dic2)

#字典字典
dic3 = {'mike':{
                'first':'a',
                'last':'b',
                'age':15,
                },
        'mali':{
                'first':'x',
                'last':'y',
                'age':16,
                }
        }
print(dic3)