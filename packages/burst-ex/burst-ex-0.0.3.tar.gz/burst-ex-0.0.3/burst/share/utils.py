# -*- coding: utf-8 -*-

import functools
import random

from .six import string_types
from .log import logger


def safe_call(func, *args, **kwargs):
    """
    安全调用
    """
    try:
        return func(*args, **kwargs)
    except Exception as e:
        logger.error('exc occur. e: %s, func: %s', e, func, exc_info=True)
        # 调用方可以通过 isinstance(e, BaseException) 来判断是否发生了异常
        return e


def safe_func(func):
    """
    把函数变为安全的
    """
    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        return safe_call(func, *args, **kwargs)
    return func_wrapper


def ip_bin_to_str(ip_num):
    """
    转换ip格式，从bin转为str
    :param ip_num:
    :return:
    """
    import socket
    return socket.inet_ntoa(ip_num)


def ip_str_to_bin(ip_str):
    """
    转化ip格式，从str转为bin
    :param ip_str:
    :return:
    """
    import socket
    return socket.inet_aton(ip_str)


def import_module_or_string(src):
    """
    按照模块导入或者字符串导入
    :param src:
    :return:
    """
    from .config import import_string
    return import_string(src) if isinstance(src, string_types) else src


class SequenceNumber(int):
    INDEX_MAX = 0x1f            # 31
    GROUP_MAX = 0x3ff           # 1023
    REQUEST_MAX = 0xffffffff    # 4294967295
    
    def __init__(self, x):
        """
        网关协议头的userdata是64位的long long类型；
        低32位，存储自增序号，即request_index；
        高32位，存储连接标识，如下：

            src_index(5)     dst_index(5)
        |--|-----|----------|-----|----------|
         00(2)    src_group_id(10) dst_group_id(10)
        """
        super(SequenceNumber, self).__init__(x)
        
        self.request_index = x & self.REQUEST_MAX       # 0 - 4294967295
        
        self.src_index = (x >> 57) & self.INDEX_MAX     # 1 - 31
        self.src_group_id = (x >> 47) & self.GROUP_MAX  # 1 - 1023
        self.dst_index = (x >> 42) & self.INDEX_MAX     # 1 - 31
        self.dst_group_id = (x >> 32) & self.GROUP_MAX  # 1 - 1023
        
        self.connection_identifier = "%02d-%04d-%02d-%04d" % (
            self.src_index, self.src_group_id, self.dst_index, self.dst_group_id)
    
    def __str__(self):
        return "%s-%010d" % (self.connection_identifier, self.request_index)
    
    def is_valid(self):
        return self.src_index > 0 and self.src_group_id > 0 and self.dst_index > 0 and self.dst_group_id > 0


class InnerCmdACK(object):
    SEND_RETRY = 20
    RECV_RETRY = 30
    
    @staticmethod
    def get_pubsub_channel(connection_identifier):
        return "inner_cmd_pubsub:%s" % connection_identifier
    
    @staticmethod
    def get_send_queue(connection_identifier):
        return "inner_cmd_send_queue:%s" % connection_identifier
    
    @staticmethod
    def get_recv_queue(connection_identifier):
        return "inner_cmd_recv_queue:%s" % connection_identifier


def hit(percent):
    return random.randint(1, 100) <= percent
