# -*- encoding: utf-8 -*-
"""
@File    :   dataClean.py    
@Contact :   liuhaobwjc@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-04-01 10:26   liuhao      1.0         None
"""
import pandas as pd

if __name__ == "__main__":
    columns = ['date', 'time', 'open', 'bid1', 'ask1', 'lastPrice', 'volume', 'openInterest']
    primary_data = pd.read_csv('tickData2013.csv', header=None, names=columns)
    primary_data['lastVolume'] = primary_data['volume'] - primary_data['volume'].shift(1)
    primary_data[primary_data['lastVolume'] < 0] = 0
    primary_data = primary_data[('15:30:01' > primary_data['time']) & (primary_data['time'] > '08:59:59')]
    primary_data[['lastVolume']] = primary_data[['lastVolume']].astype(int)
    primary_data.to_csv('rb_tick_data_2013.csv', index=False)