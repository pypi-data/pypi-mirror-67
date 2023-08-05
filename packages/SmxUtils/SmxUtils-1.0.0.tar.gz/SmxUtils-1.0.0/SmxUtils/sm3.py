# _*_coding:utf-8_*_
"""
@ProjectName: Chaos
@Author:  Javen Yan
@File: sm3.py
@Software: PyCharm
@Time :    2019/11/27 下午3:38
"""
import ctypes
from ctypes import *
import os

current_path = os.path.dirname(os.path.abspath(__file__))
loader = ctypes.cdll.LoadLibrary
soPath = os.path.join(current_path, 'ICitySMX.so')
soPath2 = os.path.join(os.getcwd(), 'ICitySMX.so')
soPath3 = "/usr/lib/ICitySMX.so"
if os.path.isfile(soPath):
    lib = loader(soPath)
elif os.path.isfile(soPath2):
    lib = loader(soPath2)
else:
    lib = loader(soPath3)


def iCitySM3(source: bytes) -> (bool, str):
    """
    :param source: Hash数据
    :return:
    """
    c_source = c_char_p(source)
    c_length = c_int(len(source))
    c_response = c_char_p()
    c_city_sm3_digest = lib.icity_sm3_digest
    c_city_sm3_digest.argtypes = [c_char_p, c_int, POINTER(c_char_p)]
    ret = c_city_sm3_digest(c_source, c_length, byref(c_response))
    if ret == 0:
        return True, c_response.value.deocde()
    else:
        return False, "Hash失败"
