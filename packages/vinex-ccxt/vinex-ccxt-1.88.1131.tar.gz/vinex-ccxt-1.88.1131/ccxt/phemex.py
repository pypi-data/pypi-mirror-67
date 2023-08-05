# -*- coding: utf-8 -*-

# PLEASE DO NOT EDIT THIS FILE, IT IS GENERATED AND WILL BE OVERWRITTEN:
# https://github.com/ccxt/ccxt/blob/master/CONTRIBUTING.md#how-to-contribute-code

import math

from ccxt.base.decimal_to_precision import DECIMAL_PLACES
from ccxt.base.decimal_to_precision import PAD_WITH_ZERO
from ccxt.base.decimal_to_precision import ROUND
from ccxt.base.errors import AuthenticationError
from ccxt.base.errors import DDoSProtection
from ccxt.base.errors import ExchangeError
from ccxt.base.errors import ExchangeNotAvailable
from ccxt.base.errors import InsufficientFunds
from ccxt.base.errors import InvalidOrder
from ccxt.base.errors import OrderNotFound
from ccxt.base.errors import PermissionDenied
from ccxt.base.exchange import Exchange


class phemex(Exchange):

    def convert_time_ns(self, ns):
        return int(math.floor(ns * math.pow(10, -6)))

    def convert_e_number(self, eNum, scale, precision, roundType):
        return self.decimal_to_precision(eNum * math.pow(10, -scale), roundType, precision, DECIMAL_PLACES,
                                         PAD_WITH_ZERO)

    def convert_ev(self, ev, scale, precision):
        return self.convert_e_number(ev, scale, precision, ROUND)

    def convert_er(self, er, scale, precision):
        return self.convert_e_number(er, scale, precision, ROUND)

    def convert_ep(self, ep, scale, precision):
        if ep is None:
            return None
        return self.convert_e_number(ep, scale, precision, ROUND)

    def convert_to_ep(self, price):
        return price * math.pow(10, 4)

    def calc_average_ep(self, filledEv, valueScale, priceScale, filled, contractSide):
        if filled == 0:
            return None
        if filledEv == 0:
            return None
        priceFactor = math.pow(10, priceScale)
        valueFactor = math.pow(10, valueScale)
        return math.pow(filledEv / (valueFactor * filled), contractSide) * priceFactor

    def calc_cost_ev(self, filled, averageEp, priceEp, priceScale, valueScale, contractSide):
        if filled == 0:
            return 0
        ep = None
        if averageEp is not None:
            ep = averageEp
        elif priceEp is not None:
            ep = priceEp
        if ep is None:
            return None
        priceFactor = math.pow(10, priceScale)
        valueFactor = math.pow(10, valueScale)
        return filled * math.pow(ep / priceFactor, contractSide) * valueFactor

    def parse_response(self, response):
        return self.safe_value(response, 'data', None)

    def parse_md_response(self, response):
        return self.safe_value(response, 'result', None)

    def parse_market(self, product, precisions):
        id = self.safe_string(product, 'symbol')
        quoteCurrency = self.safe_string(product, 'quoteCurrency')
        settlementCurrency = self.safe_string(product, 'settlementCurrency')
        underlyingSymbol = self.safe_string(product, 'underlyingSymbol')
        baseId = underlyingSymbol.split('.')[1]
        quoteId = quoteCurrency
        base = self.safe_currency_code(baseId)
        quote = self.safe_currency_code(quoteId)
        return {
            'id': id,
            'symbol': base + '/' + quote,
            'base': base,
            'quote': quote,
            'baseId': baseId,
            'quoteId': quoteId,
            'contractSide': 1 if (quoteCurrency == settlementCurrency) else -1,
            'type': 'future',
            'spot': False,
            'future': True,
            'active': True,
            'priceScale': self.safe_integer(product, 'priceScale', 1),
            'ratioScale': self.safe_integer(product, 'ratioScale', 1),
            'valueScale': self.safe_integer(product, 'valueScale', 1),
            'precision': self.safe_value(precisions, id),
            'limits': {
                'amount': {
                    'min': 1,
                    'max': product['maxOrderQty'],
                },
                'price': {
                    'min': None,
                    'max': product['maxPriceEp'],
                },
                'cost': {
                    'min': None,
                    'max': None,
                },
            },
            'info': product,
        }

    def parse_bid_ask(self, bidask, priceKey=0, amountKey=1, priceScale=4, pricePrecision=1):
        priceEp = bidask[priceKey]
        price = float(self.convert_ep(priceEp, priceScale, pricePrecision))
        amount = float(bidask[amountKey])
        return [price, amount]

    def parse_bids_asks(self, bidasks, priceKey=0, amountKey=1, priceScale=4, pricePrecision=1):
        result = []
        for i in range(0, len(bidasks)):
            bidask = self.parse_bid_ask(bidasks[i], priceKey, amountKey, priceScale, pricePrecision)
            result.append(bidask)
        return result

    def parse_order_book(self, orderbook, timestamp=None, bidsKey='bids', asksKey='asks', priceKey=0, amountKey=1,
                         market=None):
        # market data
        precisions = self.safe_value(market, 'precision')
        priceScale = self.safe_integer(market, 'priceScale')
        pricePrecision = self.safe_integer(precisions, 'price')
        rawBids = self.safe_value(orderbook, bidsKey)
        rawAsks = self.safe_value(orderbook, asksKey)
        return {
            'bids': self.sort_by(self.parse_bids_asks(rawBids, priceKey, amountKey, priceScale, pricePrecision), 0,
                                 True),
            'asks': self.sort_by(self.parse_bids_asks(rawAsks, priceKey, amountKey, priceScale, pricePrecision), 0),
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'nonce': None,
        }

    def parse_order_status(self, status):
        statuses = {
            'Untriggered': 'open',
            'Deactivated': 'closed',
            'Triggered': 'open',
            'Rejected': 'rejected',
            'New': 'open',
            'PartiallyFilled': 'open',
            'Filled': 'closed',
            'Canceled': 'canceled',
        }
        return self.safe_string(statuses, status, status)

    def parse_order(self, order, market=None):
        marketID = market['id']
        # market data
        contractSide = self.safe_integer(market, marketID, 1)
        precisions = self.safe_value(market, 'precision')
        priceScale = self.safe_integer(market, 'priceScale')
        pricePrecision = self.safe_integer(precisions, 'price')
        valueScale = self.safe_integer(market, 'valueScale')
        valuePrecision = self.safe_integer(precisions, 'value')
        # order data
        id = self.safe_string(order, 'orderID')
        type = self.safe_string_lower(order, 'ordType')
        side = self.safe_string_lower(order, 'side')
        ordStatus = self.safe_string(order, 'ordStatus')
        actionTimeNs = self.safe_integer(order, 'actionTimeNs', 0)
        transactTimeNs = self.safe_integer(order, 'transactTimeNs', 0)
        priceEp = self.safe_integer(order, 'priceEp', 0)
        amount = self.safe_integer(order, 'orderQty', 0)
        filled = self.safe_integer(order, 'cumQty', 0)
        filledEv = self.safe_integer(order, 'cumValueEv', 0)
        # derived data
        timestamp = self.convert_time_ns(actionTimeNs)
        remaining = 0
        if amount != 0:
            if filled != 0:
                remaining = max(amount - filled, 0)
        averageEp = self.calc_average_ep(filledEv, valueScale, priceScale, filled, contractSide)
        average = self.convert_ep(averageEp, priceScale, pricePrecision)
        costEv = self.calc_cost_ev(filled, averageEp, priceEp, priceScale, valueScale, contractSide)
        return {
            'info': order,
            'id': id,
            'datetime': self.iso8601(timestamp),
            'timestamp': timestamp,
            'lastTradeTimestamp': self.convert_time_ns(transactTimeNs),
            'symbol': market['symbol'],
            'type': type,
            'side': side,
            'price': self.convert_ep(priceEp, priceScale, pricePrecision),
            'amount': amount,
            'cost': self.convert_ev(costEv, valueScale, valuePrecision),
            'average': average,
            'filled': filled,
            'remaining': remaining,
            'status': self.parse_order_status(ordStatus),
            'fee': None,
        }

    def parse_orders(self, orders, market=None, since=None, limit=None, params={}):
        result = []
        ordersCount = len(orders)
        for i in range(0, ordersCount):
            result.append(self.parse_order(orders[i], market))
        return result

    def parse_my_trade(self, trade, market=None):
        marketID = market['id']
        # market data
        contractSide = self.safe_integer(market, marketID, 1)
        precisions = self.safe_value(market, 'precision')
        priceScale = self.safe_integer(market, 'priceScale')
        pricePrecision = self.safe_integer(precisions, 'price')
        valueScale = self.safe_integer(market, 'valueScale')
        valuePrecision = self.safe_integer(precisions, 'value')
        # trade data
        transactTimeNs = self.safe_integer(trade, 'transactTimeNs', 0)
        timestamp = self.convert_time_ns(transactTimeNs)
        type = self.safe_string_lower(trade, 'ordType')
        side = self.safe_string_lower(trade, 'side')
        execStatus = self.safe_string(trade, 'execStatus')
        execPriceEp = self.safe_integer(trade, 'execPriceEp', 0)
        priceEp = self.safe_integer(trade, 'priceEp', 0)
        amount = self.safe_integer(trade, 'execQty', 0)
        costEv = self.calc_cost_ev(amount, execPriceEp, priceEp, priceScale, valueScale, contractSide)
        execFeeEv = self.safe_integer(trade, 'execFeeEv', 0)
        feeRateEr = self.safe_integer(trade, 'feeRateEr', 0)
        takerOrMaker = None
        if execStatus == 'TakerFill':
            takerOrMaker = 'taker'
        elif execStatus == 'MakerFill':
            takerOrMaker = 'maker'
        return {
            'info': trade,
            'id': self.safe_string(trade, 'execID'),
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'order': self.safe_string(trade, 'orderID'),
            'type': type,
            'side': side,
            'takerOrMaker': takerOrMaker,
            'price': self.convert_ep(execPriceEp, priceScale, pricePrecision),
            'amount': amount,
            'cost': self.convert_ev(costEv + execFeeEv, valueScale, valuePrecision),
            'fee': {
                'cost': self.convert_ev(execFeeEv, valueScale, valuePrecision),
                'currency': self.safe_string(trade, 'currency'),
                'rate': self.convert_er(feeRateEr, 8, 8),
            },
        }

    def parse_my_trades(self, trades, market=None):
        result = []
        tradesCount = len(trades)
        for i in range(0, tradesCount):
            result.append(self.parse_my_trade(trades[i], market))
        return result

    def parse_md_trade(self, trade, market=None):
        # market data
        precisions = self.safe_value(market, 'precision')
        priceScale = self.safe_integer(market, 'priceScale')
        pricePrecision = self.safe_integer(precisions, 'price')
        timestampNs = trade[0]
        timestamp = self.convert_time_ns(timestampNs)
        side = trade[1].lower()
        priceEp = trade[2]
        amount = trade[3]
        return {
            'info': trade,
            'id': None,
            'timestamp': timestamp,
            'datetime': self.iso8601(timestamp),
            'symbol': market['symbol'],
            'order': None,
            'type': None,
            'side': side,
            'takerOrMaker': None,
            'price': float(self.convert_ep(priceEp, priceScale, pricePrecision)),
            'amount': amount,
            'cost': None,
            'fee': {
                'cost': None,
                'currency': None,
                'rate': None,
            },
        }

    def parse_md_trades(self, trades, market=None):
        result = []
        tradesCount = len(trades)
        for i in range(0, tradesCount):
            result.append(self.parse_md_trade(trades[i], market))
        return result

    def describe(self):
        return self.deep_extend(super(phemex, self).describe(), {
            'id': 'phemex',
            'name': 'Phemex',
            'countries': ['SC'],
            'version': 'v1',
            'userAgent': None,
            'rateLimit': 2000,
            'has': {
                'cancelAllOrders': False,
                'cancelOrder': True,
                'cancelOrders': False,
                'CORS': False,
                'createDepositAddress': False,
                'createLimitBuyOrder': True,
                'createLimitSellOrder': True,
                'createMarketBuyOrder': True,
                'createMarketSellOrder': True,
                'createOrder': True,
                'deposit': False,
                'editOrder': False,
                'fetchBalance': True,
                'fetchBidsAsks': False,
                'fetchClosedOrders': True,
                'fetchCurrencies': False,
                'fetchDepositAddress': False,
                'fetchDeposits': False,
                'fetchFundingFees': False,
                'fetchL2OrderBook': False,
                'fetchLedger': False,
                'fetchMarkets': True,
                'fetchMyTrades': True,
                'fetchOHLCV': False,
                'fetchOpenOrders': True,
                'fetchOrder': True,
                'fetchOrderBook': True,
                'fetchOrderBooks': False,
                'fetchOrders': True,
                'fetchStatus': False,
                'fetchTicker': False,
                'fetchTickers': False,
                'fetchTime': False,
                'fetchTrades': True,
                'fetchTradingFee': False,
                'fetchTradingFees': False,
                'fetchTradingLimits': False,
                'fetchTransactions': False,
                'fetchWithdrawals': False,
                'privateAPI': False,
                'publicAPI': False,
                'withdraw': False,
            },
            'timeframes': {
                '1m': '1m',
                '5m': '5m',
                '1h': '1h',
                '1d': '1d',
            },
            'urls': {
                'logo': 'https://user-images.githubusercontent.com/7397642/72579020-cd03e300-3912-11ea-9371-04cbd58c31f8.png',
                'www': 'https://phemex.com',
                'test': {
                    'public': 'https://testnet.phemex.com/api',
                    'public2': 'https://testnet-api.phemex.com',
                    'private': 'https://testnet-api.phemex.com',
                },
                'api': {
                    'public': 'https://phemex.com/api',
                    'public2': 'https://api.phemex.com',
                    'private': 'https://api.phemex.com',
                },
                'doc': [
                    'https://github.com/phemex/phemex-api-docs',
                ],
                'api_management': 'https://phemex.com/web/account/api/list',
                'referral': 'https://phemex.com/?referralCode=D6XAJ',
                'fees': 'https://phemex.com/fees-conditions',
            },
            'api': {
                'public': {
                    'get': [
                        'exchange/public/products',
                    ],
                },
                'public2': {
                    'get': [
                        'md/orderbook',
                        'md/trade',
                    ],
                },
                'private': {
                    'get': [
                        'accounts/accountPositions',
                        'phemex-user/order',
                        'phemex-user/order/list',
                        'phemex-user/order/orderList',
                        'phemex-user/order/trade',
                        'orders/activeList',
                    ],
                    'post': [
                        'orders',
                    ],
                    'put': [],
                    'delete': [
                        'orders/cancel',
                    ],
                },
            },
            'exceptions': {
                'exact': {
                    'Invalid API Key.': AuthenticationError,
                    'This key is disabled.': PermissionDenied,
                    'Access Denied': PermissionDenied,
                    'Duplicate clOrdID': InvalidOrder,
                    'orderQty is invalid': InvalidOrder,
                    'Invalid price': InvalidOrder,
                    'Invalid stopPx for ordType': InvalidOrder,
                },
                'broad': {
                    'Signature not valid': AuthenticationError,
                    'overloaded': ExchangeNotAvailable,
                    'Account has insufficient Available Balance': InsufficientFunds,
                    'Service unavailable': ExchangeNotAvailable,
                    # {"error":{"message":"Service unavailable","name":"HTTPError"}}
                },
            },
            'precisionMode': DECIMAL_PLACES,
        })

    def fetch_markets(self, params={}):
        precisions = {
            'BTCUSD': {
                'amount': 0,
                'price': 1,
                'value': 8,
            },
            'ETHUSD': {
                'amount': 0,
                'price': 2,
                'value': 2,
            },
            'XRPUSD': {
                'amount': 0,
                'price': 4,
                'value': 2,
            },
        }
        method = 'publicGetExchangePublicProducts'
        response = getattr(self, method)(params)
        products = self.safe_value(response, 'data')
        productsCount = len(products)
        result = []
        for i in range(0, productsCount):
            market = self.parse_market(products[i], precisions)
            result.append(market)
        return result

    def fetch_order_book(self, symbol, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        method = 'public2GetMdOrderbook'
        response = getattr(self, method)({'symbol': marketID})
        data = self.parse_md_response(response)
        book = self.safe_value(data, 'book')
        return self.parse_order_book(book, None, 'bids', 'asks', 0, 1, market)

    def fetch_trades(self, symbol, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        method = 'public2GetMdTrade'
        response = getattr(self, method)({'symbol': marketID})
        data = self.parse_md_response(response)
        trades = self.safe_value(data, 'trades')
        return self.parse_md_trades(self.sort_by(trades, 0), market)

    def fetch_balance(self, params={}):
        self.load_markets()
        method = 'privateGetAccountsAccountPositions'
        btcResponse = getattr(self, method)({'currency': 'BTC'})
        usdResponse = getattr(self, method)({'currency': 'USD'})
        btcAccount = self.safe_value(self.parse_response(btcResponse), 'account')
        btcBalanceEv = self.safe_value(btcAccount, 'accountBalanceEv')
        btcTotalUsedBalanceEv = self.safe_value(btcAccount, 'totalUsedBalanceEv')
        usdAccount = self.safe_value(self.parse_response(usdResponse), 'account')
        usdBalanceEv = self.safe_value(usdAccount, 'accountBalanceEv')
        usdTotalUsedBalanceEv = self.safe_value(usdAccount, 'totalUsedBalanceEv')
        BTC = {
            'free': self.convert_ev(btcBalanceEv - btcTotalUsedBalanceEv, 8, 8),
            'used': self.convert_ev(btcTotalUsedBalanceEv, 8, 8),
            'total': self.convert_ev(btcBalanceEv, 8, 8),
        }
        USD = {
            'free': self.convert_ev(usdBalanceEv - usdTotalUsedBalanceEv, 4, 2),
            'used': self.convert_ev(usdTotalUsedBalanceEv, 4, 2),
            'total': self.convert_ev(usdBalanceEv, 4, 2),
        }
        return {
            'free': {
                'BTC': self.safe_string(BTC, 'free'),
                'USD': self.safe_string(USD, 'free'),
            },
            'used': {
                'BTC': self.safe_string(BTC, 'used'),
                'USD': self.safe_string(USD, 'used'),
            },
            'total': {
                'BTC': self.safe_string(BTC, 'total'),
                'USD': self.safe_string(USD, 'total'),
            },
            'BTC': BTC,
            'USD': USD,
            'info': {},
        }

    def fetch_order(self, id, symbol=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        method = 'privateGetPhemexUserOrder'
        response = getattr(self, method)({'orderID': id, 'symbol': marketID})
        orders = self.parse_response(response)
        orderCount = len(orders)
        if orderCount > 0:
            return self.parse_order(orders[0], market)
        raise OrderNotFound(self.id + ': The order ' + id + ' not found.')

    def fetch_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        method = 'privateGetPhemexUserOrderList'
        response = getattr(self, method)({'symbol': marketID, 'start': since, 'limit': limit})
        data = self.parse_response(response)
        orders = self.safe_value(data, 'rows', [])
        return self.parse_orders(orders, market)

    def fetch_open_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        method = 'privateGetOrdersActiveList'
        try:
            response = getattr(self, method)({'symbol': marketID})
            data = self.parse_response(response)
            orders = self.safe_value(data, 'rows')
            return self.parse_orders(orders, market)
        except Exception:
            return []

    def fetch_closed_orders(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        method = 'privateGetPhemexUserOrderList'
        response = getattr(self, method)({'symbol': marketID, 'start': since, 'limit': limit})
        data = self.parse_response(response)
        rawOrders = self.safe_value(data, 'rows')
        orders = self.parse_orders(rawOrders, market)
        orderCount = len(orders)
        result = []
        for i in range(0, orderCount):
            order = orders[i]
            status = self.safe_string(order, 'status')
            if status == 'closed':
                result.append(order)
        return result

    def create_order(self, symbol, type, side, amount, price=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        request = {
            'clOrdID': self.uuid(),
            'symbol': marketID,
            'side': self.capitalize(side),
            'orderQty': amount,
            'ordType': self.capitalize(type),
            'postOnly': False,
            'reduceOnly': False,
            'timeInForce': self.safe_string(params, 'timeInForce', 'GoodTillCancel'),
        }
        if price is not None:
            request['priceEp'] = self.convert_to_ep(price)
        method = 'privatePostOrders'
        response = getattr(self, method)(self.extend(request, params))
        order = self.parse_order(response, market)
        id = self.safe_string(order, 'id')
        self.orders[id] = order
        return self.extend({'info': response}, order)

    def cancel_order(self, id, symbol=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        method = 'privateDeleteOrdersCancel'
        try:
            response = getattr(self, method)({'orderID': id, 'symbol': marketID})
            order = self.parse_response(response)
            return self.parse_order(order, market)
        except Exception:
            raise OrderNotFound(self.id + ': The order ' + id + ' not found.')

    def fetch_my_trades(self, symbol=None, since=None, limit=None, params={}):
        self.load_markets()
        market = self.market(symbol)
        marketID = market['id']
        method = 'privateGetPhemexUserOrderTrade'
        response = getattr(self, method)({'symbol': marketID, 'start': since, 'limit': limit})
        data = self.parse_response(response)
        trades = self.safe_value(data, 'rows', [])
        return self.parse_my_trades(trades, market)

    def handle_errors(self, httpCode, reason, url, method, headers, body, response, requestHeaders, requestBody):
        if httpCode == 429:
            raise DDoSProtection(self.id + ' ' + str(httpCode) + ' ' + reason + ' ' + body)
        code = self.safe_value(response, 'code', 0)
        if code != 0:
            message = self.safe_string(response, 'msg')
            raise ExchangeError(self.id + ' ' + message)

    def nonce(self):
        return self.milliseconds()

    def sign(self, path, api='public', method='GET', params={}, headers=None, body=None):
        urlPath = '/' + path
        querystring = ''
        if method == 'GET' or method == 'DELETE':
            keys = list(params.keys())
            keysCount = len(keys)
            if keysCount > 0:
                cleanParams = {}
                for i in range(0, keysCount):
                    key = keys[i]
                    if params[key] is not None:
                        cleanParams[key] = params[key]
                cleanKeys = list(cleanParams.keys())
                cleanKeysCount = len(cleanKeys)
                if cleanKeysCount > 0:
                    querystring = self.urlencode_with_array_repeat(cleanParams)
        else:
            body = self.json(params)
        url = self.urls['api'][api] + urlPath + ''
        if querystring != '':
            url += '?' + querystring
        if self.apiKey and self.secret:
            expiry = self.number_to_string(self.seconds() + 2 * 60)
            content = urlPath + querystring + expiry
            if body:
                content += body
            signature = self.hmac(content, self.secret)
            headers = {
                'Content-Type': 'application/json',
                'x-phemex-access-token': self.apiKey,
                'x-phemex-request-expiry': expiry,
                'x-phemex-request-signature': signature,
            }
        return {'url': url, 'method': method, 'headers': headers, 'body': body}
