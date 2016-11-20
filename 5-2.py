# -*- coding: utf-8 -*-

gloCount = 0;

def func(nameList, startWith, count):
    global gloCount
    #定义递归结束条件
    if(len(nameList) == 0):
        return 0;
    n = len(nameList);
    k = count % n;
    s = startWith - 1;
    #此时进行顺时针报数
    if gloCount % 2 == 0:
        s = s % n;
        p = (k + s)%n;
        print(nameList[p]);
        del nameList[p];
        gloCount = gloCount + 1;
        func(nameList, startWith, count)
    #此时进行逆时针报数
    else:
        s = s % n;
        p = (s + n - k) % n;
        print(nameList[p]);
        del nameList[p];
        gloCount = gloCount + 1;
        func(nameList, startWith, count)
        
strn = input("请输入总人数：")
n = int(strn);
stra = input("请输入开始号码：")
a = int(stra);
strm = input("请输入每次出局的号码：")
m = int(strm);

#生成号码列表

nameList = [ x for x in range(1,n+1) ];

func(nameList, a, m);


    


 