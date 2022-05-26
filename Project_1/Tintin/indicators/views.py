from django.shortcuts import render
from indicators.models import RSI, MOVINGAVG28, MOVINGAVG84, MOVINGAVG168
from . import forms

# generate random integer values



# Create your views here.
def index(request):
    return render(request, 'default_layout.html')

def indicators(request):

    form = forms.FormName()
    rsi_list = RSI.objects.order_by('-date')
    mvgAVG_28_list = MOVINGAVG28.objects.order_by('-date')
    mvgAVG_84_list = MOVINGAVG84.objects.order_by('-date')
    mvgAVG_168_list = MOVINGAVG168.objects.order_by('-date')
    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            print(symbol)
            print(type(symbol))
            rsi_list = RSI.objects.filter(symbol=symbol).order_by('-date')
            mvgAVG_28_list = MOVINGAVG28.objects.filter(symbol=symbol).order_by('-date')
            mvgAVG_84_list = MOVINGAVG84.objects.filter(symbol=symbol).order_by('-date')
            mvgAVG_168_list = MOVINGAVG168.objects.filter(symbol=symbol).order_by('-date')




    timeframe_list = ['1h','4h','1d']



    data_dict = {
        'rsi':rsi_list,
        'mvgAVG_28':mvgAVG_28_list,
        'mvgAVG_84':mvgAVG_84_list,
        'mvgAVG_168':mvgAVG_168_list,
        'timeframe':timeframe_list,
        'form':form,
        }

    return render(request, 'indicators/display.html', context=data_dict)




"""

import random

def random_list(number_of_elements):
    final_list = []
    i=0
    while i < number_of_elements:
        final_list.append(random.randint(1,10))
        i+=1
    return final_list



    helpfull_dict = {
              'timeframe' : ['1h','4h','1d','3d'],
              'indicators' : ['rsi','macd','obv','volume','volatility','stoc_rsi','MA100_dif','MA200_dif'],
              'exchange_list' : ['Binance', 'Coinbase', 'Bitfinex'],
              'fake_numers' : random_list(4)
              }

    data_dict = {'indicators':helpfull_dict['indicators'],'timeframe':helpfull_dict['timeframe'], 'fake_numers':helpfull_dict['fake_numers']}"""
