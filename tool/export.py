import os
import unittest

from parameterized import parameterized


def get_filename(file_name):
    file_list = os.listdir('C:/Users/caojingwei/Downloads')
    exit_is = "不存在"
    for i in file_list:
        if i.find(file_name) != -1:
            exit_is = "存在"
            break
    msg = file_name +"-----"+ exit_is
    return msg
    # print(file_name +"-----"+ exit_is)


class TestFile(unittest.TestCase):
    @parameterized.expand(['线索信息_未指派', '线索信息_已指派', '线索信息_作废',
                           '线索跟踪信息_跟踪中', '线索跟踪信息_已完成', '线索跟踪信息_已终止',
                           '征集录入_未提交', '征集录入_已提交',
                           '征集中_待鉴定', '征集中_已鉴定', '征集中_已终止',
                           '确认征集_未征集',
                           '拨库管理_待拨库', '拨库管理_已拨库'])
    def test01(self, file_name):
        get_filename(file_name)

    # get_filename('线索信息_未指派')
