# coding:utf-8

# coding=utf-8


class TipException(Exception):
    """
    @attention: 提示类异常,用于业务阻断时,直接返回请求
    """

    def __init__(self, msg):
        self.msg = msg

    def show_msg(self):
        return self.msg


class ReasonException(Exception):
    """
    只需要原因的日志
    """

    def __init__(self, msg, module_name, msg_template=None):
        """

        :param msg:
        :param module_name:
        :param msg_template:  必须接收 reason参数
        """
        self.msg = msg
        self.module_name = module_name
        self.msg_template = msg_template


class SpecialReasonException(Exception):
    """
    特殊异常
    """

    def __init__(self, msg, module_name, msg_template, inner_info):
        self.msg_template = msg_template
        self.module_name = module_name
        self.msg = msg
        self.inner_info = inner_info
