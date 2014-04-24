# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 21:00:17 2014

@author: latyas
"""

#针对具体的某个Token
class Token:
    def __init__(self, name, attr, lineno):
        """
        :param name: token 的符号标识
        :type name: str
        
        :param attr: token 的类型标识
        :type attr: str
        
        :param lineno: 该 token 所在的行号
        :type lineno: int
        
        """
        self.name = name
        self.attr = attr
        self.lineno = lineno

class Symbol:
    def __init__(self, name ,attr):
        """
        :param name: 符号的助记符
        :param attr: 符号的类型
        :type attr: str, 只能是 T:终止符， NT:非终止符
        """
        self.name = name
        self.attr = attr
        if attr != 'T' and attr != 'NT':
            raise TypeError("符号属性设置错误")
            
    def is_terminal(self):
        """
        :returns: Boolean 是否是种植符
        """
        if self.attr == 'T':
            return True
        else:
            return False