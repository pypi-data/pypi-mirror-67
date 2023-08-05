# -*- coding: utf-8 -*-
"""
20200410 lw

"""

import pandas as pd
import pymongo
from pyalgotrade.utils import gmEnum


from pyalgotrade.positionHelpBylw import Positions, cusHoldingPostion




class cusTrade():

    def __init__(self,tradeId,symbol,side,positionEffect,price,volume,datetime):
        self._tradeid=tradeId
        self._symbol = symbol
        # self.positionSide = None

        self._side = side  # 买还是卖
        self._positionEffect = positionEffect  # 开仓还是平仓


        self._price=price #此次成交的成交价格。
        self._volume = volume  #此次成交的 数量
        # self.commission=None #此次成交 缴纳的手续费

        # 这2个时间限制为datetime形式。
        self._created_at = datetime

        self._targetPositionSide=self._calPositionSide()
     #根据trade 描述出，改交易针对的是多头持仓，还是空头持仓
    def _calPositionSide(self):
        if self._positionEffect in [gmEnum.PositionEffect_Close, gmEnum.PositionEffect_CloseToday,
                                         gmEnum.PositionEffect_CloseYesterday]:

            # 本次平仓的成交完成了，需要取查 该持仓是否 还在，如果不在了，就要剔除相关止盈止损指令等。

            side_ = self._side
            if side_==1: #买平，表明针对空头持仓
                gmPos_=2
            if side_==2: #卖平，表明针对多头持仓
                gmPos_=1
        if self._positionEffect  in [gmEnum.PositionEffect_Open]:
            side_ = self._side   #买方向是1，卖方向是2，掘金中 多头方向也是1，空头方向也是2
            gmPos_=side_

        return gmPos_


    def getSymbol(self):
        return self._symbol
    def getSide(self):
        return self._side
    def getPositionEffect(self):
        return self._positionEffect
    def getPrice(self):
        return self._price
    def getVolume(self):
        return self._volume
    def getTradeTime(self):
        return self._created_at

    def getTargetPositionSide(self):
        return self._targetPositionSide




class mongoTrade():
    #=dbname='real_short_period',collectionname='holding'
    def __init__(self, dbname,collectionname,host='localhost'):
        client = pymongo.MongoClient(host=host, port=27017,tz_aware=True)
        db = client[dbname]
        self.collection = db[collectionname]

    def addARecordFromGm(self,gmTrade,updateWrite=False):


        tempdict={}
        tempdict['_id']=gmTrade['exec_id']
        tempdict['symbol'] =gmTrade['symbol']
        tempdict['positionEffect'] = gmTrade['position_effect']
        tempdict['side'] = gmTrade['side']
        tempdict['price'] = gmTrade['price']
        tempdict['volume'] = gmTrade['volume']
        tempdict['created_at'] = gmTrade['created_at']
        if not updateWrite:
            self.collection.insert_one(tempdict)
        else:
            self.collection.save(tempdict)



    # 获取全部成交记录
    def getAllTrades(self, timeZoneNum=8,returnType=1):
        #1 表示返回custrade类型,2表示返回dataframe类型
        trades = self.collection.find().sort('created_at',1)
        if returnType==2:
            dftrades = pd.DataFrame(list(trades))
            return dftrades
        if returnType==1:
            cusTradeList=[]
            for atrade in trades:
                acusTradeObj=cusTrade(atrade['_id'],atrade['symbol'],\
                                      atrade['side'],atrade['positionEffect'],\
                                      atrade['price'],atrade['volume'],\
                                      atrade['created_at'])
                cusTradeList.append(acusTradeObj)
            return cusTradeList




