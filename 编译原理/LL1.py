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
    def add_derivation(self):
        pass
    def set_start_symbol(self, symbol):
        self.start_symbol = symbol

    def cal_first(self,symbol):
        #遇到终止符直接返回
        if symbol.attr == 'T':
            return set([symbol])

        try:
            if self.FIRST[symbol] != set():
                return self.FIRST[symbol]
        except:
            self.FIRST[symbol] = set()
        #symbol.is_terminal 则直接返回只有该符号的集合
        #选出STATEMENTS中key=symbol的推导式
        sts = self.STATEMENTS[symbol]
        for st in sts:
        #以此遍历右端每个符号
            eps = True
            for sym in st:
            #如果当前遍历到的符号是symbol，且该符号不是终止符，则函数返回不做处理
                if sym == symbol:
                    return

        
        #依据：
        #    1. A->Ac
        #    2. A->Bd
        #    3. B->r
        #    如果没有2.则1.会进入无限递归
        #    考虑有推导A->Ac->Bdc->rdc, r是A的First集中的元素
        #    忽略掉左递归的1,通过2,3也一样可以得出同样的结果
        #    需要提交的语法没有不可化简的左递归
        #
            #获得该符号的first集
                first = self.cal_first(sym)
            #如果该符号的first集不包含ESP，则symbol的first集为这个first集
                if self.EPSILON not in first:
                    self.FIRST[symbol].update(first)
                    eps = False
                    break
            #如果该符号的first集包含ESP，则symbol的first集并上这个first集后，继续扫描下一个符号
                else:
                    self.FIRST[symbol].update(first)
            #若所有的符号都可以导出ESP，则将ESP加入symbol的first集
            if eps: self.FIRST[symbol].add(self.EPSILON)
        return self.FIRST[symbol] 

    def cal_follow(self,symbol):
         #symbol.is_terminal 则直接返回只有该符号的集合
        if symbol.attr == 'T':
            return set([symbol])
        try:
            if self.FOLLOW[symbol] != set():
                return self.FOLLOW[symbol]
        except:
            self.FOLLOW[symbol] = set()
        try:
            if symbol == self.start_symbol:
                self.FOLLOW[symbol].add(self.DOLLOR)
        except:
            raise Exception('起始符没有设置')
 
        #遍历STATEMENTS中右端含有symbol的推导式
        
        sts = []
        for k,v in self.STATEMENTS.items():
            for s in v:
                if symbol in s: sts.append((k,s))
            #A->aBcd，symbol=B
            #1. A->aB，即B后无符号： FOLLOW(B)内加入FOLLOW(A)
        for key,st in sts:
            searched = st[st.index(symbol):]
            print symbol,key,searched
            if len(searched) == 1: 
                print '情况1',symbol,searched
                follow = self.cal_follow(key)
                self.FOLLOW[symbol].update(follow)
                continue
            
            esp = True

            #2. A->aBc，c的first集为terminal，无ESP , FOLLOW(B)内加入FIRST(c)
            for sym in searched[1:]:
                first = self.cal_first(sym)
                if self.EPSILON not in first:
                    self.FOLLOW[symbol].update(first)
                    esp = False
                    break
            #3. A->aBcd, c的first集中有ESP，则FOLLOW(A)加入去掉ESP的FIRST(c),并扫描下一个符号
                else:
                    foo = first
                    foo.remove(self.EPSILON)
                    self.FOLLOW[symbol].update(foo)
            #如果B后的符号都可以导出ESP,则运用规则1后在FOLLOW(B)中加入FOLLOW(A)
            if esp: self.FOLLOW[symbol].update(self.cal_follow(key))
        return self.FOLLOW[symbol]

def main_3():
    ll = LL1Parser()
    E = Symbol('E','NT')
    T = Symbol('T','NT')
    E2 = Symbol('E\'','NT')
    plus = Symbol('+','T')
    F = Symbol('F','NT')
    T2 = Symbol('T\'','NT')
    times = Symbol('*','T')
    l_b = Symbol('(','T')
    r_b = Symbol(')','T')
    i = Symbol('i','NT')
    ll.STATEMENTS[E] = [[T,E2]]
    ll.STATEMENTS[E2] = [[plus,T,E2],[ll.EPSILON]]
    ll.STATEMENTS[T] = [[F,T2]]
    ll.STATEMENTS[T2] = [[times,F,T2],[ll.EPSILON]]
    ll.STATEMENTS[F] = [[l_b,E,r_b],[i]]
    
    ll.set_start_symbol(E)
    ll.cal_follow(F)
    print ll.FOLLOW[F]
def main():
    ll = LL1Parser()
    A = Symbol('A','NT')
    B = Symbol('B','NT')
    S = Symbol('S','NT')
    c = Symbol('c','T')
    a = Symbol('a','T')
    b = Symbol('b','T')
   
    ll.STATEMENTS[S]=[[A,B,c]]
    ll.STATEMENTS[A]=[[a],[ll.EPSILON]]
    ll.STATEMENTS[B]=[[b],[ll.EPSILON]]
    ll.cal_first(S)
    ll.cal_first(A)
    ll.cal_first(B)
    
    ll.set_start_symbol(S)
    ll.cal_follow(S)
    ll.cal_follow(A)
    ll.cal_follow(B)

    print ll.FIRST[S]
    print ll.FIRST[A]
    print ll.FIRST[B]
    print ll.FOLLOW[S]
    print ll.FOLLOW[A]
    print ll.FOLLOW[B]
if __name__ == '__main__':
    main()
