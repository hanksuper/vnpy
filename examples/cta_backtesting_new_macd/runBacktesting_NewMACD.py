# -*- encoding: utf-8 -*-
"""
@File    :   runBacktesting_NewMACD.py
@Contact :   liuhaobwjc@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019-03-21 19:59   liuhao      1.0        用于回测NewMACD策略
"""
from __future__ import division

from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, MINUTE_DB_NAME, TICK_DB_NAME

if __name__ == '__main__':
    from vnpy.trader.app.ctaStrategy.strategy.strategyNewMACD import NewMacdStrategy

    # 创建回测引擎
    engine = BacktestingEngine()

    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.TICK_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20130104', initDays=0)

    # 设置产品相关参数
    engine.setSlippage(0)  # 股指1跳
    engine.setRate(0.115 / 10000)  # 万0.115
    engine.setSize(1)  # 股指合约大小
    engine.setPriceTick(0.2)  # 股指最小价格变动

    # 设置使用的历史数据库
    engine.setDatabase(TICK_DB_NAME, 'rb_tick_data_2013')

    # 在引擎中创建策略对象
    d = {}
    engine.initStrategy(NewMacdStrategy, d)

    # 开始跑回测
    engine.runBacktesting()

    # 显示回测结果
    engine.showBacktestingResult()
