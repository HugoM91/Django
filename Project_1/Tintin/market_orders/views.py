from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'default_layout.html')

def market_orders(request):

    helpfull_dict = {
              'timeframe' : ['1h','4h','1d','3d'],
              'indicators' : ['rsi','macd','obv','volume','volatility','stoc_rsi','MA100_dif','MA200_dif'],
              'exchange_list' : ['Binance', 'Coinbase', 'Bitfinex'],
              }

    data_dict = {'exchange_list':helpfull_dict['exchange_list']}

    return render(request, 'market_orders/display.html', context=data_dict)
