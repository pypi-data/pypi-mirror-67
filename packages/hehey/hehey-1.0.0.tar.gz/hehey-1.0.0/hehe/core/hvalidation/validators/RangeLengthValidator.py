# -*- coding: utf-8 -*-
from ..base.Validator import Validator
"""
 * 字符长度范围验证器
 *<B>说明：</B>
 *<pre>
 * 规则格式:
 * ['attrs',[['len',{min':6,'max':16}]],{'message'=>'请输入一个长度为合法的6-16的字符串'}]
 * ['attrs',[['len',{min':6}]],{'message'=>'请输入一个长度大于等于6的字符串'}]
 * ['attrs',[['len',{'max':16}]],{'message'=>'请输入一个长度小于等于16的字符串'}]
 *</pre>
"""
class RangeLengthValidator(Validator):

    def __init__(self,attrs):
        self.min = None
        self.max = None

        super().__init__(attrs)

    def validateValue(self,value,name = None):

        valueLen = len(str(value))
        result = True

        if self.min is not None:
            if valueLen < self.min:
                result = False

        if self.max is not None:
            if valueLen > self.max:
                result = False

        if result:
            return True
        else:
            self.addParams({
                'min': self.min,
                'max': self.max
            })

        return result;

