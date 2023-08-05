# -*- coding: utf-8 -*-
from iqsopenapi.util import *
from iqsopenapi.util.logutil import *
from iqsopenapi.trade.realtrade.message import *
from iqsopenapi.trade.realtrade.Models import *
import uuid
import threading
import time

class PushQuoteSubscriber(object):
    '''实盘推送'''
    def __init__(self, cfg, strategy_id, user):
        '''初始化websocket'''

        self.__cfg = cfg
        self.__strategy_id = strategy_id
        self.__user_info = user
        #自动重连检测时间
        self.__AutoReconnectInterval = 10
        self.__wsClient = WebSocketClient(cfg)

    def Connect(self):
        # 连接websocket
        if not self.__wsClient.Connect():
            self.__wirteError("connect failed!")
            return False
        if not self.__SetAccountInfo():
            self.__wirteError("subscribe failed!")
            return False

        t = threading.Thread(target=self.__AuotReconnect,args=(self.__wsClient,))
        t.start()
        return True

    def __SetAccountInfo(self):
        user = self.__user_info
        req = {
            "requestType":RequestType.TradePushConect.name,
            "reqId":uuid.uuid1().hex,
            "brokerAccount":user.AccountID,
            "counterId":user.CounterID,
            "brokerType":user.BrokerType,
        }
        message = json.dumps(req,ensure_ascii=False)
        if not self.__Send(id,message):
            self.__wirteError("set account info fail :{0}".format(message))
            return False
        return True

    def __Send(self,id,msg):
        """消息发送"""
        if not msg: return False
        if not self.__wsClient.Send(msg):
            self.__wirteError("send fail:{0}".format(msg))
            return False
        return True

    def __AuotReconnect(self,client):
        """自动连接"""
        while True:
            try:
                if not client.IsConnected():
                    self.__wirteInfo("未连接，尝试连接...")
                    ret = client.Connect()
                    self.__wirteInfo("重连完成：{0}".format(ret))
            except Exception as e:
                self.__wirteError('自动连接异常:{0}'.format(e))
            time.sleep(self.__AutoReconnectInterval)

    def __OnRecv(self,msg):
        '''收到消息'''
        if not msg: return
        # 心跳消息直接返回
        if msg.get("requestType") == ResponseType.HeartBeat.name: return
        cfg = self.__cfg
        if not cfg: return
        cfg.recvCallback(msg)

    def __wirteError(self, error):
        '''写错误日志'''
        logger.error(error)

    def __wirteInfo(self, info):
        '''写日志'''
        logger.info(info)
