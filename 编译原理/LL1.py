# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
/home/latyas/.spyder2/.temp.py
"""
from basic.definition import *

class LL1Parser:
    def __init__(self):
        pass
        self.STATEMENTS = {}
        self.FIRST = {}
        self.FOLLOW = {}
        self.EPSILON = Symbol('epsilon','T')
        self.DOLLOR = Symbol('$','T')
    def add_symbol(self,name,attr):
        """
        :param name: 符号助记符
        :param attr: 符号属性，可选值为T或NT
        :type attr: str
        """
        if attr != 'T' and attr != 'NT':
            raise TypeError("符号属性设置错误")
    
    def cal_first(self,symbol):
        #symbol.is_terminal 则直接返回只有该符号的集合
        #选出STATEMENTS中key=symbol的推导式
        #以此遍历右端每个符号
            #如果当前遍历到的符号是symbol，则函数返回不做处理
        """
        依据：
            1. A->Ac
            2. A->Bd
            3. B->r
            如果没有2.则1.会进入无限递归
            考虑有推导A->Ac->Bdc->rdc, r是A的First集中的元素
            忽略掉左递归的1,通过2,3也一样可以得出同样的结果
            需要提交的语法没有不可化简的左递归
        """
            #获得该符号的first集
            #如果该符号的first集不包含ESP，则symbol的first集为这个first集
            #如果该符号的first集包含ESP，则symbol的first集并上这个first集后，继续扫描下一个符号
            #若所有的符号都可以导出ESP，则将ESP加入symbol的first集
        pass
    
    
    def cal_follow(self,symbol):
        #symbol.is_terminal 则直接返回只有该符号的集合
        #遍历STATEMENTS中右端含有symbol的推导式
            #A->aBcd，symbol=B
            #1. A->aB，即B后无符号： FOLLOW(B)内加入FOLLOW(A)
            #2. A->aBc，c的first集为terminal，无ESP , FOLLOW(B)内加入FIRST(c)
            #3. A->aBcd, c的first集中有ESP，则FOLLOW(A)加入去掉ESP的FIRST(c),并扫描下一个符号
            #如果B后的符号都可以导出ESP,则运用规则1后在FOLLOW(B)中加入ESP
        pass
