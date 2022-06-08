from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.decorators.csrf import csrf_exempt

import json


helpfull_list = [0]
# Create your views here.

@csrf_exempt
def testcall(request):

    a = request.POST['text']

    helpfull_list[0] = float(a) + helpfull_list[0]
    print(a)
    print(helpfull_list[0])
    data_dict = {'quantity':helpfull_list}
    return render(request, 'market_orders/display.html', context=data_dict)

"""return HttpResponse(request.POST['text'])"""


def index(request):

    return render(request, 'default_layout.html')

@csrf_exempt
def market_orders(request):

    helpfull_dict = {
              'timeframe' : ['1h','4h','1d','3d'],
              'indicators' : ['rsi','macd','obv','volume','volatility','stoc_rsi','MA100_dif','MA200_dif'],
              'exchange_list' : ['Binance', 'Coinbase', 'Bitfinex'],
              }

    data_dict = {'exchange_list':helpfull_dict['exchange_list']}

    return render(request, 'market_orders/display.html', context=data_dict)


class AjaxHandlerView(View):
    """docstring for AjaxHandlerView."""

    def get(self, request):
        text = request.GET.get('value')
        print('PILAAAAAAAAA')
        print(type(text))
        pass
