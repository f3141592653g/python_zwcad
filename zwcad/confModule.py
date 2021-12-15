# -*- coding:utf-8 _*-
""" 
@author:mongo
@time: 2018/12/17 
@email:3126972006@qq.com
@function： 
"""
import configparser

import contants


class ReadConfig:
    """
    完成配置文件的读取
    """

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(contants.FTP_path, encoding='utf-8')  # 先加载global

    def get(self, section, option):
        return self.config.get(section, option)

if __name__ == '__main__':
    print(ReadConfig().get('FTP_value', 'host'))
