from .client import Client
from .consts import *


class TradeAPI(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, flag='1'):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag)

    # Place Order
    def place_order(self, instId, tdMode, side, ordType, sz, ccy=None, clOrdId=None, tag=None, posSide=None, px=None,
                    reduceOnly=None):
        params = {'instId': instId, 'tdMode': tdMode, 'side': side, 'ordType': ordType, 'sz': sz, 'ccy': ccy,
                  'clOrdId': clOrdId, 'tag': tag, 'posSide': posSide, 'px': px, 'reduceOnly': reduceOnly}
        return self._request_with_params(POST, PLACE_ORDER, params)

        # Place  Order 2
    def place_order2(self, instId, tdMode, side, ordType, sz, ccy=None,clOrdId=None, tag=None, posSide=None, px=None,
                     reduceOnly=None,tpTriggerPxType=None, tpTriggerPx=None, tpOrdPx=None, slTriggerPxType=None,
                     slTriggerPx=None, slOrdPx=None,triggerPx=None, orderPx=None):
            params = {'instId': instId, 'tdMode': tdMode, 'side': side, 'ordType': ordType, 'sz': sz, 'ccy': ccy,
                      'clOrdId':clOrdId, 'tag':tag,  'posSide': posSide, 'px':px,'reduceOnly': reduceOnly,
                      'tpTriggerPxType': tpTriggerPxType, 'tpTriggerPx': tpTriggerPx,'tpOrdPx': tpOrdPx,
                      'slTriggerPxType': slTriggerPxType,'slTriggerPx': slTriggerPx, 'slOrdPx': slOrdPx,
                      'triggerPx': triggerPx, 'orderPx': orderPx}
            return self._request_with_params(POST, PLACE_ORDER, params)

    # Place Multiple Orders
    def place_multiple_orders(self, orders_data):
        return self._request_with_params(POST, BATCH_ORDERS, orders_data)

    # Cancel Order
    def cancel_order(self, instId, ordId=None, clOrdId=None):
        params = {'instId': instId, 'ordId': ordId, 'clOrdId': clOrdId}
        return self._request_with_params(POST, CANAEL_ORDER, params)

    # Cancel Multiple Orders
    def cancel_multiple_orders(self, orders_data):
        return self._request_with_params(POST, CANAEL_BATCH_ORDERS, orders_data)

    # Amend Order
    def amend_order(self, instId, cxlOnFail=None, ordId=None, clOrdId=None, reqId=None, newSz=None, newPx=None):
        params = {'instId': instId, 'cxlOnFailc': cxlOnFail, 'ordId': ordId, 'clOrdId': clOrdId, 'reqId': reqId,
                  'newSz': newSz,
                  'newPx': newPx}
        return self._request_with_params(POST, AMEND_ORDER, params)

    # Amend Multiple Orders
    def amend_multiple_orders(self, orders_data):
        return self._request_with_params(POST, AMEND_BATCH_ORDER, orders_data)

    # Close Positions
    def close_positions(self, instId, mgnMode, posSide=None, ccy=None):
        params = {'instId': instId, 'mgnMode': mgnMode, 'posSide': posSide, 'ccy': ccy}
        return self._request_with_params(POST, CLOSE_POSITION, params)
        # Close Positions

    def close_positions2(self, instId, mgnMode, posSide=None, ccy=None,autoCxl=None):
        params = {'instId': instId, 'mgnMode': mgnMode, 'posSide': posSide, 'ccy': ccy,'autoCxl':autoCxl}
        return self._request_with_params(POST, CLOSE_POSITION, params)

    # Get Order Details
    def get_orders(self, instId, ordId=None, clOrdId=None):
        params = {'instId': instId, 'ordId': ordId, 'clOrdId': clOrdId}
        return self._request_with_params(GET, ORDER_INFO, params)

    # Get Order List
    def get_order_list(self, instType=None, uly=None, instId=None, ordType=None, state=None, after=None, before=None, limit=None):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordType': ordType, 'state': state,
                  'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, ORDERS_PENDING, params)

    # Get Order History (last 7 days）
    def get_orders_history(self, instType, uly=None, instId=None, ordType=None, state=None, after=None, before=None, limit=None):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordType': ordType, 'state': state,
                  'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, ORDERS_HISTORY, params)

    # Get Order History (last 3 months)
    def orders_history_archive(self, instType, uly=None, instId=None, ordType=None, state=None, after=None, before=None, limit=None):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordType': ordType, 'state': state,
                  'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, ORDERS_HISTORY_ARCHIVE, params)

    # Get Transaction Details
    def get_fills(self, instType=None, uly=None, instId=None, ordId=None, after=None, before=None, limit=None):
        params = {'instType': instType, 'uly': uly, 'instId': instId, 'ordId': ordId, 'after': after, 'before': before,
                  'limit': limit}
        return self._request_with_params(GET, ORDER_FILLS, params)

    # Place Algo Order
    def place_algo_order(self, instId, tdMode, side, ordType, sz, ccy=None, posSide=None, reduceOnly=None, tpTriggerPx=None,
                         tpOrdPx=None, slTriggerPx=None, slOrdPx=None, triggerPx=None, orderPx=None):
        params = {'instId': instId, 'tdMode': tdMode, 'side': side, 'ordType': ordType, 'sz': sz, 'ccy': ccy,
                  'posSide': posSide, 'reduceOnly': reduceOnly, 'tpTriggerPx': tpTriggerPx, 'tpOrdPx': tpOrdPx,
                  'slTriggerPx': slTriggerPx, 'slOrdPx': slOrdPx, 'triggerPx': triggerPx, 'orderPx': orderPx}
        return self._request_with_params(POST, PLACE_ALGO_ORDER, params)

    # Place Algo Order 2
    def place_algo_order2(self, instId, tdMode, side, ordType, sz, ccy=None, posSide=None, reduceOnly=None,tpTriggerPxType=None,
                         tpTriggerPx=None, tpOrdPx=None,slTriggerPxType=None,slTriggerPx=None, slOrdPx=None, triggerPx=None, orderPx=None):
        params = {'instId': instId, 'tdMode': tdMode, 'side': side, 'ordType': ordType, 'sz': sz, 'ccy': ccy,
                  'posSide': posSide, 'reduceOnly': reduceOnly, 'tpTriggerPxType':tpTriggerPxType,''
                  'tpTriggerPx': tpTriggerPx, 'tpOrdPx': tpOrdPx,'slTriggerPxType':slTriggerPxType,
                  'slTriggerPx': slTriggerPx, 'slOrdPx': slOrdPx, 'triggerPx': triggerPx, 'orderPx': orderPx}
        return self._request_with_params(POST, PLACE_ALGO_ORDER, params)

    # Cancel Algo Order
    def cancel_algo_order(self, params):
        return self._request_with_params(POST, CANCEL_ALGOS, params)

    # Get Algo Order List
    def order_algos_list(self, ordType, algoId=None, instType=None, instId=None, after=None, before=None, limit=None):
        params = {'ordType': ordType, 'algoId': algoId, 'instType': instType, 'instId': instId, 'after': after,
                  'before': before, 'limit': limit}
        return self._request_with_params(GET, ORDERS_ALGO_OENDING, params)

    # Get Algo Order History
    def order_algos_history(self, ordType, state=None, algoId=None, instType=None, instId=None, after=None, before=None, limit=None):
        params = {'ordType': ordType, 'state': state, 'algoId': algoId, 'instType': instType, 'instId': instId,
                  'after': after, 'before': before, 'limit': limit}
        return self._request_with_params(GET, ORDERS_ALGO_HISTORY, params)
