# -*- encoding: utf-8 -*-
"""
@File    :   loadTickCsv.py
@Contact :   liuhaobwjc@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-03-21 19:51   liuhao      1.0       导入历史Tick级别数据到MongoDB
"""

from vnpy.trader.app.ctaStrategy.ctaBase import TICK_DB_NAME
from vnpy.trader.app.ctaStrategy.ctaHistoryData import loadTickCsv

if __name__ == '__main__':
    loadTickCsv('rb_tick_data_2013.csv', TICK_DB_NAME, 'rb_tick_data_2013')

