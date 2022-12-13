import os
import unittest

from parameterized import parameterized


def get_filename(file_name):
    # 与浏览器默认下载目录里文件名一一比较
    file_list = os.listdir('C:/Users/caojingwei/Downloads')
    for i in file_list:
        if i.find(file_name) != -1:
            return True
    # 实在找不到，返回一个异常语句
    return False
